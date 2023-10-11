
-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(55) NOT NULL
);

PRAGMA table_info('users');

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) 
    REFERENCES users(id)
);

PRAGMA table_info('articles');

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

SELECT *
FROM users;

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);


-- INNER JOIN
SELECT * FROM users
INNER JOIN articles 
  ON users.id = articles.userId;


SELECT articles.title, users.name 
FROM articles
INNER JOIN users 
  ON users.id = articles.userId
WHERE users.id = 1;














-- LEFT JOIN
SELECT * FROM users
LEFT JOIN articles
  ON users.id = articles.userId;

SELECT * FROM users
LEFT JOIN articles 
  ON articles.userId = users.id
WHERE articles.userId IS NULL;


-- 심화 (직접 해보기)
-- CREATE TABLE articles (
  -- id INTEGER PRIMARY KEY AUTOINCREMENT,
  -- title VARCHAR(50) NOT NULL,
  -- content VARCHAR(100) NOT NULL,
  -- userId INTEGER NOT NULL,
  -- FOREIGN KEY (userId) 
  --   REFERENCES users(id)
--     ON DELETE SET NULL
-- );

-- INSERT INTO 
--   users (name)
-- VALUES 
--   ('권미자'),
--   ('류준하'),
--   ('정영식'),
--   ('테스트');

-- DELETE FROM users 
-- WHERE id = 4;


