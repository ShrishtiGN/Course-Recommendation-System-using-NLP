"""Test script to check if all imports work correctly"""

print("Testing imports...")

try:
    import streamlit as st
    print("✓ streamlit imported")
except ImportError as e:
    print(f"✗ streamlit import failed: {e}")

try:
    import pandas as pd
    print("✓ pandas imported")
except ImportError as e:
    print(f"✗ pandas import failed: {e}")

try:
    import numpy as np
    print("✓ numpy imported")
except ImportError as e:
    print(f"✗ numpy import failed: {e}")

try:
    from surprise import SVD
    print("✓ scikit-surprise imported")
except ImportError as e:
    print(f"✗ scikit-surprise import failed: {e}")

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    print("✓ scikit-learn imported")
except ImportError as e:
    print(f"✗ scikit-learn import failed: {e}")

try:
    from data_preprocessing import DataPreprocessor
    print("✓ data_preprocessing imported")
except ImportError as e:
    print(f"✗ data_preprocessing import failed: {e}")

try:
    from collaborative_filtering import CollaborativeFiltering
    print("✓ collaborative_filtering imported")
except ImportError as e:
    print(f"✗ collaborative_filtering import failed: {e}")

try:
    from content_based_filtering import ContentBasedFiltering
    print("✓ content_based_filtering imported")
except ImportError as e:
    print(f"✗ content_based_filtering import failed: {e}")

try:
    from hybrid_recommender import HybridRecommender
    print("✓ hybrid_recommender imported")
except ImportError as e:
    print(f"✗ hybrid_recommender import failed: {e}")

try:
    from evaluation_metrics import EvaluationMetrics
    print("✓ evaluation_metrics imported")
except ImportError as e:
    print(f"✗ evaluation_metrics import failed: {e}")

print("\nAll imports completed!")


