"""
Script to show app structure and verify it works
"""
import os
import sys

print("=" * 70)
print("COURSE RECOMMENDATION SYSTEM - APP PREVIEW")
print("=" * 70)

print("\n📱 APP STRUCTURE:")
print("-" * 70)
print("""
┌─────────────────────────────────────────────────────────────┐
│  📚 Course Recommendation System                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SIDEBAR (Left):                                            │
│  ├─ ⚙️ Configuration                                        │
│  ├─ 📤 Upload CSV File                                      │
│  ├─ Model Parameters (sliders)                             │
│  ├─ 🚀 Train Models button                                  │
│  ├─ 📂 Load Models button                                   │
│  └─ 💾 Save Models button                                   │
│                                                             │
│  MAIN AREA (Tabs):                                          │
│  ├─ 📊 Data Overview                                        │
│  │   ├─ Dataset statistics (Total Courses, Avg Rating, etc)│
│  │   ├─ Sample data table                                   │
│  │   └─ Visualizations (charts)                             │
│  │                                                          │
│  ├─ 🎯 Recommendations                                      │
│  │   ├─ User ID selector                                    │
│  │   ├─ Number of recommendations slider                    │
│  │   ├─ Model type selector (Hybrid/CF/CB)                 │
│  │   └─ Recommendations table                               │
│  │                                                          │
│  ├─ 📈 Evaluation                                           │
│  │   ├─ RMSE metric                                         │
│  │   ├─ Precision@K metrics                                │
│  │   ├─ Recall@K metrics                                    │
│  │   └─ Evaluation charts                                   │
│  │                                                          │
│  ├─ 📥 Download Results                                     │
│  │   └─ Download recommendations as CSV                    │
│  │                                                          │
│  └─ ℹ️ About                                                │
│      └─ System documentation                                │
└─────────────────────────────────────────────────────────────┘
""")

print("\n🎨 THEME: Black (#1E1E1E) and Cream (#F5F5DC) with Gold accents")
print("\n📋 WORKFLOW:")
print("  1. Upload CSV file → Data Overview tab")
print("  2. Click 'Train Models' → Wait 2-5 minutes")
print("  3. Go to Recommendations tab → Select User ID")
print("  4. Get personalized course recommendations!")
print("  5. View evaluation metrics in Evaluation tab")
print("  6. Download results as CSV")

print("\n" + "=" * 70)
print("🚀 TO START THE APP:")
print("=" * 70)
print("\nRun this command in your terminal:")
print("  streamlit run app.py")
print("\nOr:")
print("  py -m streamlit run app.py")
print("\nThe app will open at: http://localhost:8501")
print("\n" + "=" * 70)

# Check if app.py exists
if os.path.exists("app.py"):
    print("\n✅ app.py found!")
    with open("app.py", "r", encoding="utf-8") as f:
        lines = len(f.readlines())
    print(f"   File size: {lines} lines of code")
else:
    print("\n❌ app.py not found!")

# Check dependencies
print("\n📦 CHECKING DEPENDENCIES:")
print("-" * 70)
deps = ["streamlit", "pandas", "numpy", "scikit-learn", "scikit-surprise"]
for dep in deps:
    try:
        __import__(dep.replace("-", "_"))
        print(f"  ✅ {dep}")
    except:
        print(f"  ❌ {dep} - Install with: pip install {dep}")

print("\n" + "=" * 70)
print("Ready to run! Execute: streamlit run app.py")
print("=" * 70)

