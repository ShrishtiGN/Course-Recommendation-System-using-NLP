"""
Diagnostic script to check why Streamlit app won't run
"""

import sys
import os

print("=" * 70)
print("DIAGNOSING STREAMLIT APP ISSUES")
print("=" * 70)
print()

# Check 1: Python version
print("[1] Checking Python...")
try:
    print(f"   Python version: {sys.version}")
    print(f"   Python executable: {sys.executable}")
    print("   ✓ Python is working")
except Exception as e:
    print(f"   ✗ Python error: {e}")
    sys.exit(1)

print()

# Check 2: Required packages
print("[2] Checking required packages...")
required_packages = {
    'streamlit': 'streamlit',
    'pandas': 'pandas',
    'numpy': 'numpy',
    'sklearn': 'scikit-learn',
    'surprise': 'scikit-surprise',
    'matplotlib': 'matplotlib',
    'seaborn': 'seaborn'
}

missing_packages = []
for module, package in required_packages.items():
    try:
        __import__(module)
        print(f"   ✓ {package}")
    except ImportError:
        print(f"   ✗ {package} - MISSING")
        missing_packages.append(package)

if missing_packages:
    print()
    print("   Install missing packages with:")
    print(f"   pip install {' '.join(missing_packages)}")
    print("   OR:")
    print("   pip install -r requirements.txt")

print()

# Check 3: Local modules
print("[3] Checking local modules...")
local_modules = [
    'data_preprocessing',
    'collaborative_filtering',
    'content_based_filtering',
    'hybrid_recommender',
    'evaluation_metrics'
]

for module in local_modules:
    try:
        __import__(module)
        print(f"   ✓ {module}.py")
    except ImportError as e:
        print(f"   ✗ {module}.py - ERROR: {e}")

print()

# Check 4: App file
print("[4] Checking app.py...")
if os.path.exists("app.py"):
    print("   ✓ app.py exists")
    try:
        with open("app.py", "r", encoding="utf-8") as f:
            content = f.read()
            if "streamlit" in content:
                print("   ✓ Contains Streamlit code")
            if "def main" in content:
                print("   ✓ Has main function")
    except Exception as e:
        print(f"   ✗ Error reading app.py: {e}")
else:
    print("   ✗ app.py NOT FOUND")
    print(f"   Current directory: {os.getcwd()}")

print()

# Check 5: CSV file
print("[5] Checking dataset...")
csv_files = [f for f in os.listdir(".") if f.endswith(".csv")]
if csv_files:
    print(f"   ✓ Found CSV files: {', '.join(csv_files)}")
else:
    print("   ⚠ No CSV files found (you can upload via UI)")

print()

# Check 6: Streamlit command
print("[6] Testing Streamlit installation...")
try:
    import subprocess
    result = subprocess.run(
        [sys.executable, "-m", "streamlit", "--version"],
        capture_output=True,
        text=True,
        timeout=5
    )
    if result.returncode == 0:
        print(f"   ✓ Streamlit version: {result.stdout.strip()}")
    else:
        print(f"   ✗ Streamlit check failed: {result.stderr}")
except Exception as e:
    print(f"   ✗ Cannot check Streamlit: {e}")

print()
print("=" * 70)
print("DIAGNOSIS COMPLETE")
print("=" * 70)
print()

if missing_packages:
    print("ACTION REQUIRED:")
    print(f"   Install missing packages: pip install {' '.join(missing_packages)}")
    print()
else:
    print("ALL CHECKS PASSED!")
    print()
    print("Try running:")
    print("   streamlit run app.py")
    print()
    print("If that doesn't work, try:")
    print(f"   {sys.executable} -m streamlit run app.py")

