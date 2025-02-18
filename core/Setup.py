import os
import sys
import subprocess
import venv

# Define venv path
VENV_DIR = "BlockHut_venv"  # Change this if needed

# Function to create a virtual environment if it doesn't exist
def create_venv():
    if not os.path.exists(VENV_DIR):
        print(f"Creating virtual environment in {VENV_DIR}...")
        venv.create(VENV_DIR, with_pip=True)
    else:
        print(f"Virtual environment {VENV_DIR} already exists.")

# Function to install dependencies inside the venv
def install_dependencies(packages):
    python_executable = os.path.join(VENV_DIR, "Scripts", "python.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    
    print(f"Installing dependencies: {', '.join(packages)}...")
    subprocess.check_call([python_executable, "-m", "pip", "install", *packages])

# Function to run another script inside the venv
def run_script(script_path):
    python_executable = os.path.join(VENV_DIR, "Scripts", "python.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")
    
    print(f"Running {script_path} inside the virtual environment...")
    subprocess.check_call([python_executable, script_path])

# Main logic
if __name__ == "__main__":
    create_venv()
    install_dependencies(["tqdm", "requests","keyboard"])  # Add dependencies here
    run_script("BlockHutUI.py")  # Replace with the script you want to run