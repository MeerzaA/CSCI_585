-- Meerza Ahmed: CSCI 585 HW2

-- DATABASE USED: https://livesql.oracle.com/

-- Q5 (1 point). Create your own query! What else would you like to learn, from the data? Describe/list the question, and come up with the query to answer it. You'll get 1 extra point if your query involves table division [be sure to indicate this in your README].

-- "What is the average temperature across all scans in the scan table". I am trying to figure out what temperature employees have on average. I higher average would mean more people either have or are developing a fever, a lower average would mean most employees have a normal body temperature. 


SELECT AVG(SCAN_TEMP) 
FROM SCAN;
