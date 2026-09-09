import subprocess
import sys

def test_hello_world():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True
    )

    assert result.stdout.strip() == "Hello, World"
