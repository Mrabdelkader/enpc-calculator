@echo off
REM Create and activate virtual environment
python -m venv venv
call venv\Scripts\activate

REM Install required packages
pip install -r requirements.txt

REM Run the application
python sys.py
