# Quick Start Guide

## Installation

1. **Install Python 3.8 or higher** (if not already installed)

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Running the Application

### Option 1: Use the Web Interface (Recommended)

1. **Start the Streamlit app**:
```bash
streamlit run app.py
```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Upload your dataset**:
   - Click "Upload CSV File" in the sidebar
   - Select `edtech (1).csv` (or your own CSV file)

4. **Train models**:
   - Go to "Data Overview" tab to see your data
   - Adjust parameters in sidebar (optional)
   - Click "🚀 Train Models" button
   - Wait for training to complete (~2-5 minutes)

5. **Get recommendations**:
   - Go to "🎯 Recommendations" tab
   - Select a User ID (0 to n_users-1)
   - Choose number of recommendations
   - Select model type (Hybrid recommended)
   - Click "Get Recommendations"

### Option 2: Train Models Offline First

1. **Train models using command line**:
```bash
python train_models.py
```

Or with custom parameters:
```bash
python train_models.py "edtech (1).csv" 1000 0.7
```

2. **Start the Streamlit app**:
```bash
streamlit run app.py
```

3. **Load pre-trained models**:
   - Click "📂 Load Models" in the sidebar
   - Models will be loaded from `models/` directory

## Example Usage

### Getting Recommendations

1. After training models, go to "Recommendations" tab
2. Enter User ID: `0`
3. Select Number of Recommendations: `10`
4. Choose Model: `Hybrid`
5. Click "Get Recommendations"

### Evaluating Models

1. Go to "📈 Evaluation" tab
2. Click "Calculate Evaluation Metrics"
3. View RMSE, Precision@K, and Recall@K metrics

### Downloading Results

1. Generate recommendations first
2. Go to "📥 Download Results" tab
3. Click "📥 Download as CSV"

## Troubleshooting

### Issue: "Module not found" error
**Solution**: Install dependencies: `pip install -r requirements.txt`

### Issue: "File not found" error
**Solution**: Make sure `edtech (1).csv` is in the same directory as `app.py`

### Issue: Training takes too long
**Solution**: Reduce `n_users` or `n_factors` in the sidebar

### Issue: No recommendations shown
**Solution**: 
- Make sure models are trained
- Check if user ID exists in the dataset
- Try a different user ID

### Issue: Memory error
**Solution**: 
- Reduce number of users
- Reduce `max_features` in content-based model
- Close other applications

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: ~500MB for models and dependencies
- **Browser**: Modern browser (Chrome, Firefox, Edge)

## Next Steps

- Read `README.md` for detailed documentation
- Read `PROJECT_REPORT.md` for technical details
- Experiment with different model parameters
- Try with your own dataset

## Support

For issues or questions, refer to:
- `README.md` - General documentation
- `PROJECT_REPORT.md` - Technical report
- Code comments in source files


