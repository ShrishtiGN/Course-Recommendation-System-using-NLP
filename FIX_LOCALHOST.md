# Fix: Localhost Not Running

## Quick Fixes

### Issue 1: Python Not Found
**Symptoms:** "Python was not found" error

**Solutions:**
```bash
# Try these commands in order:
py -m streamlit run app.py
python3 -m streamlit run app.py
python -m streamlit run app.py

# If none work, install Python:
# 1. Go to https://www.python.org/downloads/
# 2. Download and install Python
# 3. Make sure to check "Add Python to PATH" during installation
```

### Issue 2: Streamlit Not Installed
**Symptoms:** "streamlit is not recognized" or "No module named streamlit"

**Solution:**
```bash
pip install streamlit
# OR install all dependencies:
pip install -r requirements.txt
```

### Issue 3: Port Already in Use
**Symptoms:** "Address already in use" or port 8501 is busy

**Solutions:**
```bash
# Use a different port:
streamlit run app.py --server.port 8502

# OR close other Streamlit apps first
```

### Issue 4: Import Errors
**Symptoms:** ModuleNotFoundError when starting

**Solution:**
```bash
# Install all required packages:
pip install streamlit pandas numpy scikit-learn scikit-surprise matplotlib seaborn

# OR:
pip install -r requirements.txt
```

## Step-by-Step Troubleshooting

### Step 1: Run Diagnostic
```bash
python diagnose.py
# OR
py diagnose.py
```

This will tell you exactly what's missing.

### Step 2: Install Missing Dependencies
Based on diagnostic output, install what's needed:
```bash
pip install -r requirements.txt
```

### Step 3: Verify Installation
```bash
python -c "import streamlit; print('Streamlit OK')"
streamlit --version
```

### Step 4: Run the App
```bash
streamlit run app.py
```

## Common Error Messages and Fixes

### "Python was not found"
- Install Python from python.org
- Or use: `py -m streamlit run app.py`

### "streamlit: command not found"
- Run: `pip install streamlit`
- Or: `python -m pip install streamlit`

### "No module named 'surprise'"
- Run: `pip install scikit-surprise`

### "Address already in use"
- Close other Streamlit apps
- Or use: `streamlit run app.py --server.port 8502`

### "SyntaxError" or "IndentationError"
- The app.py file might be corrupted
- Check the file for syntax errors

## Alternative: Use Python Directly

If `streamlit` command doesn't work, use Python module:

```bash
python -m streamlit run app.py
py -m streamlit run app.py
python3 -m streamlit run app.py
```

## Check if Server is Actually Running

Even if browser doesn't open, check:
1. Look at terminal - does it show "Local URL: http://localhost:8501"?
2. If yes, manually open browser and go to: http://localhost:8501
3. If no, there's an error - check the error message

## Still Not Working?

1. **Run diagnostic:**
   ```bash
   python diagnose.py
   ```

2. **Check Python:**
   ```bash
   python --version
   ```

3. **Check pip:**
   ```bash
   pip --version
   ```

4. **Reinstall everything:**
   ```bash
   pip install --upgrade streamlit
   pip install -r requirements.txt
   ```

5. **Try minimal test:**
   ```bash
   streamlit hello
   ```
   If this works, the issue is with app.py, not Streamlit.

## Need More Help?

Share the exact error message you see, and I can help fix it!

