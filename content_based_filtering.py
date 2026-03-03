"""
Content-Based Filtering Module
Implements TF-IDF vectorization and Cosine Similarity
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os


class ContentBasedFiltering:
    """Content-Based Filtering using TF-IDF and Cosine Similarity"""
    
    def __init__(self, max_features: int = 5000, ngram_range: tuple = (1, 2)):
        """
        Initialize the content-based filtering model
        
        Args:
            max_features: Maximum number of features for TF-IDF
            ngram_range: N-gram range for TF-IDF
        """
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=ngram_range,
            stop_words='english',
            lowercase=True
        )
        self.tfidf_matrix = None
        self.courses_df = None
        
    def train(self, courses_df: pd.DataFrame, description_col: str = 'description'):
        """
        Train the content-based model
        
        Args:
            courses_df: DataFrame with course information
            description_col: Column name containing course descriptions
        """
        self.courses_df = courses_df.copy()
        
        # Create TF-IDF matrix
        descriptions = self.courses_df[description_col].fillna('').astype(str)
        self.tfidf_matrix = self.vectorizer.fit_transform(descriptions)
        
        print(f"TF-IDF matrix shape: {self.tfidf_matrix.shape}")
        
    def get_similar_courses(self, course_id: int, n: int = 10) -> list:
        """
        Get similar courses based on content similarity
        
        Args:
            course_id: Course ID to find similar courses for
            n: Number of similar courses to return
            
        Returns:
            List of similar course IDs with similarity scores
        """
        if self.tfidf_matrix is None:
            raise ValueError("Model not trained. Call train() first.")
        
        # Get course index
        course_idx = self.courses_df[
            self.courses_df['course_id'] == course_id
        ].index
        
        if len(course_idx) == 0:
            return []
        
        course_idx = course_idx[0]
        
        # Calculate cosine similarity
        course_vector = self.tfidf_matrix[course_idx:course_idx+1]
        similarities = cosine_similarity(course_vector, self.tfidf_matrix).flatten()
        
        # Get top N similar courses (excluding the course itself)
        similar_indices = np.argsort(similarities)[::-1][1:n+1]
        
        recommendations = []
        for idx in similar_indices:
            course_info = self.courses_df.iloc[idx]
            recommendations.append({
                'course_id': int(course_info['course_id']),
                'similarity_score': round(float(similarities[idx]), 4),
                'title': course_info['title'],
                'developer': course_info['developer']
            })
        
        return recommendations
    
    def get_user_recommendations(self, user_rated_courses: list, 
                                user_ratings: list, n: int = 10) -> list:
        """
        Get content-based recommendations for a user based on their rated courses
        
        Args:
            user_rated_courses: List of course IDs the user has rated
            user_ratings: List of ratings corresponding to the courses
            n: Number of recommendations to return
            
        Returns:
            List of recommended courses
        """
        if self.tfidf_matrix is None:
            raise ValueError("Model not trained. Call train() first.")
        
        # Get user profile (weighted average of rated courses)
        user_profile = None
        total_weight = 0
        
        for course_id, rating in zip(user_rated_courses, user_ratings):
            course_idx = self.courses_df[
                self.courses_df['course_id'] == course_id
            ].index
            
            if len(course_idx) > 0:
                course_vector = self.tfidf_matrix[course_idx[0]:course_idx[0]+1]
                weight = rating / 5.0  # Normalize rating to 0-1
                
                if user_profile is None:
                    user_profile = course_vector * weight
                else:
                    user_profile += course_vector * weight
                
                total_weight += weight
        
        if user_profile is None or total_weight == 0:
            return []
        
        # Normalize user profile
        user_profile = user_profile / total_weight
        
        # Calculate similarity with all courses
        similarities = cosine_similarity(user_profile, self.tfidf_matrix).flatten()
        
        # Exclude already rated courses
        rated_indices = self.courses_df[
            self.courses_df['course_id'].isin(user_rated_courses)
        ].index
        
        similarities[rated_indices] = -1
        
        # Get top N recommendations
        top_indices = np.argsort(similarities)[::-1][:n]
        
        recommendations = []
        for idx in top_indices:
            if similarities[idx] > 0:
                course_info = self.courses_df.iloc[idx]
                recommendations.append({
                    'course_id': int(course_info['course_id']),
                    'similarity_score': round(float(similarities[idx]), 4),
                    'title': course_info['title'],
                    'developer': course_info['developer']
                })
        
        return recommendations
    
    def save_model(self, filepath: str):
        """Save the trained model"""
        os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
        model_data = {
            'vectorizer': self.vectorizer,
            'tfidf_matrix': self.tfidf_matrix,
            'courses_df': self.courses_df
        }
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath: str):
        """Load a trained model"""
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
        self.vectorizer = model_data['vectorizer']
        self.tfidf_matrix = model_data['tfidf_matrix']
        self.courses_df = model_data['courses_df']
        print(f"Model loaded from {filepath}")


