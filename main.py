import csv
import time


class SchoolBase:
    def __init__(self, students_path,teachers_path):
        self.students_path = students_path
        self.teachers_path=teachers_path
        self.students = []
        self.teachers = []
        self.load_data()
        
    def load_data(self):
        with open(self.students_path, "r") as md: 
            reader = csv.reader(md) 
            for row in reader:
                if len(row) !=5:
                    print("некоректний формат файлу list.txt")
                    exit(1)
                
                student = {"StLastName": row[0], "StFirstName": row[1], "Grade": int(row[2]), "Classroom": int(row[3]), "Bus": int(row[4])}
                self.students.append(student)
            
        with open(self.teachers_path,"r") as md:  
            reader = csv.reader(md) 
            for row in reader:
                if len(row) !=3:
                    print("некоректний формат файлу list.txt")
                    exit(1)  
                     
            teacher={"TLastName": row[0], "TFirstname": row[1],"Classroom":int(row[2])}
            self.teachers.append(teacher)
    
    def search_teacher_by_classroom(self,classroom,print=False):
        start_time = time.time()
        results = [t for t in self.teachers if t["Classroom"] == classroom]
        elapsed_time = time.time() - start_time
        if print:
            if results:
                print(f"Вчителі з класу {classroom}")
                for teacher in results:
                    print(f"{teacher['TLastName']} {teacher['TFirstName']} ")
            else:
                print("Немає вчителів з цього класу")      
            print(f"Час пошуку {elapsed_time} секунд")
        return results
                     
    def search_by_student(self, last_name):
        start_time = time.time()
        results = [s for s in self.students if s["StLastName"].lower() == last_name.lower()]
        elapsed_time = time.time() - start_time
        
        if results:
            print(f"Студенти з прізвищем {last_name}")
            for student in results:
                teachers=self.search_teacher_by_classroom(student["Classroom"])
                for teacher in teachers:
                    print(f"{student['StLastName']} {student['StFirstName']} є вихованцем {teacher['TLastName']} {teacher['TFirstname']} у класі {student['Classroom']}")
        else:
            print("За таким прізвищем студента не знайдено") 
        print(f"Час пошуку {elapsed_time} секунд")      
        
    def search_by_student_bus(self, last_name):
        start_time = time.time()
        results = [s for s in self.students if s["StLastName"].lower() == last_name.lower()]
        elapsed_time = time.time() - start_time
        
        if results:
            print(f"Студенти з прізвищем {last_name}")
            for student in results:
                print(f"{student['StLastName']} {student['StFirstName']} їзде маршрутом {student['Bus']} до школи ")
        else:
            print("За таким прізвищем студента не знайдено")  
        print(f"Час пошуку {elapsed_time} секунд")
            
    def search_by_teacher(self, last_name):
        start_time = time.time()
    
        results=[t for t in self.teachers if t["TLastName"].lower() == last_name.lower()]
        elapsed_time = time.time() - start_time
        
        if results:
            print(f"Студенти, у яких  прізвище викладача {last_name}")
            for teacher in results:
                students=[s for s in self.students if s["Classroom"]==teacher["Classroom"]]
                for student in students:
                    print(f"{student['StLastName']} {student['StFirstName']}")
        else:
            print("Цей викладач не має студентів")  
        print(f"Час пошуку {elapsed_time} секунд")
        
            
    def search_by_classroom(self, classroom):
        start_time = time.time()
        results = [s for s in self.students if s["Classroom"] == classroom]
        elapsed_time = time.time() - start_time
        
        if results:
            print(f"Студенти з класу {classroom}")
            for student in results:
                print(f"{student['StLastName']} {student['StFirstName']} ")
        else:
            print("Немає студентів з цього класу")      
        print(f"Час пошуку {elapsed_time} секунд")

            
    def search_by_bus_route(self, bus_route):
        start_time = time.time()
        results = [s for s in self.students if s["Bus"] == bus_route]
        elapsed_time = time.time() - start_time
        
        if results:
            print(f"Студенти з класу, які їздять маршрутом {bus_route} до школи")
            for student in results:
                print(f"{student['StLastName']} {student['StFirstName']} ")
        else:
            print("Немає студентів з цього класу")  
        print(f"Час пошуку {elapsed_time} секунд")
        
    def search_by_grade(self,grade):
        start_time = time.time()
        results = [s for s in self.students if s["Grade"] == grade]
        elapsed_time = time.time() - start_time
        
        if results:
            print(f"Студенти , які мають грейд {grade}")
            for student in results:
                print(f"{student['StLastName']} {student['StFirstName']} ")
        else:
            print("Немає студентів з таким грейдом")  
        print(f"Час пошуку {elapsed_time} секунд")
    
    def search_by_grade_teachers(self,grade):
        start_time = time.time()
        results = [s for s in self.students if s["Grade"] == grade]
        elapsed_time = time.time() - start_time
        
        if results:
            print(f"Учителі , які мають грейд {grade}")
            for student in results:
                teachers=self.search_teacher_by_classroom(student["Classroom"])
                for teacher in teachers:
                    print(f"{teacher['TLastName']} {teacher['TFirstname']}")
        else:
            print("Немає учителів з таким грейдом")  
        print(f"Час пошуку {elapsed_time} секунд")


students_path = "Laba2\list.txt"
teachers_path=r"Laba2\teachers.txt"
database = SchoolBase(students_path,teachers_path)
    
while True:
    print("\nОпції: \n S[tudent]: <lastname> BUS \n S[tudent]: <lastname> \n T[eacher]: <lastname> \n C[lassroom]: <number> \n B[us]: <number> ")
    print("G[rade]: <Number>\n C[lassroom]: <Number> Teacher\n G[rade]: <Number> Teacher\n Q[uit]")
    choise = input("Виберіть команду: ").strip()
        
    start_time = time.time()
        
    if choise.lower().startswith("s"):
        if "bus" in choise.lower():
            last_name = choise.split()[1]
            database.search_by_student_bus(last_name)
        else:
            last_name = choise.split()[1]
            database.search_by_student(last_name)
            
    elif choise.lower().startswith("t"):
        last_name = choise.split()[1]
        database.search_by_teacher(last_name)
        
    elif choise.lower().startswith("c"):
        if "teacher" in choise.lower():
            classroom = int(choise.split()[1])
            database.search_teacher_by_classroom(classroom,print=True)
        else:
            classroom = int(choise.split()[1])
            database.search_by_classroom(classroom)
             
    elif choise.lower().startswith("b"):
        bus = int(choise.split()[1])
        database.search_by_bus_route(bus)
    
    elif choise.lower().startswith("g"):
        if "teacher" in choise.lower():
            grade=int(choise.split()[1])
            database.search_by_grade_teachers(grade)
        else:
            grade = int(choise.split()[1])
            database.search_by_grade(grade)
    
    elif choise.lower().startswith("q"):
        print("Завершення програми")
        exit()
        
    else:
        print("Недійсна команда")
      
        
