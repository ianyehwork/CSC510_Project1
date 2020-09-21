DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS user_stock;
DROP TABLE IF EXISTS stock;

CREATE TABLE user (
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE user_stock (
  stock_id TEXT NOT NULL,
  username TEXT NOT NULL
);

CREATE TABLE stock (
  stock_id TEXT PRIMARY KEY,
  stock_name TEXT NOT NULL
);
