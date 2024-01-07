MEERZA AHMED CSCI 585 HW2 | README- 10/8/2023

I loaded my tables manually with a few rows and gave my attributes simple values, such as EMP_ID being (00000001,00000002,..etc)
I did this for my own testing, to make sure that my logic was correct for answers Q2-Q5. We were given the freedom to create as many or as little rows as we saw fit.  

Please keep my tables from Q1, my SQL files for Q2-Q5 only have the answers to that specific question. My Q1 file creates all the relevant tables and loads them with data, which is queried by Q2-Q5. 

Q1: For anything related to time when creating the tables, I assumed that every 'TIME' related attribute would round to the nearest hour since we were told to use integers and have them between 0-23, this also applies to meetings as we had to set a time between 8-18

The Employee and Meetings tables relationship is shown as 1:M in the chart but I couldn't figure out why that was the case, since 1 employee can have many meetings and every meeting can have many employees. In my answer, I decided to treat the Employee and Meeting table as an M:N relationship when writing my SQL and created a bridge table called ATTENDANCE to handle the M:N relationship. The idea is that someone creates meetings in the company and assigns employees to them (like a supervisor or manager) and the employees who actually attend these meetings would appear in the ATTENDANCE Table. 

Every table required Employee ID as an attribute. Now aside from Meetings, I didn't see it necessary to create bridge tables for Notification, test, Scan, and case. These tables had their own PK in the form of Case_ID, Notif_ID, Scan_ID..etc and that should be enough to identify every row individually. Also, the chart showed this relationship as 1:M so I assume this is how the professor wanted us to do it.

For symptom and Health status tables, I'm assuming that these are reported separately from one another and the ROW_ID isn't the same in both tables. I made a composite key for row_ID and EMP_ID in both symptom and health status since that would be enough to identify every row individually. 

For health status and SYMPTOMS, I assumed that employees reported once a day. Symptom ID required a number between 1 and 5 for the possible symptoms the company wanted reported, I am assuming that employees only report one symptom once a day as having a symptom of any kind would require a COVID TEST. Also, I know that employees can have more than 1 symptom at a time, but it wouldn't make sense for employees to report each symptom individually. I was unsure how the SYMPTOM table was supposed to work, why have a Symptom ID from 1-5 and have employees report just 1 symptom at a time, I was thinking of just having a HAVE_SYMPTOMS attribute which either holds a value of 'YES' or 'NO', but changed it back to the original method.  

Q2: I am assuming that you want the most repeated value from the Symptom ID column, I made an ordered list showing every symptom and how many times they appeared in the table. the most common symptom is at the top.

Q3: For this question one of the instructors in Piazza stated that the sickest floor is "the floor with the most number of positive cases + symptomatic individuals". So I need to find out which floor got the most positive cases and out of those which floor also has the most individuals with symptoms. To do this I did a FULL join with the Employee table (EMPLOYEE) with the cases table (POS_CASE). So I isolated every employee who had a positive COVID CASE, and then I did another INNER JOIN with the SYMPTOMS table to get all individual employees who also had symptoms. *My final submission was wrong, I was only able to accomplish half of this in time to submit my assingment.

Q4: Didn't get to this one

Q5: I just went with an easy question, to be honest, but Q5 does seem like it was a freebie anyway. I hope that is OK.
The question is in the SQL file but I will also leave it here: "What is the average temperature across all scans in the scan table". I am trying to figure out what temperature employees have on average. I higher average would mean more people either have or are developing a fever, a lower average would mean most employees have a normal body temperature. 
