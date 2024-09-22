# Write your MySQL query statement below
WITH ConsecutiveNums AS (
    SELECT
        num,
        LAG(num, 1) OVER () AS prev_num,
        LEAD(num, 1) OVER () AS next_num
    FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM ConsecutiveNums
WHERE num = prev_num AND num = next_num;