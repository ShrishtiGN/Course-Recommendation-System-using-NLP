# Course Recommendation System

A comprehensive course recommendation system that uses Collaborative Filtering, Content-Based Filtering, and Hybrid approaches to suggest personalized courses to users.

## Features

- ✅ **User-Item Collaborative Filtering** with Matrix Factorization (SVD)
- ✅ **Content-Based Filtering** using TF-IDF and Cosine Similarity
- ✅ **Hybrid Recommender** combining both methods
- ✅ **Top-N Recommendations** per user
- ✅ **CSV Upload** from the UI
- ✅ **Evaluation Dashboards** with RMSE, Precision@K, Recall@K
- ✅ **Model Saving/Loading** (Pickle)
- ✅ **Simple & Responsive UI** with Black and Cream theme

## Tech Stack

- **Python 3.8+**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations
- **Scikit-Surprise** - Collaborative Filtering (SVD)
- **Scikit-Learn** - TF-IDF and Content Similarity
- **Streamlit** - Web interface
- **Matplotlib/Seaborn** - Visualizations

## Installation

1. Clone or download this repository

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. The application will open in your browser at `http://localhost:8501`

### Using the System

1. **Upload Dataset**: 
   - Click on "Upload CSV File" in the sidebar
   - Upload your EdTech dataset CSV file

2. **Train Models**:
   - Adjust model parameters in the sidebar (optional)
   - Click "🚀 Train Models" button
   - Wait for training to complete (may take a few minutes)

3. **Get Recommendations**:
   - Go to the "🎯 Recommendations" tab
   - Select a User ID
   - Choose the number of recommendations
   - Select the model type (Hybrid, Collaborative Filtering, or Content-Based)
   - Click "Get Recommendations"

4. **Evaluate Models**:
   - Go to the "📈 Evaluation" tab
   - Click "Calculate Evaluation Metrics"
   - View RMSE, Precision@K, and Recall@K metrics

5. **Download Results**:
   - Go to the "📥 Download Results" tab
   - Download recommendations as CSV

6. **Save/Load Models**:
   - Use "💾 Save Models" to save trained models
   - Use "📂 Load Models" to load previously saved models

## Dataset Format

The CSV file should contain the following columns:
- `title`: Course/App name
- `score`: Rating score (1-5)
- `ratings`: Number of ratings
- `reviews`: Number of reviews
- `developer`: Developer/Publisher name
- `contentRating`: Content rating
- Other metadata columns (optional)

## Project Structure

```
.
├── app.py                          # Main Streamlit application
├── data_preprocessing.py           # Data loading and preprocessing
├── collaborative_filtering.py     # Collaborative Filtering model
├── content_based_filtering.py     # Content-Based Filtering model
├── hybrid_recommender.py          # Hybrid Recommender
├── evaluation_metrics.py          # Evaluation metrics
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── models/                        # Saved models (created after training)
└── edtech (1).csv                 # Dataset file
```

## Model Details

### Collaborative Filtering (CF)
- Uses **Singular Value Decomposition (SVD)** for matrix factorization
- Finds latent factors in user-item interactions
- Parameters: `n_factors`, `n_epochs`, `lr_all`, `reg_all`

### Content-Based Filtering
- Uses **TF-IDF** vectorization to represent course content
- Calculates **Cosine Similarity** between courses
- Recommends courses similar to user's previously rated courses

### Hybrid Recommender
- Combines CF and Content-Based approaches
- Weighted combination: `hybrid_score = α × CF_score + (1-α) × CB_score`
- Default weights: CF=0.6, CB=0.4 (adjustable)

## Evaluation Metrics

- **RMSE (Root Mean Squared Error)**: Measures prediction accuracy
- **Precision@K**: Fraction of recommended items that are relevant
- **Recall@K**: Fraction of relevant items that are recommended

## Notes

- The system generates synthetic user ratings if the dataset doesn't contain user-item interactions
- Model training may take several minutes depending on dataset size
- Saved models are stored in the `models/` directory
- The UI uses a Black and Cream color theme for better visibility

## Troubleshooting

1. **Import Errors**: Make sure all dependencies are installed (`pip install -r requirements.txt`)

2. **Model Training Fails**: 
   - Check if the CSV file is properly formatted
   - Ensure sufficient memory for large datasets
   - Try reducing the number of users or factors

3. **No Recommendations**: 
   - Make sure models are trained or loaded
   - Check if the user ID exists in the dataset
   - Verify that the dataset has sufficient data

## License

This project is provided as-is for educational purposes.

## Contact

For questions or issues, please refer to the project documentation.


