# Write your MySQL query statement below
SELECT e.name, bonus
FROM employee AS e
LEFT OUTER JOIN bonus AS b
ON e.empId = b.empId
WHERE COALESCE(b.bonus, 0) < 1000