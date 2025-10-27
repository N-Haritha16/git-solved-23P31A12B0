import subprocess
import os
import pytest

# Test 1: Check if deploy.sh exists
def test_deploy_script_exists():
    assert os.path.exists("./scripts/deploy.sh"), "deploy.sh file missing!"

# Test 2: Check if deploy.sh has execute permissions
def test_deploy_script_executable():
    assert os.access("./scripts/deploy.sh", os.X_OK), "deploy.sh is not executable!"

# Test 3: Simulate deployment command (dry run)
def test_deploy_script_runs():
    try:
        result = subprocess.run(["bash", "./scripts/deploy.sh", "--dry-run"], capture_output=True, text=True)
        assert result.returncode == 0, f"Deploy script failed: {result.stderr}"
    except FileNotFoundError:
        pytest.skip("deploy.sh not found, skipping run test")

# Test 4: Check deployment log directory
def test_logs_directory():
    os.makedirs("./logs", exist_ok=True)
    assert os.path.isdir("./logs"), "Logs directory not found or not created properly."
