# sort students by rate of required exam or by mean rate of required exams, then name and surname
def sort_list(_students, dep):

    def sort_conditions(student):
        mean = mean_rate(student, dep)
        gpa = float(student[gpa_id])
        return -max(mean, gpa), student[name_id], student[surname_id]

    return sorted(_students, key=sort_conditions)


def mean_rate(_x, _dep):
    exams = dep_exams[_dep]
    total = 0
    for exam in exams:
        exam_index = s_data[exam]  # position of required exam rate in the list with student data
        total += float(_x[exam_index])
    return round(total / len(exams), 2)


def save_accepted_students():
    for department, accepted in departments.items():
        file_name = department.lower() + '.txt'
        with open(file_name, 'w') as f:
            for student in sort_list(accepted, department):
                mean = mean_rate(student, department)
                gpa = float(student[gpa_id])
                rate = max(mean, gpa)
                f.write(f'{student[name_id]} {student[surname_id]} {str(rate)}\n')


def accept_students(not_accepted):
    for priority in [1, 2, 3]:
        priority_index = s_data[f'{priority}_pr']  # position of current priority in the list with student data
        for department, accepted in departments.items():
            free_places = num_accepted - len(accepted)
            not_accepted = sort_list(not_accepted, department)  # sort students by of required exam
            #not_accepted = sorted(not_accepted, key=sort_conditions)

            if free_places:
                accepted = [student for student in not_accepted if student[priority_index] == department]
                departments[department] += accepted[:free_places]
                # updates not_accepted_list, by not including just accepted students
                not_accepted = [student for student in not_accepted if student not in departments[department]]


num_accepted = int(input())

departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

s_data = {'name': 0, 'surname': 1, 'physics': 2, 'chemistry': 3, 'math': 4, 'computer science': 5,
          'gpa': 6, '1_pr': 7, '2_pr': 8, '3_pr': 9
          }

dep_exams = {'Biotech': ['chemistry', 'physics'],
             'Chemistry': ['chemistry'],
             'Engineering': ['computer science', 'math'],
             'Mathematics': ['math'],
             'Physics': ['physics', 'math']
             }

gpa_id, name_id, surname_id = s_data['gpa'], s_data['name'], s_data['surname']

with open('applicants.txt', 'r') as applicants_file:
    students = [student.split() for student in applicants_file]

accept_students(students)
save_accepted_students()
