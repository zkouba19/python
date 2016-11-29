students = [
	{'first_name': 'Michael', 'last_name': 'Jordan'},
	{'first_name': 'John', 'last_name': 'Rosales'},
	{'first_name': 'Mark', 'last_name': 'Guillen'},
	{'first_name': 'KB', 'last_name': 'Tonel'},
]

instructors = [
	{'first_name': 'Michael', 'last_name': 'Choi'},
	{'first_name': 'Martin', 'last_name': 'Prunyear'},
]
for i in range(0,len(students)):
	fn = len(students[i]["first_name"])
	ln = len(students[i]["last_name"])
	length = fn + ln
	s = str(i+1) + " - " + students[i]["first_name"] + " " + students[i]["last_name"] + " - " + str(length)
	print s
for i in range(0,len(instructors)):
	fn1 = len(instructors[i]["first_name"])
	ln1 = len(instructors[i]["last_name"])
	length1 = fn1 + ln1
	inst = str(i+1) + " - " + instructors[i]["first_name"] + " " + instructors[i]["last_name"]  + " - " + str(length1)
	print inst