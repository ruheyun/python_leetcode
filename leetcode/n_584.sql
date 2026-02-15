-- Docstring for leetcode.n_584 寻找用户推荐人（数据库题）

SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id != 2;