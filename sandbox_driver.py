import os
import docker

def run_code_in_sandbox(code_string: str) -> dict:
    """
    Runs Python code inside a temporary, isolated Docker container with local volume mounting.
    """
    client = docker.from_env()
    
    try:
        # Execute code inside isolated environment with attached local volume for saving output files
        container_output = client.containers.run(
            image="data-copilot-sandbox",
            command=["python", "-c", code_string],
            network="copilot-net",
            volumes={
                os.path.abspath("."): {'bind': '/workspace', 'mode': 'rw'}
            },
            working_dir="/workspace",
            detach=False,
            remove=True,           # Automatically remove the container when it exits
            mem_limit="256m",      # Restrict memory allocation to 256MB
            network_disabled=False,
            stdout=True,
            stderr=True
        )
        return {"status": "success", "output": container_output.decode('utf-8').strip()}
    except docker.errors.ContainerError as e:
        # Catch errors raised by the code running inside the container
        return {"status": "error", "error": e.stderr.decode('utf-8').strip()}
    except Exception as e:
        return {"status": "system_error", "error": str(e)}

if __name__ == "__main__":
    print("--- Test 1: Valid Code ---")
    res1 = run_code_in_sandbox("print('Hello World from Docker Sandbox!')")
    print(res1)

    print("\n--- Test 2: Error-producing Code ---")
    res2 = run_code_in_sandbox("print(10 / 0)")
    print(res2)