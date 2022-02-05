# University-Admission-Procedure
JetBrain Study project



1. Read an N integer from the input. This integer represents the maximum number of students for each department.

2. Read the file named applicants.txt Each line equals one applicant, their first name, last name, physics, chemistry, math, computer science, first priority department, second priority department, and third priority department. Columns with values are separated by whitespace characters. Each line contains four columns with scores for particular exams: physics, chemistry, math, computer science (in this order). For example, `John Ritchie 89 45 83 75 Physics Engineering Mathematics`.

3. Consider the following exam results for departments: physics and math for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science and math for the Engineering Department, chemistry and physics for the Biotech department.

4. For the departments that need several exams, calculate the mean score and use it to rank the applicants (use floating-point numbers with at least one decimal). Otherwise, use the result for a single exam.

5. Mind one additional column, right after the last exam's result. This column represents the special exam's score. For example, `Willie McBride 76 45 79 80 100 Physics Engineering Mathematics`(where 100 is the admission exam's score). Choose the best score for a student in the ranking: either the mean score for the final exam(s) or the special exam's score. Use the same set of finals for each Department as in the previous stage. Note that you may need to compare the values several times: for example, if a student doesn't get accepted to the Department of the first priority, compare the finals mean score and the special exam's score once again (but this time, for the second priority department).

6. Perform three stages of admission based on the applicants' priorities. Applicants should be ranked by their exam score and, in case they have the same score, their full name in alphabetic order. There should be no more than N accepted applicants for each department. One student can only be accepted to one department.

7. Output the admission lists to files. Create a file for each department, name it %department_name%.txt, for example, physics.txt. Write the names of the students accepted to the department and their mean finals score to the corresponding file (one student per line).




