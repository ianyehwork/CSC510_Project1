from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('stock', __name__)


@bp.route('/')
def home():
    return redirect(url_for('auth.login'))


@bp.route('/index')
@login_required
def index():
    # db = get_db()
    # I created a method in this file get_post() which gets all the ticker names from stock_id, which is currently just amazon
    # posts = get_post()
    # You need to do the following - for each stock_id in posts, call the fetch_data function, save the matplotlib chart image into static folder
    # with the filename format COMAPNYNAME-DD-MM-YY for the date upto which model has been made
    # Now populate the below list(of lists) with ['COMPANYNAME','FILENAME'] for each company, format which will be read at website
    # This is all static to represent working
    info_stocks = [['AMZN', 'AMZN-DD-MM-YY.png']]
    return render_template('stock/index.html', posts=info_stocks)


@bp.route('/choose', methods=('POST', 'GET'))
@login_required
def choose():
    if request.method == 'POST':
        stock_name = request.form['stock_name']
        error = None

        if not stock_name:
            error = 'Stock Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            try:
                stock_id = db.execute(
                    'SELECT stock_id FROM stock WHERE stock_name = ?', (stock_name,)).fetchone()
                # The API which gets data from internet does not take company name for getting data, but rather ticker for the company
                # For example Amazon has ticker AMZN, Apple AAPL, so gather a list from internet which gives you this conversion
                # Then u need to store those into stock_id column of stock table corresponding to each company
                db.execute('INSERT INTO user_stock '
                           ' VALUES (?, ?)',
                           (session.get('username'), 'AMZN'))
                # Currently I am just storing AMZN only to represent, you can modify it back to previous way after you are able to get
                # correct tickers
                db.commit()
                print('Got Ticker')
            except Exception as e:
                print(e)
            return redirect(url_for('stock.index'))

    return render_template('stock/choose.html')


def get_post():
    try:
        print(session.get('username'))
        post = get_db().execute('SELECT stock_id from user_stock WHERE username = ?',
                                (session.get('username'),)).fetchall()
        print(post)
    except Exception as e:
        print(e)
    return post
