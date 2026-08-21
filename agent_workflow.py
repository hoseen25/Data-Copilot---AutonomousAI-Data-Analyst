import os
import glob
from dotenv import load_dotenv

load_dotenv()

from pydantic_ai import Agent, RunContext
from sandbox_driver import run_code_in_sandbox

# Define System Prompt with database instructions and visualization rules
SYSTEM_INSTRUCTION = (
    "You are an expert Python Data Analyst agent.\n"
    "Your goal is to solve the user request by generating Python code and executing it via the `execute_python_code` tool.\n\n"
    "Database Details:\n"
    "- host: copilot_postgres\n"
    "- port: 5432\n"
    "- user: postgres\n"
    "- password: password123\n"
    "- dbname: postgres\n\n"
    "CRITICAL VISUALIZATION RULES:\n"
    "- Never use `plt.show()`.\n"
    "- Always save plots as PNG using `plt.savefig('output_chart.png', bbox_inches='tight')`.\n"
    "- Always call `plt.close()` after saving."
)

# Initialize PydanticAI Agent instance
agent = Agent(
    'groq:openai/gpt-oss-20b',
    system_prompt=SYSTEM_INSTRUCTION
)

# Tool definition inside PydanticAI Agent SDK framework
@agent.tool
def execute_python_code(ctx: RunContext[None], code: str) -> str:
    """
    Executes generated Python code inside the Docker sandbox.
    """
    # Clean up existing PNG files before running new code
    for old_file in glob.glob("*.png"):
        try:
            os.remove(old_file)
        except Exception:
            pass

    cleaned_code = code.strip().replace("```python", "").replace("```", "").strip()
    result = run_code_in_sandbox(cleaned_code)

    if result["status"] == "success":
        return f"Execution Output:\n{result['output']}"
    else:
        return f"Execution Error:\n{result['error']}"

# Wrapper class to maintain compatibility with app.py
class AgentSDKWrapper:
    def invoke(self, state: dict) -> dict:
        prompt = f"Chat History:\n{state.get('chat_history', '')}\n\nUser Query: {state['user_query']}"
        
        # Execute agent run through Agent SDK
        run_result = agent.run_sync(prompt)
        
        created_images = glob.glob("*.png")
        return {
            "output": str(run_result.output),
            "generated_files": created_images
        }

app = AgentSDKWrapper()