"""
Collaborative Filtering Module
Implements Matrix Factorization using SVD
"""

import numpy as np
import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy
import pickle
import os


class CollaborativeFiltering:
    """Collaborative Filtering using SVD Matrix Factorization"""
    
    def __init__(self, n_factors: int = 50, n_epochs: int = 20, 
                 lr_all: float = 0.005, reg_all: float = 0.02):
        """
        Initialize the collaborative filtering model
        
        Args:
            n_factors: Number of factors for matrix factorization
            n_epochs: Number of training epochs
            lr_all: Learning rate
            reg_all: Regularization parameter
        """
        self.model = SVD(
            n_factors=n_factors,
            n_epochs=n_epochs,
            lr_all=lr_all,
            reg_all=reg_all,
            random_state=42
        )
        self.trainset = None
        self.testset = None
        
    def train(self, ratings_df: pd.DataFrame, test_size: float = 0.2):
        """
        Train the collaborative filtering model
        
        Args:
            ratings_df: DataFrame with columns: user_id, course_id, rating
            test_size: Proportion of data to use for testing
        """
        # Prepare data for Surprise
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(
            ratings_df[['user_id', 'course_id', 'rating']],
            reader
        )
        
        # Split data
        self.trainset, self.testset = train_test_split(
            data, test_size=test_size, random_state=42
        )
        
        # Train model
        self.model.fit(self.trainset)
        
    def predict(self, user_id: int, course_id: int) -> float:
        """
        Predict rating for a user-course pair
        
        Args:
            user_id: User ID
            course_id: Course ID
            
        Returns:
            Predicted rating
        """
        prediction = self.model.predict(user_id, course_id)
        return prediction.est
    
    def get_top_n_recommendations(self, user_id: int, n: int = 10,
                                 courses_df: pd.DataFrame = None) -> list:
        """
        Get top N course recommendations for a user
        
        Args:
            user_id: User ID
            n: Number of recommendations
            courses_df: DataFrame with course information
            
        Returns:
            List of recommended course IDs with predicted ratings
        """
        if self.trainset is None:
            raise ValueError("Model not trained. Call train() first.")
        
        # Get all courses
        all_courses = set(self.trainset.all_items())
        
        # Get courses already rated by user
        user_ratings = self.trainset.ur[self.trainset.to_inner_uid(user_id)]
        rated_courses = {self.trainset.to_raw_iid(iid) for (iid, _) in user_ratings}
        
        # Get unrated courses
        unrated_courses = all_courses - rated_courses
        
        # Predict ratings for unrated courses
        predictions = []
        for course_id in unrated_courses:
            pred_rating = self.predict(user_id, course_id)
            predictions.append((course_id, pred_rating))
        
        # Sort by predicted rating and get top N
        predictions.sort(key=lambda x: x[1], reverse=True)
        top_n = predictions[:n]
        
        # Format results
        recommendations = []
        for course_id, rating in top_n:
            rec = {'course_id': int(course_id), 'predicted_rating': round(rating, 2)}
            if courses_df is not None:
                course_info = courses_df[courses_df['course_id'] == int(course_id)]
                if not course_info.empty:
                    rec['title'] = course_info.iloc[0]['title']
                    rec['developer'] = course_info.iloc[0]['developer']
            recommendations.append(rec)
        
        return recommendations
    
    def evaluate(self) -> dict:
        """
        Evaluate the model using RMSE
        
        Returns:
            Dictionary with evaluation metrics
        """
        if self.testset is None:
            raise ValueError("Test set not available. Train model first.")
        
        predictions = self.model.test(self.testset)
        rmse = accuracy.rmse(predictions, verbose=False)
        
        return {'RMSE': rmse}
    
    def save_model(self, filepath: str):
        """Save the trained model"""
        os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump(self.model, f)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath: str):
        """Load a trained model"""
        with open(filepath, 'rb') as f:
            self.model = pickle.load(f)
        print(f"Model loaded from {filepath}")


