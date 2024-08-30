# Write your MySQL query statement below
SELECT W1.ID
FROM WEATHER W1
JOIN WEATHER W2
ON W1.RECORDDATE = DATE_ADD(W2.RECORDDATE, INTERVAL 1 DAY)
WHERE W1.TEMPERATURE > W2.TEMPERATURE