students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def printNames(nameDict):
    for student in nameDict:
        print student["first_name"] + " " + student["last_name"]

printNames(students)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def nameInfo(nameDict):
    for category in users:
        print category
        for index in range(0,len(users[category]),1):  
            print index+1, " - ",
            print users[category][index]['first_name'], users[category][index]['last_name'], " - ",
            print len(users[category][index]['first_name']) + len(users[category][index]['last_name'])
           




nameInfo(users)

