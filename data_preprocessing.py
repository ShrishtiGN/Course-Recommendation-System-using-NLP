"""
Data Preprocessing Module
Handles data loading, cleaning, and synthetic user rating generation
"""

import pandas as pd
import numpy as np
from typing import Tuple, Dict


class DataPreprocessor:
    """Preprocesses EdTech dataset and generates synthetic user ratings"""
    
    def __init__(self, csv_path: str):
        """
        Initialize the preprocessor
        
        Args:
            csv_path: Path to the CSV file (can be file path or file-like object)
        """
        self.csv_path = csv_path
        self.df = None
        self.ratings_df = None
        
    def load_data(self) -> pd.DataFrame:
        """Load and clean the dataset"""
        self.df = pd.read_csv(self.csv_path)
        
        # Clean data
        self.df = self.df.dropna(subset=['title', 'score'])
        
        # Fill missing values
        self.df['ratings'] = self.df['ratings'].fillna(0)
        self.df['reviews'] = self.df['reviews'].fillna(0)
        self.df['developer'] = self.df['developer'].fillna('Unknown')
        self.df['contentRating'] = self.df['contentRating'].fillna('Everyone')
        
        # Create course ID
        self.df['course_id'] = range(len(self.df))
        
        return self.df
    
    def generate_synthetic_ratings(self, n_users: int = 1000, 
                                   sparsity: float = 0.7,
                                   random_seed: int = 42) -> pd.DataFrame:
        """
        Generate synthetic user ratings based on course scores and popularity
        
        Args:
            n_users: Number of synthetic users to generate
            sparsity: Percentage of missing ratings (0-1)
            random_seed: Random seed for reproducibility
            
        Returns:
            DataFrame with columns: user_id, course_id, rating
        """
        np.random.seed(random_seed)
        
        n_courses = len(self.df)
        n_ratings = int(n_users * n_courses * (1 - sparsity))
        
        ratings_list = []
        
        # Generate ratings based on course score and popularity
        for _ in range(n_ratings):
            user_id = np.random.randint(0, n_users)
            course_id = np.random.randint(0, n_courses)
            
            # Base rating from course score
            base_score = self.df.iloc[course_id]['score']
            
            # Add noise based on popularity (more popular = less variance)
            popularity = min(self.df.iloc[course_id]['ratings'] / 1000000, 1.0)
            noise_std = 0.5 * (1 - popularity) + 0.1
            
            # Generate rating with some variance
            rating = base_score + np.random.normal(0, noise_std)
            
            # Clip to valid range [1, 5]
            rating = np.clip(rating, 1.0, 5.0)
            
            ratings_list.append({
                'user_id': user_id,
                'course_id': course_id,
                'rating': round(rating, 2)
            })
        
        self.ratings_df = pd.DataFrame(ratings_list)
        
        # Remove duplicates (same user-course pair)
        self.ratings_df = self.ratings_df.drop_duplicates(
            subset=['user_id', 'course_id']
        )
        
        return self.ratings_df
    
    def get_course_metadata(self) -> pd.DataFrame:
        """Get course metadata for content-based filtering"""
        metadata = self.df[['course_id', 'title', 'developer', 
                           'contentRating', 'score', 'ratings']].copy()
        
        # Create description from available fields
        metadata['description'] = (
            metadata['title'].astype(str) + ' ' +
            metadata['developer'].astype(str) + ' ' +
            metadata['contentRating'].astype(str)
        )
        
        return metadata
    
    def get_user_item_matrix(self) -> pd.DataFrame:
        """Convert ratings to user-item matrix"""
        if self.ratings_df is None:
            raise ValueError("Ratings not generated. Call generate_synthetic_ratings() first.")
        
        matrix = self.ratings_df.pivot_table(
            index='user_id',
            columns='course_id',
            values='rating',
            fill_value=0
        )
        
        return matrix
    
    def prepare_surprise_data(self):
        """Prepare data in Surprise library format"""
        from surprise import Dataset
        from surprise.reader import Reader
        
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(
            self.ratings_df[['user_id', 'course_id', 'rating']],
            reader
        )
        
        return data

