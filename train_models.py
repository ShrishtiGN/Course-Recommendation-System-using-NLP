"""
Offline Model Training Script
Train all recommendation models and save them
"""

import pandas as pd
import os
from data_preprocessing import DataPreprocessor
from collaborative_filtering import CollaborativeFiltering
from content_based_filtering import ContentBasedFiltering
from hybrid_recommender import HybridRecommender

def train_all_models(csv_path: str, n_users: int = 1000, sparsity: float = 0.7,
                    n_factors: int = 50, n_epochs: int = 20,
                    cf_weight: float = 0.6, cb_weight: float = 0.4):
    """
    Train all recommendation models
    
    Args:
        csv_path: Path to CSV dataset
        n_users: Number of synthetic users
        sparsity: Data sparsity level
        n_factors: CF number of factors
        n_epochs: CF number of epochs
        cf_weight: Hybrid CF weight
        cb_weight: Hybrid CB weight
    """
    print("=" * 60)
    print("Course Recommendation System - Model Training")
    print("=" * 60)
    
    # Create models directory
    os.makedirs('models', exist_ok=True)
    
    # Step 1: Load and preprocess data
    print("\n[1/4] Loading and preprocessing data...")
    preprocessor = DataPreprocessor(csv_path)
    df = preprocessor.load_data()
    print(f"   ✓ Loaded {len(df)} courses")
    
    # Step 2: Generate synthetic ratings
    print("\n[2/4] Generating synthetic user ratings...")
    ratings_df = preprocessor.generate_synthetic_ratings(
        n_users=n_users, sparsity=sparsity
    )
    print(f"   ✓ Generated {len(ratings_df)} ratings for {n_users} users")
    
    # Step 3: Train Collaborative Filtering
    print("\n[3/4] Training Collaborative Filtering model...")
    cf_model = CollaborativeFiltering(
        n_factors=n_factors, n_epochs=n_epochs
    )
    cf_model.train(ratings_df)
    cf_metrics = cf_model.evaluate()
    print(f"   ✓ CF Model trained - RMSE: {cf_metrics['RMSE']:.4f}")
    cf_model.save_model('models/cf_model.pkl')
    
    # Step 4: Train Content-Based
    print("\n[4/4] Training Content-Based model...")
    courses_df = preprocessor.get_course_metadata()
    cb_model = ContentBasedFiltering()
    cb_model.train(courses_df)
    print(f"   ✓ CB Model trained")
    cb_model.save_model('models/cb_model.pkl')
    
    # Step 5: Create Hybrid Model
    print("\n[5/5] Creating Hybrid model...")
    hybrid_model = HybridRecommender(cf_model, cb_model, cf_weight, cb_weight)
    print(f"   ✓ Hybrid Model created (CF weight: {cf_weight}, CB weight: {cb_weight})")
    
    # Save metadata
    metadata = {
        'n_users': n_users,
        'n_courses': len(df),
        'n_ratings': len(ratings_df),
        'cf_weight': cf_weight,
        'cb_weight': cb_weight
    }
    
    import pickle
    with open('models/metadata.pkl', 'wb') as f:
        pickle.dump(metadata, f)
    
    print("\n" + "=" * 60)
    print("✓ All models trained and saved successfully!")
    print("=" * 60)
    print(f"\nModels saved in: {os.path.abspath('models')}")
    print("\nYou can now use the Streamlit app to load these models.")

if __name__ == "__main__":
    import sys
    
    # Default parameters
    csv_path = "edtech (1).csv"
    n_users = 1000
    sparsity = 0.7
    n_factors = 50
    n_epochs = 20
    cf_weight = 0.6
    cb_weight = 0.4
    
    # Parse command line arguments if provided
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
    if len(sys.argv) > 2:
        n_users = int(sys.argv[2])
    if len(sys.argv) > 3:
        sparsity = float(sys.argv[3])
    
    train_all_models(
        csv_path=csv_path,
        n_users=n_users,
        sparsity=sparsity,
        n_factors=n_factors,
        n_epochs=n_epochs,
        cf_weight=cf_weight,
        cb_weight=cb_weight
    )


