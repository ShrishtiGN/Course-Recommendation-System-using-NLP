"""Simple test to check if Streamlit can run"""
import sys

print("Testing Streamlit...")
print(f"Python: {sys.executable}")
print()

try:
    import streamlit as st
    print("✓ Streamlit imported successfully")
    print(f"  Version: {st.__version__}")
    print()
    print("Try running: streamlit run app.py")
except ImportError as e:
    print("✗ Streamlit not installed")
    print(f"  Error: {e}")
    print()
    print("Install with: pip install streamlit")
    sys.exit(1)

print("All checks passed!")

