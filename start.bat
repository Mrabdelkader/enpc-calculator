@echo off
REM Check if pip is installed
pip --version
IF %ERRORLEVEL% NEQ 0 (
    echo Pip is not installed. Installing pip...
    python -m ensurepip
)
REM Install required packages
pip install -r requirements.txt
REM Run the application
python sys.py
