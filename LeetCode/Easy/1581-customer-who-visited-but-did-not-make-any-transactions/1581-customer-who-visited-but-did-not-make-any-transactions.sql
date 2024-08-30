# Write your MySQL query statement below
SELECT CUSTOMER_ID, COUNT(*) AS COUNT_NO_TRANS
FROM VISITS AS V
LEFT JOIN TRANSACTIONS AS T ON V.VISIT_ID = T.VISIT_ID
WHERE TRANSACTION_ID IS NULL
GROUP BY V.CUSTOMER_ID