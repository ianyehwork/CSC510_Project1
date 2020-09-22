# Stock Exchange Prediction using Machine Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Build Status](https://travis-ci.com/ianyehwork/CSC510_Project1.svg?branch=master)](https://travis-ci.com/ianyehwork/CSC510_Project1)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4042066.svg)](https://doi.org/10.5281/zenodo.4042066)

## Video

Below is the video which describes our project's idea and implementation

[![Stock Market Predictions using Machine Learning](http://i3.ytimg.com/vi/3YbNEt3dYtc/hqdefault.jpg)](https://www.youtube.com/watch?v=3YbNEt3dYtc)

## Why choose this project:

- The project provides visualisation of stocks of 2000+ company markets and helps in making prediction for the next time period.
- Modular architecture
- Scalable design
- You will be able to explore data analysis, predictive modelling and explore the integration of NLP functionality.
- You can scale the project to use different predictive models to compare the efficiencies as well as compare different stocks to make the right decision to invest.

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

## Run  
To run just do the following

flask run

# Application Overview
<img src="/doc/ApplicationStructure.png" />

# Database Schema
<img src="/doc/Schema.png" />
