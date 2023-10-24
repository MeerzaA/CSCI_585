-- Meerza Ahmed: CSCI 585 HW2

-- DATABASE USED: https://livesql.oracle.com/

-- Q3 (1 point). Write a query to output the 'sickest' floor.


SELECT DISTINCT SYMPTOM.EMP_ID, EMPLOYEE.EMP_FLOOR_NUM 
FROM EMPLOYEE FULL JOIN POS_CASE ON EMPLOYEE.EMP_ID = POS_CASE.EMP_ID  
       INNER JOIN SYMPTOM ON SYMPTOM.EMP_ID = POS_CASE.EMP_ID 
ORDER BY EMPLOYEE.EMP_FLOOR_NUM 