"""
Hybrid Recommender Module
Combines Collaborative Filtering and Content-Based Filtering
"""

import numpy as np
import pandas as pd
from collaborative_filtering import CollaborativeFiltering
from content_based_filtering import ContentBasedFiltering


class HybridRecommender:
    """Hybrid Recommender combining CF and Content-Based methods"""
    
    def __init__(self, cf_model: CollaborativeFiltering, 
                 cb_model: ContentBasedFiltering,
                 cf_weight: float = 0.6, cb_weight: float = 0.4):
        """
        Initialize the hybrid recommender
        
        Args:
            cf_model: Trained Collaborative Filtering model
            cb_model: Trained Content-Based Filtering model
            cf_weight: Weight for collaborative filtering (0-1)
            cb_weight: Weight for content-based filtering (0-1)
        """
        self.cf_model = cf_model
        self.cb_model = cb_model
        self.cf_weight = cf_weight
        self.cb_weight = cb_weight
        
        # Normalize weights
        total_weight = cf_weight + cb_weight
        self.cf_weight = cf_weight / total_weight
        self.cb_weight = cb_weight / total_weight
    
    def get_recommendations(self, user_id: int, n: int = 10,
                           courses_df: pd.DataFrame = None,
                           user_rated_courses: list = None,
                           user_ratings: list = None) -> list:
        """
        Get hybrid recommendations for a user
        
        Args:
            user_id: User ID
            n: Number of recommendations
            courses_df: DataFrame with course information
            user_rated_courses: List of course IDs user has rated
            user_ratings: List of ratings
            
        Returns:
            List of recommended courses with hybrid scores
        """
        # Get CF recommendations
        try:
            cf_recs = self.cf_model.get_top_n_recommendations(
                user_id, n=n*2, courses_df=courses_df
            )
        except Exception as e:
            # Fallback if CF fails
            cf_recs = []
        
        # Get CB recommendations
        if user_rated_courses and user_ratings:
            cb_recs = self.cb_model.get_user_recommendations(
                user_rated_courses, user_ratings, n=n*2
            )
        else:
            # Fallback: use most popular courses
            cb_recs = []
        
        # Combine recommendations
        recommendations_dict = {}
        
        # Add CF recommendations
        for rec in cf_recs:
            course_id = rec['course_id']
            if course_id not in recommendations_dict:
                recommendations_dict[course_id] = {
                    'course_id': course_id,
                    'cf_score': 0,
                    'cb_score': 0,
                    'hybrid_score': 0
                }
                if 'title' in rec:
                    recommendations_dict[course_id]['title'] = rec['title']
                if 'developer' in rec:
                    recommendations_dict[course_id]['developer'] = rec['developer']
            
            # Normalize CF score (rating 1-5 -> 0-1)
            cf_score = (rec['predicted_rating'] - 1) / 4.0
            recommendations_dict[course_id]['cf_score'] = cf_score
        
        # Add CB recommendations
        for rec in cb_recs:
            course_id = rec['course_id']
            if course_id not in recommendations_dict:
                recommendations_dict[course_id] = {
                    'course_id': course_id,
                    'cf_score': 0,
                    'cb_score': 0,
                    'hybrid_score': 0
                }
                if 'title' in rec:
                    recommendations_dict[course_id]['title'] = rec['title']
                if 'developer' in rec:
                    recommendations_dict[course_id]['developer'] = rec['developer']
            
            recommendations_dict[course_id]['cb_score'] = rec['similarity_score']
        
        # Calculate hybrid scores
        for course_id in recommendations_dict:
            rec = recommendations_dict[course_id]
            rec['hybrid_score'] = (
                self.cf_weight * rec['cf_score'] +
                self.cb_weight * rec['cb_score']
            )
        
        # Sort by hybrid score and return top N
        recommendations = list(recommendations_dict.values())
        recommendations.sort(key=lambda x: x['hybrid_score'], reverse=True)
        
        # Format output
        formatted_recs = []
        for rec in recommendations[:n]:
            formatted_recs.append({
                'course_id': rec['course_id'],
                'hybrid_score': round(rec['hybrid_score'], 4),
                'cf_score': round(rec['cf_score'], 4),
                'cb_score': round(rec['cb_score'], 4),
                'title': rec.get('title', 'Unknown'),
                'developer': rec.get('developer', 'Unknown')
            })
        
        return formatted_recs

