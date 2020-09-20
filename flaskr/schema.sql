DROP TABLE IF EXISTS user
DROP TABLE IF EXISTS post
DROP TABLE IF EXISTS user_stock
DROP TABLE IF EXISTS stock

CREATE TABLE user(
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)

CREATE TABLE user_stock(
    username TEXT NOT NULL,
    stock_id INTEGER NOT NULL,
    FOREIGN KEY(username) REFERENCES user(username),
    FOREIGN KEY(stock_id) REFERENCES stock(stock_id)
)

CREATE TABLE stock(
    stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_name TEXT NOT NULL
)
