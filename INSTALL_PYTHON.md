# Python Installation Guide - Required to Run the App

## The Problem
Your system shows: "Python was not found"

This means Python is either:
1. Not installed
2. Installed but not in PATH
3. Needs to be configured

## Solution: Install Python

### Option 1: Install from Python.org (Recommended)

1. **Download Python:**
   - Go to: https://www.python.org/downloads/
   - Click "Download Python 3.x.x" (latest version)
   - Save the installer

2. **Run the Installer:**
   - Double-click the downloaded file
   - **IMPORTANT:** Check the box "Add Python to PATH" at the bottom
   - Click "Install Now"
   - Wait for installation to complete

3. **Verify Installation:**
   - Open a NEW Command Prompt or PowerShell
   - Type: `python --version`
   - You should see: `Python 3.x.x`

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the App:**
   ```bash
   streamlit run app.py
   ```

### Option 2: Install from Microsoft Store

1. Open Microsoft Store
2. Search for "Python 3.11" or "Python 3.12"
3. Click "Install"
4. After installation, open a NEW terminal
5. Run: `python --version` to verify

### Option 3: Use Anaconda/Miniconda

1. Download from: https://www.anaconda.com/download
2. Install Anaconda
3. Open "Anaconda Prompt"
4. Navigate to project folder
5. Install: `pip install -r requirements.txt`
6. Run: `streamlit run app.py`

## After Installing Python

### Step 1: Verify Python Works
```bash
python --version
pip --version
```

### Step 2: Install Dependencies
```bash
pip install streamlit pandas numpy scikit-learn scikit-surprise matplotlib seaborn
```

OR:
```bash
pip install -r requirements.txt
```

### Step 3: Run the App
```bash
streamlit run app.py
```

## If Python is Installed But Not Found

### Windows PATH Fix:

1. **Find Python Installation:**
   - Usually in: `C:\Users\YourName\AppData\Local\Programs\Python\`
   - Or: `C:\Python3x\`

2. **Add to PATH:**
   - Press `Win + R`
   - Type: `sysdm.cpl` and press Enter
   - Go to "Advanced" tab
   - Click "Environment Variables"
   - Under "System Variables", find "Path"
   - Click "Edit"
   - Click "New"
   - Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python3x\`
   - Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python3x\Scripts\`
   - Click OK on all windows
   - **Restart your terminal**

## Quick Test Commands

Try these in order until one works:

```bash
python --version
py --version
python3 --version
```

If any of these work, use that command:
```bash
py -m streamlit run app.py
python3 -m streamlit run app.py
```

## Still Having Issues?

1. **Restart your computer** after installing Python
2. **Open a NEW terminal** (don't use the old one)
3. **Check PATH:** `echo %PATH%` (should include Python)
4. **Reinstall Python** with "Add to PATH" checked

## Alternative: Use Online Services

If you can't install Python locally:
- Use Google Colab
- Use Replit
- Use Streamlit Cloud (for deployment)

---

**Once Python is installed, the app will run at: http://localhost:8501**

