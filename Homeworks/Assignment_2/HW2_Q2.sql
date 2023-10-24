-- Meerza Ahmed: CSCI 585 HW2

-- DATABASE USED: https://livesql.oracle.com/

-- Q2(1 point): Write a query to output the most-self-reported symptom.

SELECT SYMP_ID, COUNT(*) AS "Num of Occurrence" 
FROM SYMPTOM 
GROUP BY SYMP_ID 
ORDER BY "Num of Occurrence" DESC 
FETCH FIRST ROW only;
