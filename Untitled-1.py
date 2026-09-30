class Student:
    college_name= "Aditya Institute of Technology"
    total_students=0
    PASS_MARK=35
    MAX_SUBJECTS=5

def __init__(self,roll_number,name,branch):
    self.name=name
    self._roll_number=roll_number
    self._branch=branch
    self.__marks={} # outside __init__, then every Student object shares the same dictionary, which is wrong.
    Student.total_students+=1

@property
def roll_number(self):
    return self._roll_number

@property
def average(self):
    if len(self._marks)==0:
        return 0.0
    return round(sum(self._marks.values())/len(self._marks),2)

@property
def grade(self):
    avg=self.average
    if(avg>=90):
        return "A+"
    elif(avg>=75):
        return "A"
    elif(avg>=60):
        return "B"
    elif(avg>=35):
        return "C"
    else:
        return "F"

def add_marks(self,subject,mark):
    '''
    if not isinstance(mark,(int,float)):
        raise TypeError("Mark must be a Number")
    if mark<0 or mark>100:
        raise ValueError("Mark must be between 0 and 100")
    '''
    Student.is_valid_mark(mark)
    if subject not in self.__marks and len(self.__marks)>=Student.MAX_SUBJECTS:
        raise ValueError("More than MAX_SUBJECTS subjects")
    self.__marks[subject]=mark

def get_marks(self):
    return dict(self.__marks)

def has_passed(self):
    for i in self.__marks.values():
        if i<Student.PASS_MARK:
            return False
    return True

def change_branch(self,new_branch):
    old=self._branch
    self._branch=new_branch
    return f"{old}->{new_branch}"

@classmethod
def get_total_students(cls):
    return cls.total_students

@staticmethod
def is_valid_mark(mark):
    if not isinstance(mark,(int,float)):
            raise TypeError("Mark must be a Number")
    if mark<0 or mark>100:
        raise ValueError("Mark must be between 0 and 100")
    return True

def __str__(self):
    return f"Student[{self.roll_number}] {self.name} | {self._branch} | Avg: {self.average:.2f} | Grade: {self.grade}"
