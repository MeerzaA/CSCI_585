MEERZA AHMED CSCI 585 HW1 | README- 09/17/2023


RELATIONSHIPS 

EMPLOYEE : REGISTRATION_SYSTEM (1:M) - Employees can register in the system 1 time but the registration system can have many employees registar  
EMPLOYEE : COVID_TEST_REPORT (1:M) - Employees can submit many COVID test reports, but every test report pertains to only 1 employee 
EMPLOYEE : QUARANTINE_STATUS_REPORT (1:M) - Employees can update their status many times, every status update pertains to 1 employee 
EMPLOYEE : COVID_SYMPTOM_REPORT (1:M) - Employees can report COVID symtoms many times, but every symptom report pertains to 1 employee  
EMPLOYEE : MEETINGS (M:N) - Emplpoyees can have many meetings, every meeing can have many employees  
EMPLOYEE : FACILITY_TRAFFIC_LOG (M:N) - Employees can enter and exit the facility many times, the facility has many employees enter and exit 

EMP_HEALTH_APP : COVID_TEST_REPORT (1:M) - The employee health app can recieve many test reports, but only store the latest 1 (the latest report)
EMP_HEALTH_APP : QUARATINE_STATUS_REPORT (1:M) - The employee health app can recieve many quaratine status updates, but only store the latest 1 (the latest report)
EMP_HEALTH_APP : COVID_SYMPTOM_REPORT (1:M) - The employee health app can recieve many COVID symptom reports, but only store the latest 1 (the latest report)
EMP_HEALTH_APP : REGISTRATION_SYSTEM (1:1) - The employee health app creats 1 profile, the registration system can only register 1 profile at a time 
EMP_HEALTH_APP : CONTACT_TRACKING_SYSTEM (1:1) - The employee health app triggers the contact tracking system for every 1 COVID case, the COVID tracking system can track only 1 case at a time

FACILITY_TRAFFIC_LOG : RANDOM_TEMPERATURE_SCAN (1:1) - Every 1 tempature scan is related to 1 instance of an employee either entering or exiting the building 
FACILITY_TRAFFIC_LOG : COMPANY_COVID_TEST (1:1) - Every 1 COVID test is realted to 1 instancve of an employee either entering or exiting the building 
RANDOM_TEMPATURE_SCAN : COMPANY_COVID_TEST (1:1) - For every 1 instance of high fever there has to be one instance of COVID test (company requires COVID test if employee has high fever)

CONTACT_TRACKING_SYSTEM : EMPLOYEE_NOTIFY_LIST (1:1) - For every 1 instance of the tracking system being triggerd there has to be 1 instance of employees being notified who are on the same floor 
CONTACT_TRACKING_SYSTEM : AFFECTED_EMPLOYEES (1:M) - The contact tracking system can find many affacted employees for every 1 time it is triggered (due to a posative covid case)  
CONTACT_TRACKING_SYSTEM : MEETINGS (1:M) - The contact tracking can find many meetings for every 1 time it is triggered (due to a posative covid case)

HR_CONTACT_LIST : AFFECTED_EMPLOYEE (1:1) - For every 1 affacted employee, there is 1 notification made by HR in the form of a call or email  