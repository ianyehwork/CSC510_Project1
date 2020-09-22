## Technologies and Tools
<b>Language</b>: Python 3, HTML, CSS

<b>Libraries</b>: Flask, click, yfinance, matplotlib, Werkzeug, pandas, numpy, get_all_tickers, pytest, scikit_learn.

<b>Web Application Framework</b>: Flask

<b>Test Framework</b>: pytest

<b>Database</b>: SQLite

<b>Tools</b>: Visual Studio Code

<b>Syntax Checker & Sytle Checker</b>: pylint (VSCode Python v2020.8.109390 Extension)

<b>Code Formatter</b>: autopep8 (VSCode Python-autopep8 v1.0.2)

<b>Version Control</b>: git

# Installation Guide
## Using Docker
1. navigate to the project directory with the Dockerfile
2. docker build -t csc510/p1:latest .
3. docker run -p 5000:5000 csc510/p1:latest
4. open browser and enter http://localhost:5000/auth/login

## For Mac/Ubuntu  
Install Flask using pip - pip/pip3 install flask

cd to project directory

export FLASK_APP=flaskr

flask init-db

## For Windows
Install Flask using pip - pip/pip3 install flask

cd to project directory

set FLASK_APP=flaskr

flask init-db

## Run  
To run just do the following

flask run
