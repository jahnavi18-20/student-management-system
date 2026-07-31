#project
students=[[1,'janu',90],
          [2,'manasa',80],
          [3,'pandu',50]]
def add_student():
    roll=int(input('enter a roll no: '))
    name=input('enter a student name: ')
    marks=float(input('enter a marks: '))
    students.append([roll,name,marks])
    print(f'{name} student added sucessfully')
def view_student():
    roll=int(input('enter a roll no to check: '))
    if not students:
        print('student is not found in our school')
        return
    print('-'*45)
    print(f'{'name':<10} {'roll':<10} {'marks':<10}')
    print('-'*45)
    for s in students:
        print(f'{s[0]:<10}{s[1]:<10}{s[2]:<10}')
    print('-'*45)

def search_student():
    roll=int(input('enter a roll no to check: '))
    found=False
    for s in students:
        if s[0]==roll:
            print(f'roll no:{s[0]}')
            print(f'name :{s[1]}')
            print(f'marks:{s[2]}')
            break
    if not found:
        print('student not found')
def update_student():
    roll=int(input('enter a roll no to check: '))
    found=False
    for s in students:
        name=input('enter a name to update: ')
        marks=float(input('enter a marks to update: '))
        s[1]=name
        s[2]=marks
        print(f'roll no{roll} updated sucessfully')
        found=True
        break
    if not found:
        print('student not found')

def delete_student():
    roll=int(input('enter a roll no to delete: '))
    found=False
    for s in students:
        if s[0]==roll:
            students.remove(s)
            print(f'roll no{roll} was deleted')
            found=True
            break
        if not found:
            print('student not found')
    

while True:
    print('1.add student')
    print('2.view all students')
    print('3.search student')
    print('4.update student')
    print('5.delete student')
    print('6.exit')
    choice=input('enter a choice(1/6): ')
    if choice=='1':
            add_student()
    elif choice=='2':
        view_student()
    elif choice=='3':
        search_student()
    elif choice=='4':
        update_student()
    elif choice=='5':
        delete_student()
    elif choice=='6':
        print('good bye')
        break
    else:
        print('enter correct choice')
