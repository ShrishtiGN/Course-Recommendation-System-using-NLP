# How to Run the Application

## Quick Start

### Method 1: Using Python directly
```bash
streamlit run app.py
```

### Method 2: Using the start script
```bash
python start_app.py
```

### Method 3: Using Windows batch file
Double-click `run_app.bat` or run:
```bash
run_app.bat
```

### Method 4: Using PowerShell
```bash
.\run_app.ps1
```

## If localhost doesn't open automatically:

1. **Check the terminal output** - Streamlit will show the URL
2. **Manually open**: `http://localhost:8501` in your browser
3. **If port 8501 is busy**, Streamlit will use the next available port (8502, 8503, etc.)

## Common Issues:

### Issue: "Python not found"
**Solution**: 
- Use `py` instead of `python`: `py -m streamlit run app.py`
- Or install Python from python.org

### Issue: "Streamlit not found"
**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Port already in use
**Solution**: 
- Close other Streamlit apps
- Or use: `streamlit run app.py --server.port 8502`

## What to expect:

1. Terminal will show: "You can now view your Streamlit app in your browser"
2. Browser should open automatically
3. If not, copy the URL from terminal and paste in browser

