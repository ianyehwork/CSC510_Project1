DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS user_stock;
DROP TABLE IF EXISTS stock;

CREATE TABLE user (
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE user_stock (
  username TEXT NOT NULL,
  ticker_name TEXT NOT NULL,
  FOREIGN KEY (username) REFERENCES user (username),
  FOREIGN KEY (ticker_name) REFERENCES stock (ticker_name),
  PRIMARY KEY (username,ticker_name)
);

CREATE TABLE stock (
  stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
  stock_name TEXT NOT NULL,
  ticker_name TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
