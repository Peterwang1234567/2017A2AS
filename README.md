# 2017A2AS
Peter
*** TASK 1.1***
JPL structure diagrams help to design a program, and it gives the exact structure that the program will handle.

*** TASK 1.2***
*: Repetition*
°: Selection

*** TASK 1.3***
WHILE EndOfFile = FALSE
	CALL ReadSalary()
	IF Salary > 50
		THEN
			IF Salary >= 90
				THEN
					Role = ProjectManager
				ELSE
					Role = LeadDeveloper
			ENDIF
		ELSE
			Role = Manager
	ENDIF
ENDWHILE

*** TASK 1.4***
           Salary > 50
     FALSE              TRUE                   
Assign Manager         Salary >=90   
     FALSE                    TRUE
Salary >70          Assign Project Manager
       FALSE                    TRUE 
Assign Lead Developed      Assign Consultant 

*** TASK 1.5***
IF Salary >= 90 
	THEN 
	Role = ProjectManager 
  ELIF Salary > 70 
			THEN 
				Role = Consultant 
			ELSE 
				Role = LeadDeveloper 
		ENDIF 
ENDIF

*** TASK 1.6***
def determinerole(salary):
    if salary>50:
        if salary>70:
            if salary>=90
                return 'projectmanager'
            else:
                return 'consultant'
        else:
            return 'leaddeveloper'
    else:
        return 'manager'
