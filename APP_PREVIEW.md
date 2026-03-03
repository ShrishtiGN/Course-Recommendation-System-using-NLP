# 📱 Course Recommendation System - App Preview

## 🎨 Visual Interface Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  📚 Course Recommendation System                    [📊] [🎯] [📈] [📥] [ℹ️] │
├──────────────┬──────────────────────────────────────────────────────────────┤
│              │                                                              │
│  SIDEBAR     │                    MAIN CONTENT AREA                        │
│              │                                                              │
│  ⚙️ Config   │  ┌────────────────────────────────────────────────────┐    │
│              │  │                                                    │    │
│  📤 Upload   │  │  Tab Content (changes based on selected tab)       │    │
│  CSV File    │  │                                                    │    │
│              │  │                                                    │    │
│  ─────────   │  │                                                    │    │
│              │  │                                                    │    │
│  Parameters: │  │                                                    │    │
│  • Users     │  │                                                    │    │
│  • Sparsity  │  │                                                    │    │
│  • Factors   │  │                                                    │    │
│  • Epochs    │  │                                                    │    │
│  • CF Weight │  │                                                    │    │
│              │  │                                                    │    │
│  ─────────   │  │                                                    │    │
│              │  │                                                    │    │
│  [🚀 Train]  │  │                                                    │    │
│  [📂 Load]   │  │                                                    │    │
│  [💾 Save]   │  │                                                    │    │
│              │  └────────────────────────────────────────────────────┘    │
└──────────────┴──────────────────────────────────────────────────────────────┘
```

## 🎨 Color Scheme (Black & Cream Theme)

- **Background**: Dark Black (#1E1E1E)
- **Sidebar**: Dark Gray (#2D2D2D)
- **Text**: Cream (#F5F5DC)
- **Buttons**: Gold (#D4AF37)
- **Accents**: Gold (#D4AF37)

## 📑 Tab Details

### 1. 📊 Data Overview Tab

**What you'll see:**
```
┌─────────────────────────────────────────────────────────┐
│  Dataset Overview                                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [Total Courses: 81]  [Avg Rating: 4.2]  [Ratings: ...] │
│                                                          │
│  Sample Data:                                            │
│  ┌──────────────────────────────────────────────────┐   │
│  │ Title          │ Developer │ Score │ Ratings    │   │
│  ├────────────────┼───────────┼───────┼────────────┤   │
│  │ BYJU'S App     │ BYJU'S    │ 4.12  │ 1,745,108  │   │
│  │ Duolingo       │ Duolingo  │ 4.57  │ 12,512,116 │   │
│  │ ...            │ ...       │ ...   │ ...        │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
│  [Rating Distribution Chart]  [Top 10 Courses Chart]    │
└─────────────────────────────────────────────────────────┘
```

### 2. 🎯 Recommendations Tab

**What you'll see:**
```
┌─────────────────────────────────────────────────────────┐
│  Get Recommendations                                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ✅ Models are ready for recommendations!                │
│                                                          │
│  Get Personalized Recommendations:                       │
│                                                          │
│  User ID: [0        ]  Recommendations: [10 ▼]         │
│                                                          │
│  Model: [Hybrid ▼]                                      │
│                                                          │
│  [Get Recommendations]                                   │
│                                                          │
│  ────────────────────────────────────────────────────   │
│                                                          │
│  Top 10 Recommendations:                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │ Title              │ Developer │ Score            │   │
│  ├────────────────────┼───────────┼───────────────────┤   │
│  │ Course Name 1      │ Dev 1     │ 4.85             │   │
│  │ Course Name 2     │ Dev 2     │ 4.72             │   │
│  │ ...               │ ...       │ ...              │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### 3. 📈 Evaluation Tab

**What you'll see:**
```
┌─────────────────────────────────────────────────────────┐
│  Model Evaluation                                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [Calculate Evaluation Metrics]                          │
│                                                          │
│  ────────────────────────────────────────────────────   │
│                                                          │
│  [RMSE: 0.9234]  [Precision@5: 0.45]  [Recall@5: 0.32] │
│                                                          │
│  [Precision@K Chart]  [Recall@K Chart]                  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 4. 📥 Download Results Tab

**What you'll see:**
```
┌─────────────────────────────────────────────────────────┐
│  Download Results                                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Last Generated Recommendations:                         │
│                                                          │
│  [Recommendations Table]                                │
│                                                          │
│  [📥 Download as CSV]                                    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 5. ℹ️ About Tab

**What you'll see:**
```
┌─────────────────────────────────────────────────────────┐
│  About the System                                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ### Course Recommendation System                        │
│                                                          │
│  This system implements three recommendation approaches: │
│                                                          │
│  1. Collaborative Filtering (CF)                        │
│  2. Content-Based Filtering                              │
│  3. Hybrid Model                                         │
│                                                          │
│  Features:                                               │
│  ✅ User-Item Collaborative Filtering with SVD          │
│  ✅ Content-Based Similarity using TF-IDF               │
│  ✅ Hybrid Recommender combining both methods           │
│  ✅ Top-N Recommendations                                │
│  ✅ CSV Upload functionality                             │
│  ✅ Evaluation Metrics (RMSE, Precision@K, Recall@K)   │
│  ✅ Model Saving/Loading                                 │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Step-by-Step Usage

### Step 1: Upload Data
1. Click "Upload CSV File" in sidebar
2. Select `edtech (1).csv`
3. Data loads automatically

### Step 2: View Data
1. Go to "📊 Data Overview" tab
2. See statistics and charts
3. Verify data loaded correctly

### Step 3: Train Models
1. Adjust parameters (optional)
2. Click "🚀 Train Models"
3. Wait 2-5 minutes
4. See success message: "✅ Models trained successfully!"

### Step 4: Get Recommendations
1. Go to "🎯 Recommendations" tab
2. Select User ID (0 to n_users-1)
3. Choose number of recommendations (5-50)
4. Select model type (Hybrid recommended)
5. Click "Get Recommendations"
6. See personalized course list!

### Step 5: Evaluate
1. Go to "📈 Evaluation" tab
2. Click "Calculate Evaluation Metrics"
3. View RMSE, Precision@K, Recall@K

### Step 6: Download
1. Go to "📥 Download Results" tab
2. Click "📥 Download as CSV"
3. Save recommendations file

## 🎯 What Makes It Special

1. **Beautiful UI**: Black & Cream theme with gold accents
2. **Interactive**: Sliders, dropdowns, file upload
3. **Real-time**: See results instantly
4. **Comprehensive**: All features in one place
5. **Professional**: Clean, modern design

## 📸 Expected Screenshots

When you run the app, you should see:
- Dark theme interface
- Gold-colored buttons
- Cream-colored text
- Professional layout
- Interactive widgets
- Real-time updates

---

**To see it in action, run:**
```bash
streamlit run app.py
```

Then open: **http://localhost:8501**

