class Crew_Member:
    group = 9
    def __init__(self, name, salary=30, language='Python'):# Dunder Metod; which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
    
    def info(self):
        print(f'{self.name}, an expert in {self.language}, is a valuable member of crew {self.group}. \nSalary:{self.salary}LPA \n')
    
    @staticmethod
    def greet():
        print('Introducing')

names = ['trina', 'sneha','tuhin', 'arka', 'riju', 'mal']
full_names = ['Trinakshi Tarai', 'Sneha Karmakar',"Tuhin Bidyanta", 'Arkajit Roy', 'Soumya Mahata', 'Soumyadeep Mal']

for i in range(len(names)):
    if names[i] == 'tuhin':
        names[i] = Crew_Member(full_names[i], 30, "Java")
    else:
        names[i] = Crew_Member(full_names[i])
    names[i].greet()
    names[i].info()

