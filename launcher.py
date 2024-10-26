import subprocess
import signal
import os
import sys
import time

# List to hold the subprocesses
processes = []

def run_script(script_name):
    """Run a Python script in a subprocess."""
    process = subprocess.Popen([sys.executable, script_name])
    processes.append(process)

def terminate_processes():
    """Terminate all the subprocesses."""
    for process in processes:
        process.terminate()
    for process in processes:
        process.wait()  # Wait for processes to terminate

if __name__ == "__main__":
    try:
        # Run both scripts
        run_script("./frontend/puzzle-8-game/server.py")
        run_script("./backend/server.py")

        print("Both scripts are running in the background.")

        # Keep the controller running until a keyboard interrupt (Ctrl+C)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTerminating the scripts...")
        terminate_processes()
        print("All scripts have been terminated.")
