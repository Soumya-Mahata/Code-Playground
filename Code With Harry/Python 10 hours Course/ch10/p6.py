class Programmer:
    company = 'SLB'
    salary = 50

    def __init__(harry, name, gender, language):
        harry.name = name
        harry.gender = gender
        harry.language = language
    
    def get_info(harry):
        if harry.gender == 'Male':
            pronoun = "He"
        else:
            pronoun = "She"
        print(f'Full name: {harry.name} \nSalary: {harry.salary}LPA \n{pronoun} is an expert in {harry.language}. \n{pronoun} works in {harry.company}. \n')

    @staticmethod
    def greet():
        print('Introducing')


names = ['trina', 'sneha','tuhin', 'arka', 'mal' , 'riju']
full_names = ['Trinakshi Tarai', 'Sneha Karmakar', 'Tuhin Bidyanta', 'Arkajit Roy', 'Soumyadeep Mal', 'Soumya Mahata']

for i in range(len(names)):
    if (names[i] == 'sneha') or (names[i] == 'trina'):
        names[i] = Programmer(full_names[i], 'Female', "Python")
    else:
        names[i] = Programmer(full_names[i], 'Male', 'Python')
    names[i].greet()
    names[i].get_info()
