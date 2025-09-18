import csv
import json
import time

class SchoolBase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.students = []
        self.teachers = {}
        self.load_data()
        
    def load_data(self):
        with open(self.file_path, "r") as md: 
            reader = csv.reader(md) 
            for row in reader:
                if len(row) !=7:
                    print("некоректний формат файлу")
                    exit(1)
                
                student = {"StLastName": row[0], "StFirstName": row[1], "Grade": int(row[2]), "Classroom": int(row[3]), "Bus": int(row[4]), "TLastName": row[5], "TFirstname": row[6]}
                self.students.append(student)
                teacher_key = (row[5], row[6])
                
                if teacher_key not in self.teachers:
                    self.teachers[teacher_key] = []
            
                self.teachers[teacher_key].append(student)
                    
    def search_by_student(self, last_name):
        start_time = time.time()
        results = [s for s in self.students if s["StLastName"].lower() == last_name.lower()]
        elapsed_time = time.time() - start_time
        
        if results:
            print(f"Студенти з прізвищем {last_name}")
            for student in results:
                print(f"{student['StLastName']} {student['StFirstName']} є вихованцем {student['TLastName']} {student['TFirstname']} у класі {student['Classroom']}")
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
        #results = [v for k,v in self.teachers.items() if k[0]==last_name]
        #print(results[1])
        results=[s for s in self.students if s["TLastName"].lower() == last_name.lower()]
        elapsed_time = time.time() - start_time
        
        if results:
            print(f"Студенти, у яких  прізвище викладача {last_name}")
            for student in results:
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


file_path = 'students.txt'
database = SchoolBase(file_path)
    
while True:
    print("\nОпції: \n S[tudent]: <lastname> BUS \n S[tudent]: <lastname> \n T[eacher]: <lastname> \n C[lassroom]: <number> \n B[us]: <number> \n Q[uit]")
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
        classroom = int(choise.split()[1])
        database.search_by_classroom(classroom)
             
    elif choise.lower().startswith("b"):
        bus = int(choise.split()[1])
        database.search_by_bus_route(bus)
   
    elif choise.lower().startswith("q"):
        print("Завершення програми")
        exit()
        
    else:
        print("Недійсна команда")
      
        
