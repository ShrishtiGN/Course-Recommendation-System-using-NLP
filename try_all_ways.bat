@echo off
echo ========================================================================
echo TRYING TO RUN STREAMLIT APP - Testing All Methods
echo ========================================================================
echo.

echo [Method 1] Trying: streamlit run app.py
streamlit run app.py
if %ERRORLEVEL% EQU 0 goto success

echo.
echo [Method 2] Trying: py -m streamlit run app.py
py -m streamlit run app.py
if %ERRORLEVEL% EQU 0 goto success

echo.
echo [Method 3] Trying: python -m streamlit run app.py
python -m streamlit run app.py
if %ERRORLEVEL% EQU 0 goto success

echo.
echo [Method 4] Trying: python3 -m streamlit run app.py
python3 -m streamlit run app.py
if %ERRORLEVEL% EQU 0 goto success

echo.
echo ========================================================================
echo ALL METHODS FAILED
echo ========================================================================
echo.
echo Python is not installed or not in PATH.
echo.
echo SOLUTIONS:
echo 1. Install Python from https://www.python.org/downloads/
echo 2. Make sure to check "Add Python to PATH" during installation
echo 3. Restart your computer after installation
echo 4. Open a NEW terminal and try again
echo.
echo See INSTALL_PYTHON.md for detailed instructions.
echo.
pause
exit /b 1

:success
echo.
echo ========================================================================
echo SUCCESS! App should be running at http://localhost:8501
echo ========================================================================
pause

