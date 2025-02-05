class Crew_Member:
    group = 9
    language ='Python'
    
    def info(self):
        print(f'{self.name} is a valuable member of crew {self.group}.\n He is an expert in {self.language}.\n')
    
    @staticmethod
    def greet():
        print('Good Morning')



print(Crew_Member().language)

riju = Crew_Member()
riju.name = 'Soumya Mahata'
riju.greet()
riju.info()

tuhin = Crew_Member()
tuhin.name = 'Tuhin Bidyanta'
tuhin.language = 'Java'
tuhin.info()