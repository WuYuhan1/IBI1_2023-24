#define a class reflcting a student
class students(object):
    def __init__(self,name,major,code_score,group_score,exam_score):
        #students name; major(BMI/BMS); score for their code portfolio; score for their group project; and exam score.
        self.name=name
        self.major=major
        self.code_score=code_score
        self.group_score=group_score
        self.exam_score=exam_score
    def information(self):
        #print all information in a line
        print("student's name:",self.name,", major:",self.major,", code portfolio score:",self.code_score,", group project score:",self.group_score,", exam score:",self.exam_score)
        return()
#example of using the class
student1=students("A","BMI",100,100,100)
student1.information()