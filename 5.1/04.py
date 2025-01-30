class Programmer:

    def __init__(self, name, post, workexp=0):
        self.name = name
        self.posts = {'Junior': 0, 'Middle': 1, 'Senior': 2}
        self.post = self.posts[post]
        self.workexp = workexp
        self.salary = 10 + 5 * self.posts[post]
        self.earnings = 0

    def work(self, time):
        self.workexp += time
        self.earnings += self.salary * time

    def rise(self):
        if self.post < 2:
            self.post += 1
            self.salary += 5
        else:
            self.salary += 1

    def info(self):
        return f"{self.name} {self.workexp}ч. {self.earnings}тгр."
    

programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())



        