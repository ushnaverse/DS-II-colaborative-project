from PairingHeap import PairingHeap 
from datetime import datetime
class Task():
    def __init__(self, cname= "", weightage_=-1, date_=(0,0,0), personal_priority_=None, task_=""):
        print(date_)
        self.date = datetime(int(date_[0]), int(date_[1]), int(date_[2]))
        self.personal_priority = personal_priority_
        self.weightage = weightage_
        self.task = task_
        self.course_name = cname
        self.priority = self.priority_calculator()
       
    def priority_calculator(self):
        date = 4*((self.date-datetime.now()).days)
        weightage = 3*(self.weightage)
        personal = 2*(self.personal_priority)
        self.priority = ((date + weightage + personal) // 3)*-1
        return (self.priority)


# p = PairingHeap()
# task1= Task(10,(2023, 4, 21),10,"DO DS")
# task2= Task(15,(2023, 4, 21),10,"LA")
# task3= Task(30,(2023, 4, 25),15,"CA")
# task4= Task(20,(2023, 4, 23),5,"PnS")

# p.Insert(task1)
# # print(p.Top())
# p.Insert(task2)
# # print(p.Top())
# p.Insert(task3)
# p.Insert(task4)
# (p.traverse(p.root))
# print(p.tasks)
# # for i in k:
# #     print(i.task)
        
