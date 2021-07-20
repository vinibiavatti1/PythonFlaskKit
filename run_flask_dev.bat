@echo off

REM Activate venv
cd .\.venv\Scripts
call activate.bat
cd ..\..

REM Set flask variables
set FLASK_APP=app
set FLASK_ENV=development

REM Run flask
flask run
pause
