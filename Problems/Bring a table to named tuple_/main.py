from collections import namedtuple

student_template = namedtuple('Student', 'name age department')
print(student_template('Alina', '22', 'linguistics'))
print(student_template('Alex', '25', 'programming'))
print(student_template('Kate', '19', 'art'))
