# PowerShell script to run the Streamlit app
Write-Host "Starting Course Recommendation System..." -ForegroundColor Green
Write-Host ""
Write-Host "Make sure you have installed all dependencies:" -ForegroundColor Yellow
Write-Host "  pip install -r requirements.txt" -ForegroundColor Yellow
Write-Host ""
Write-Host "Starting Streamlit app..." -ForegroundColor Green
Write-Host ""

# Try different Python commands
$pythonCmds = @("python", "py", "python3")

foreach ($cmd in $pythonCmds) {
    try {
        $version = & $cmd --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Using: $cmd" -ForegroundColor Cyan
            & $cmd -m streamlit run app.py
            break
        }
    } catch {
        continue
    }
}

Write-Host ""
Write-Host "If the app didn't start, try:" -ForegroundColor Yellow
Write-Host "  1. Install Python from python.org" -ForegroundColor Yellow
Write-Host "  2. Install dependencies: pip install -r requirements.txt" -ForegroundColor Yellow
Write-Host "  3. Run: streamlit run app.py" -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to exit"


