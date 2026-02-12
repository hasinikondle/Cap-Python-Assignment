class Exam:
    
    pass_marks = 40
    
    def __init__(self, student_name, total_marks, obtained_marks=0):
        self.student_name = student_name
        self.total_marks = total_marks
        self.obtained_marks = obtained_marks
        self.started = False
        self.submitted = False
    
    def start_exam(self):
        if not self.started and  not self.submitted:
            self.started = True
            print("Exam Started")
        else:
            print("Cannot start exam")

    def submit_exam(self):
        if self.started and not self.submitted:
            self.submitted = True
            self.started = False
            print("Exam Submitted")
        else:
            print("Cannot submit exam")

    
    def calculate_score(self):
        percentage = (self.obtained_marks / self.total_marks) * 100
        print("Score:", percentage)
        if percentage >= Exam.pass_marks:
            print("Result: Pass")
        else:
            print("Result: Fail")
    
    @classmethod
    def update_pass_marks(cls, new_marks):
        cls.pass_marks = new_marks


exam1 = Exam("Hasini", 100, 75)

exam1.start_exam()
exam1.calculate_score()
exam1.submit_exam()

print()

Exam.update_pass_marks(50)
exam1.calculate_score()
