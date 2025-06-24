class name_change:
    def __init__(self,name):
        self.name = name + " Changed"

class Person(name_change):
    def __init__(self,name:str,age:int,subject:str):
        super().__init__(name)
        self.name += " ######"
        self.age = age
        self.subject = subject
    def info(self):
        return f"{self.name}'s age is {self.age}"

class ClassRoom(Person):
    TOP_SCORE = 0
    def __init__(self,**details):
        self.__dict__ = details
        ClassRoom.TOP_SCORE = self.marks if ClassRoom.TOP_SCORE < self.marks else ClassRoom.TOP_SCORE

    def change_subject(self,subject):
        self.subject = subject
        super().__init__(self.name,self.age,self.subject)
    
    @classmethod
    def merit_student(cls):
        
        # db : dict[str, int] = {"raju":1,"looser":3,"Medium":2}
        # @staticmethod
        # def highest_score() -> int:
            # for i,j in db.items():
                # if j == score:
        return ClassRoom.TOP_SCORE
        # top_ranker : int = highest_score(marks)
        # return top_ranker
    
    @staticmethod
    def no_instance():
        print("Callable without an instance")

# class_room_details = ClassRoom(**{"name":"Ram","age":90,"class_room":"X","subject":"Maths"})
# class_room_details.change_subject("English")
# ClassRoom.no_instance()
person_1 = ClassRoom(**{"name":"Ram","age":90,"class_room":"X","subject":"Maths","marks":90})
person_2 = ClassRoom(**{"name":"Raman","age":90,"class_room":"X","subject":"Maths","marks":98})
person_3 = ClassRoom(**{"name":"Ramu","age":90,"class_room":"X","subject":"Maths","marks":88})
highest_scorer = ClassRoom.merit_student()
print(highest_scorer)