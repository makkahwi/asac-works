DROP TABLE IF EXISTS movies;

CREATE TABLE IF NOT EXISTS movies (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  summary VARCHAR(10000)
);