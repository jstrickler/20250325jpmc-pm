DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS {{cookiecutter.app_slug}};

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE {{cookiecutter.app_slug}}s (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  data TEXT NOT NULL
);