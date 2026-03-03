"""
Evaluation Metrics Module
Implements RMSE, Precision@K, and Recall@K metrics
"""

import numpy as np
import pandas as pd
from typing import List, Dict


class EvaluationMetrics:
    """Evaluation metrics for recommendation systems"""
    
    @staticmethod
    def calculate_rmse(predictions: List[float], actuals: List[float]) -> float:
        """
        Calculate Root Mean Squared Error
        
        Args:
            predictions: List of predicted ratings
            actuals: List of actual ratings
            
        Returns:
            RMSE value
        """
        predictions = np.array(predictions)
        actuals = np.array(actuals)
        mse = np.mean((predictions - actuals) ** 2)
        rmse = np.sqrt(mse)
        return rmse
    
    @staticmethod
    def calculate_precision_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
        """
        Calculate Precision@K
        
        Args:
            recommended: List of recommended item IDs
            relevant: List of relevant item IDs (ground truth)
            k: Number of top recommendations to consider
            
        Returns:
            Precision@K value
        """
        if k == 0 or len(recommended) == 0:
            return 0.0
        
        top_k_recommended = recommended[:k]
        relevant_set = set(relevant)
        
        # Count how many recommended items are relevant
        hits = sum(1 for item in top_k_recommended if item in relevant_set)
        
        precision = hits / min(k, len(top_k_recommended))
        return precision
    
    @staticmethod
    def calculate_recall_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
        """
        Calculate Recall@K
        
        Args:
            recommended: List of recommended item IDs
            relevant: List of relevant item IDs (ground truth)
            k: Number of top recommendations to consider
            
        Returns:
            Recall@K value
        """
        if len(relevant) == 0:
            return 0.0
        
        top_k_recommended = recommended[:k]
        relevant_set = set(relevant)
        
        # Count how many relevant items are in recommendations
        hits = sum(1 for item in top_k_recommended if item in relevant_set)
        
        recall = hits / len(relevant_set)
        return recall
    
    @staticmethod
    def evaluate_recommendations(recommendations_df: pd.DataFrame,
                                test_ratings_df: pd.DataFrame,
                                k_values: List[int] = [5, 10, 20]) -> Dict:
        """
        Evaluate recommendations using Precision@K and Recall@K
        
        Args:
            recommendations_df: DataFrame with columns: user_id, course_id
            test_ratings_df: DataFrame with test ratings: user_id, course_id, rating
            k_values: List of K values to evaluate
            
        Returns:
            Dictionary with evaluation metrics
        """
        results = {}
        
        # Group test ratings by user
        test_by_user = test_ratings_df.groupby('user_id')
        
        # Group recommendations by user
        recs_by_user = recommendations_df.groupby('user_id')
        
        for k in k_values:
            precisions = []
            recalls = []
            
            for user_id in test_by_user.groups.keys():
                if user_id not in recs_by_user.groups:
                    continue
                
                # Get relevant items (items with rating >= 4 in test set)
                user_test = test_by_user.get_group(user_id)
                relevant_items = user_test[user_test['rating'] >= 4]['course_id'].tolist()
                
                # Get recommended items
                user_recs = recs_by_user.get_group(user_id)
                recommended_items = user_recs['course_id'].tolist()
                
                # Calculate metrics
                precision = EvaluationMetrics.calculate_precision_at_k(
                    recommended_items, relevant_items, k
                )
                recall = EvaluationMetrics.calculate_recall_at_k(
                    recommended_items, relevant_items, k
                )
                
                precisions.append(precision)
                recalls.append(recall)
            
            results[f'Precision@{k}'] = np.mean(precisions) if precisions else 0.0
            results[f'Recall@{k}'] = np.mean(recalls) if recalls else 0.0
        
        return results


