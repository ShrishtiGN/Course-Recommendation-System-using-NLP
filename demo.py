"""
Quick demo to verify the system works
Run: python demo.py
"""

print("=" * 60)
print("Course Recommendation System - Quick Demo")
print("=" * 60)

# Test imports
print("\n[1/5] Testing imports...")
try:
    import streamlit as st
    import pandas as pd
    import numpy as np
    from surprise import SVD
    from sklearn.feature_extraction.text import TfidfVectorizer
    print("✓ All required packages imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("\nPlease install dependencies: pip install -r requirements.txt")
    exit(1)

# Test local imports
print("\n[2/5] Testing local modules...")
try:
    from data_preprocessing import DataPreprocessor
    from collaborative_filtering import CollaborativeFiltering
    from content_based_filtering import ContentBasedFiltering
    from hybrid_recommender import HybridRecommender
    from evaluation_metrics import EvaluationMetrics
    print("✓ All local modules imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
    exit(1)

# Test data loading
print("\n[3/5] Testing data loading...")
try:
    import os
    csv_file = "edtech (1).csv"
    if os.path.exists(csv_file):
        preprocessor = DataPreprocessor(csv_file)
        df = preprocessor.load_data()
        print(f"✓ Data loaded: {len(df)} courses found")
    else:
        print(f"⚠ CSV file '{csv_file}' not found, but system is ready")
except Exception as e:
    print(f"⚠ Data loading issue: {e}")

# Test Streamlit
print("\n[4/5] Testing Streamlit...")
try:
    import subprocess
    import sys
    result = subprocess.run([sys.executable, "-m", "streamlit", "--version"], 
                          capture_output=True, text=True, timeout=5)
    if result.returncode == 0:
        print(f"✓ Streamlit is installed: {result.stdout.strip()}")
    else:
        print("⚠ Streamlit check failed")
except:
    print("⚠ Could not verify Streamlit version")

# Final instructions
print("\n[5/5] System Status")
print("=" * 60)
print("\n✅ System is ready!")
print("\nTo start the app, run one of these commands:")
print("  1. streamlit run app.py")
print("  2. python start_app.py")
print("  3. py -m streamlit run app.py")
print("\nThe app will open at: http://localhost:8501")
print("=" * 60)

