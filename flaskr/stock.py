from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('stock', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT s.stock_id, stock_name'
        ' FROM stock s'
    ).fetchall()
    return render_template('stock/index.html', posts=posts)

@bp.route('/choose')
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
            stock_id = db.execute(
            'SELECT stock_id FROM stock WHERE stock_name = ?', (stock_name,)
        ).fetchone()
            db.execute(
                'INSERT INTO user_stock (username, stock_id)'
                ' VALUES (?, ?)',
                (session.get('username'), stock_id)
            )
            db.commit()
            return redirect(url_for('stock.index'))

    return render_template('stock/choose.html')
