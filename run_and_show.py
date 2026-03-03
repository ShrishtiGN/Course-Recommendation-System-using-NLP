"""
Script to demonstrate what happens when you run the Streamlit app
"""

import subprocess
import sys
import os
import time

print("=" * 70)
print("COURSE RECOMMENDATION SYSTEM - STARTING SERVER")
print("=" * 70)
print()

# Check if we're in the right directory
if not os.path.exists("app.py"):
    print("ERROR: app.py not found in current directory!")
    print(f"Current directory: {os.getcwd()}")
    sys.exit(1)

print("✓ Found app.py")
print()

# Try different Python commands
python_commands = ["python", "py", "python3"]

print("Attempting to start Streamlit server...")
print("-" * 70)
print()

for cmd in python_commands:
    try:
        # Check if command exists
        result = subprocess.run([cmd, "--version"], 
                              capture_output=True, 
                              text=True, 
                              timeout=2)
        if result.returncode == 0:
            print(f"✓ Found Python: {cmd}")
            print(f"  Version: {result.stdout.strip()}")
            print()
            
            # Try to run streamlit
            print("Starting Streamlit...")
            print("-" * 70)
            print()
            print("EXPECTED OUTPUT:")
            print("=" * 70)
            print("""
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501

  For better performance, install watchdog:
    pip install watchdog
            """)
            print("=" * 70)
            print()
            print("Starting server now...")
            print("(Press Ctrl+C to stop)")
            print()
            print("-" * 70)
            
            # Actually run streamlit
            subprocess.run([cmd, "-m", "streamlit", "run", "app.py"])
            break
    except FileNotFoundError:
        continue
    except subprocess.TimeoutExpired:
        continue
    except Exception as e:
        print(f"Error with {cmd}: {e}")
        continue
else:
    print("ERROR: Could not find Python!")
    print()
    print("SOLUTIONS:")
    print("1. Install Python from https://www.python.org/downloads/")
    print("2. Make sure Python is added to PATH during installation")
    print("3. Or use: py -m streamlit run app.py")
    print("4. Or use: python3 -m streamlit run app.py")
    print()
    print("Once Python is installed, run:")
    print("  pip install -r requirements.txt")
    print("  streamlit run app.py")

