"""
Streamlit Web Application for Course Recommendation System
Black and Cream Theme
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import DataPreprocessor
from collaborative_filtering import CollaborativeFiltering
from content_based_filtering import ContentBasedFiltering
from hybrid_recommender import HybridRecommender
from evaluation_metrics import EvaluationMetrics

# Page configuration
st.set_page_config(
    page_title="Course Recommendation System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Black and Cream theme
st.markdown("""
    <style>
    .main {
        background-color: #1E1E1E;
        color: #F5F5DC;
    }
    .stApp {
        background-color: #1E1E1E;
    }
    .stSidebar {
        background-color: #2D2D2D;
    }
    h1, h2, h3 {
        color: #F5F5DC;
    }
    .stButton>button {
        background-color: #D4AF37;
        color: #1E1E1E;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #C9A227;
    }
    .metric-card {
        background-color: #2D2D2D;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #D4AF37;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'models_trained' not in st.session_state:
    st.session_state.models_trained = False
if 'cf_model' not in st.session_state:
    st.session_state.cf_model = None
if 'cb_model' not in st.session_state:
    st.session_state.cb_model = None
if 'hybrid_model' not in st.session_state:
    st.session_state.hybrid_model = None
if 'courses_df' not in st.session_state:
    st.session_state.courses_df = None
if 'ratings_df' not in st.session_state:
    st.session_state.ratings_df = None
if 'preprocessor' not in st.session_state:
    st.session_state.preprocessor = None

def main():
    """Main application function"""
    
    st.title("Course Recommendation System")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("Configuration")
        
        # File upload
        uploaded_file = st.file_uploader(
            "Upload CSV File",
            type=['csv'],
            help="Upload your EdTech dataset CSV file"
        )
        
        # Model parameters
        st.subheader("Model Parameters")
        n_users = st.slider("Number of Users", 100, 2000, 1000, 100)
        sparsity = st.slider("Data Sparsity", 0.3, 0.9, 0.7, 0.1)
        n_factors = st.slider("CF: Number of Factors", 10, 100, 50, 10)
        n_epochs = st.slider("CF: Number of Epochs", 10, 50, 20, 5)
        cf_weight = st.slider("Hybrid: CF Weight", 0.0, 1.0, 0.6, 0.1)
        cb_weight = 1.0 - cf_weight
        st.write(f"Content-Based Weight: {cb_weight:.1f}")
        
        # Action buttons
        st.markdown("---")
        train_models = st.button("Train Models", type="primary", use_container_width=True)
        load_models = st.button("Load Models", use_container_width=True)
        save_models = st.button("Save Models", use_container_width=True)
    
    # Main content area
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Data Overview", 
        "Recommendations", 
        "Evaluation", 
        "Download Results",
        "About"
    ])
    
    # Tab 1: Data Overview
    with tab1:
        st.header("Dataset Overview")
        
        if uploaded_file is not None:
            # Load and process data
            file_key = uploaded_file.name if hasattr(uploaded_file, 'name') else str(uploaded_file)
            if st.session_state.preprocessor is None or not hasattr(st.session_state.preprocessor, 'file_key') or st.session_state.preprocessor.file_key != file_key:
                with st.spinner("Loading data..."):
                    # Save uploaded file temporarily
                    import tempfile
                    import os
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv', mode='wb') as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_path = tmp_file.name
                    
                    preprocessor = DataPreprocessor(tmp_path)
                    df = preprocessor.load_data()
                    preprocessor.file_key = file_key  # Store file identifier
                    st.session_state.preprocessor = preprocessor
                    st.session_state.courses_df = preprocessor.get_course_metadata()
                    # Clean up temp file after loading
                    try:
                        os.unlink(tmp_path)
                    except:
                        pass
            else:
                df = st.session_state.preprocessor.df
                st.session_state.courses_df = st.session_state.preprocessor.get_course_metadata()
            
            # Display dataset info
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Courses", len(df))
            with col2:
                st.metric("Average Rating", f"{df['score'].mean():.2f}")
            with col3:
                st.metric("Total Ratings", f"{df['ratings'].sum():,.0f}")
            with col4:
                st.metric("Developers", df['developer'].nunique())
            
            # Display sample data
            st.subheader("Sample Data")
            st.dataframe(df[['title', 'developer', 'score', 'ratings', 'reviews']].head(10))
            
            # Visualizations
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Rating Distribution")
                fig, ax = plt.subplots(figsize=(8, 5))
                ax.hist(df['score'].dropna(), bins=20, color='#D4AF37', edgecolor='black')
                ax.set_xlabel('Rating', color='#F5F5DC')
                ax.set_ylabel('Frequency', color='#F5F5DC')
                ax.set_facecolor('#2D2D2D')
                fig.patch.set_facecolor('#1E1E1E')
                ax.tick_params(colors='#F5F5DC')
                st.pyplot(fig)
            
            with col2:
                st.subheader("Top 10 Courses by Ratings")
                top_courses = df.nlargest(10, 'ratings')[['title', 'ratings', 'score']]
                fig, ax = plt.subplots(figsize=(8, 5))
                ax.barh(range(len(top_courses)), top_courses['ratings'], color='#D4AF37')
                ax.set_yticks(range(len(top_courses)))
                ax.set_yticklabels([title[:30] + '...' if len(title) > 30 else title 
                                   for title in top_courses['title']], color='#F5F5DC')
                ax.set_xlabel('Number of Ratings', color='#F5F5DC')
                ax.set_facecolor('#2D2D2D')
                fig.patch.set_facecolor('#1E1E1E')
                ax.tick_params(colors='#F5F5DC')
                plt.tight_layout()
                st.pyplot(fig)
        else:
            st.info("Please upload a CSV file to get started")
    
    # Tab 2: Recommendations
    with tab2:
        st.header("Get Recommendations")
        
        if train_models:
            if uploaded_file is None and st.session_state.preprocessor is None:
                st.error("Please upload a CSV file first")
            elif st.session_state.preprocessor is None:
                st.error("Please load data in the Data Overview tab first")
            else:
                with st.spinner("Training models... This may take a few minutes."):
                    try:
                        # Generate synthetic ratings
                        if st.session_state.ratings_df is None:
                            ratings_df = st.session_state.preprocessor.generate_synthetic_ratings(
                                n_users=n_users, sparsity=sparsity
                            )
                            st.session_state.ratings_df = ratings_df
                        else:
                            ratings_df = st.session_state.ratings_df
                        
                        # Train Collaborative Filtering
                        cf_model = CollaborativeFiltering(
                            n_factors=n_factors, n_epochs=n_epochs
                        )
                        cf_model.train(ratings_df)
                        st.session_state.cf_model = cf_model
                        
                        # Train Content-Based
                        cb_model = ContentBasedFiltering()
                        cb_model.train(st.session_state.courses_df)
                        st.session_state.cb_model = cb_model
                        
                        # Create Hybrid Model
                        hybrid_model = HybridRecommender(
                            cf_model, cb_model, cf_weight, cb_weight
                        )
                        st.session_state.hybrid_model = hybrid_model
                        
                        st.session_state.models_trained = True
                        st.success("Models trained successfully!")
                    
                    except Exception as e:
                        st.error(f"Error training models: {str(e)}")
        
        if load_models:
            try:
                cf_model = CollaborativeFiltering()
                cf_model.load_model('models/cf_model.pkl')
                st.session_state.cf_model = cf_model
                
                cb_model = ContentBasedFiltering()
                cb_model.load_model('models/cb_model.pkl')
                st.session_state.cb_model = cb_model
                
                hybrid_model = HybridRecommender(cf_model, cb_model, cf_weight, cb_weight)
                st.session_state.hybrid_model = hybrid_model
                
                if st.session_state.courses_df is None:
                    st.warning("Please upload CSV file first to load course metadata")
                else:
                    st.session_state.models_trained = True
                    st.success("Models loaded successfully!")
            except Exception as e:
                st.error(f"Error loading models: {str(e)}")
        
        if save_models and st.session_state.models_trained:
            try:
                os.makedirs('models', exist_ok=True)
                st.session_state.cf_model.save_model('models/cf_model.pkl')
                st.session_state.cb_model.save_model('models/cb_model.pkl')
                st.success("Models saved successfully!")
            except Exception as e:
                st.error(f"Error saving models: {str(e)}")
        
        if st.session_state.models_trained:
            st.success("Models are ready for recommendations!")
            
            # Recommendation interface
            st.subheader("Get Personalized Recommendations")
            
            col1, col2 = st.columns(2)
            
            with col1:
                user_id = st.number_input(
                    "User ID",
                    min_value=0,
                    max_value=n_users-1 if st.session_state.ratings_df is not None else 1000,
                    value=0,
                    step=1
                )
                n_recommendations = st.slider(
                    "Number of Recommendations",
                    min_value=5,
                    max_value=50,
                    value=10,
                    step=5
                )
            
            with col2:
                model_type = st.selectbox(
                    "Recommendation Model",
                    ["Hybrid", "Collaborative Filtering", "Content-Based"]
                )
            
            if st.button("Get Recommendations", type="primary"):
                try:
                    if model_type == "Collaborative Filtering":
                        recommendations = st.session_state.cf_model.get_top_n_recommendations(
                            user_id, n=n_recommendations,
                            courses_df=st.session_state.courses_df
                        )
                        recs_df = pd.DataFrame(recommendations)
                        if 'predicted_rating' in recs_df.columns:
                            recs_df = recs_df.rename(columns={'predicted_rating': 'score'})
                    
                    elif model_type == "Content-Based":
                        # Get user's rated courses
                        user_ratings = st.session_state.ratings_df[
                            st.session_state.ratings_df['user_id'] == user_id
                        ]
                        if len(user_ratings) > 0:
                            rated_courses = user_ratings['course_id'].tolist()
                            ratings = user_ratings['rating'].tolist()
                            recommendations = st.session_state.cb_model.get_user_recommendations(
                                rated_courses, ratings, n=n_recommendations
                            )
                            recs_df = pd.DataFrame(recommendations)
                            if 'similarity_score' in recs_df.columns:
                                recs_df = recs_df.rename(columns={'similarity_score': 'score'})
                        else:
                            st.warning("User has no ratings. Using popular courses.")
                            recommendations = []
                            recs_df = pd.DataFrame()
                    
                    else:  # Hybrid
                        user_ratings = st.session_state.ratings_df[
                            st.session_state.ratings_df['user_id'] == user_id
                        ]
                        rated_courses = user_ratings['course_id'].tolist() if len(user_ratings) > 0 else []
                        ratings = user_ratings['rating'].tolist() if len(user_ratings) > 0 else []
                        
                        recommendations = st.session_state.hybrid_model.get_recommendations(
                            user_id, n=n_recommendations,
                            courses_df=st.session_state.courses_df,
                            user_rated_courses=rated_courses,
                            user_ratings=ratings
                        )
                        recs_df = pd.DataFrame(recommendations)
                        if 'hybrid_score' in recs_df.columns:
                            recs_df = recs_df.rename(columns={'hybrid_score': 'score'})
                    
                    if len(recs_df) > 0:
                        st.subheader(f"Top {len(recs_df)} Recommendations")
                        st.dataframe(recs_df[['title', 'developer', 'score']], use_container_width=True)
                        
                        # Store for download
                        st.session_state.last_recommendations = recs_df
                    else:
                        st.warning("No recommendations available.")
                        
                except Exception as e:
                    st.error(f"Error getting recommendations: {str(e)}")
        else:
            st.info("Please train or load models first")
    
    # Tab 3: Evaluation
    with tab3:
        st.header("Model Evaluation")
        
        if st.session_state.models_trained and st.session_state.ratings_df is not None:
            # Calculate metrics
            if st.button("Calculate Evaluation Metrics"):
                with st.spinner("Calculating metrics..."):
                    try:
                        # RMSE for CF
                        cf_metrics = st.session_state.cf_model.evaluate()
                        
                        # Display metrics
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("RMSE (CF)", f"{cf_metrics['RMSE']:.4f}")
                        
                        # Generate recommendations for evaluation
                        test_users = st.session_state.ratings_df['user_id'].unique()[:100]
                        all_recommendations = []
                        
                        for user_id in test_users:
                            try:
                                recs = st.session_state.cf_model.get_top_n_recommendations(
                                    user_id, n=20, courses_df=st.session_state.courses_df
                                )
                                for rec in recs:
                                    all_recommendations.append({
                                        'user_id': user_id,
                                        'course_id': rec['course_id']
                                    })
                            except:
                                continue
                        
                        if all_recommendations:
                            recs_df = pd.DataFrame(all_recommendations)
                            
                            # Split test set
                            test_size = int(len(st.session_state.ratings_df) * 0.2)
                            test_ratings = st.session_state.ratings_df.tail(test_size)
                            
                            # Calculate Precision@K and Recall@K
                            evaluator = EvaluationMetrics()
                            eval_results = evaluator.evaluate_recommendations(
                                recs_df, test_ratings, k_values=[5, 10, 20]
                            )
                            
                            # Display metrics
                            st.subheader("Precision and Recall Metrics")
                            metrics_cols = st.columns(3)
                            
                            for i, (metric, value) in enumerate(eval_results.items()):
                                with metrics_cols[i % 3]:
                                    st.metric(metric, f"{value:.4f}")
                            
                            # Visualization
                            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
                            
                            # Precision@K
                            precision_vals = [eval_results[f'Precision@{k}'] for k in [5, 10, 20]]
                            ax1.bar(['P@5', 'P@10', 'P@20'], precision_vals, color='#D4AF37')
                            ax1.set_ylabel('Precision', color='#F5F5DC')
                            ax1.set_title('Precision@K', color='#F5F5DC')
                            ax1.set_facecolor('#2D2D2D')
                            ax1.tick_params(colors='#F5F5DC')
                            
                            # Recall@K
                            recall_vals = [eval_results[f'Recall@{k}'] for k in [5, 10, 20]]
                            ax2.bar(['R@5', 'R@10', 'R@20'], recall_vals, color='#D4AF37')
                            ax2.set_ylabel('Recall', color='#F5F5DC')
                            ax2.set_title('Recall@K', color='#F5F5DC')
                            ax2.set_facecolor('#2D2D2D')
                            ax2.tick_params(colors='#F5F5DC')
                            
                            fig.patch.set_facecolor('#1E1E1E')
                            plt.tight_layout()
                            st.pyplot(fig)
                            
                    except Exception as e:
                        st.error(f"Error calculating metrics: {str(e)}")
        else:
            st.info("Please train models first to evaluate")
    
    # Tab 4: Download Results
    with tab4:
        st.header("Download Results")
        
        if 'last_recommendations' in st.session_state:
            st.subheader("Last Generated Recommendations")
            st.dataframe(st.session_state.last_recommendations)
            
            # Convert to CSV
            csv = st.session_state.last_recommendations.to_csv(index=False)
            st.download_button(
                label="Download as CSV",
                data=csv,
                file_name="recommendations.csv",
                mime="text/csv"
            )
        else:
            st.info("Generate recommendations first to download results")
    
    # Tab 5: About
    with tab5:
        st.header("About the System")
        st.markdown("""
        ### Course Recommendation System
        
        This system implements three recommendation approaches:
        
        1. **Collaborative Filtering (CF)**: Uses Matrix Factorization (SVD) to find similar users
        2. **Content-Based Filtering**: Uses TF-IDF and Cosine Similarity to find similar courses
        3. **Hybrid Model**: Combines both CF and Content-Based approaches
        
        ### Features:
        - User-Item Collaborative Filtering with SVD
        - Content-Based Similarity using TF-IDF
        - Hybrid Recommender combining both methods
        - Top-N Recommendations
        - CSV Upload functionality
        - Evaluation Metrics (RMSE, Precision@K, Recall@K)
        - Model Saving/Loading
        
        ### Tech Stack:
        - Python, Pandas, NumPy
        - Scikit-Surprise (Collaborative Filtering)
        - Scikit-Learn (TF-IDF)
        - Streamlit (Web Interface)
        - Matplotlib/Seaborn (Visualizations)
        """)

if __name__ == "__main__":
    main()

