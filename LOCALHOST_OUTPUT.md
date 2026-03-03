# What You'll See When Running the App

## Command to Run:
```bash
streamlit run app.py
```

## Expected Terminal Output:

```
Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501

  For better performance, install watchdogs:
    pip install watchdog
```

## What Happens Next:

1. **Browser Opens Automatically**: Streamlit will try to open your default browser
2. **URL**: The app will be available at `http://localhost:8501`
3. **Server Running**: The terminal will show the server is running
4. **To Stop**: Press `Ctrl+C` in the terminal

## If Browser Doesn't Open:

1. **Manually open**: Copy `http://localhost:8501` and paste in your browser
2. **Check port**: If 8501 is busy, Streamlit will use 8502, 8503, etc.
3. **Look at terminal**: It will show the exact URL to use

## What You'll See in Browser:

### Initial Screen:
- **Title**: "Course Recommendation System"
- **Sidebar** (left): Configuration panel with file upload
- **Main Area**: "Data Overview" tab (default)
- **Theme**: Black background with cream text

### After Uploading CSV:
- Dataset statistics appear
- Sample data table
- Charts showing rating distribution

### After Training Models:
- Success message: "Models trained successfully!"
- Can now get recommendations

## Troubleshooting:

### If you see "Python not found":
```bash
# Try these alternatives:
py -m streamlit run app.py
python3 -m streamlit run app.py
```

### If you see "streamlit not found":
```bash
pip install streamlit
# or
pip install -r requirements.txt
```

### If port is already in use:
```bash
streamlit run app.py --server.port 8502
```

## Server Status Indicators:

- **Running**: Terminal shows "You can now view..."
- **Error**: Terminal shows error message
- **Stopped**: Terminal returns to command prompt

---

**To see this in action, run: `streamlit run app.py`**

