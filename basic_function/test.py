import requests

class CheckSolution:
    def __init__(self, task_name):
        self.task_name = task_name
        self.url = "https://calms.pythonanywhere.com/reporter/attempt/"
    
    def checking(self, tg_username, isSolved, homework_name):
        data = {
            "tg_username": tg_username,
            "assignment_name": homework_name,
            "task_name": self.task_name,
            "is_correct": isSolved
        }
        response = requests.post(self.url, data=data)
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)
    

class TaskOne(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution() == 0
    
    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution)
        self.checking(tg_username, isSolve, self.homework_name)

class TaskTwo(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution() == "Hello, World"

    def test_case_2(self, solution):
        return type(solution()) == str
    
    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution) and self.test_case_2(solution)
        self.checking(tg_username, isSolve, self.homework_name)

# return "CODEACADEMY" if solution == "CODEACADEMY"  and type(solution) == str
class TaskThree(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution() == "CODEACADEMY"

    def test_case_2(self, solution):
        return type(solution()) == str
    
    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution) and self.test_case_2(solution)
        self.checking(tg_username, isSolve, self.homework_name)


# Return the value integer type, if type(solution) == int
class TaskFour(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return type(solution()) == int

    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution)
        self.checking(tg_username, isSolve, self.homework_name)

# Return the value float type. if type(solution) == float
class TaskFive(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return type(solution()) == float

    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution)
        self.checking(tg_username, isSolve, self.homework_name)

# Return the value str type. if type(solution) == str
class TaskSix(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return type(solution()) == str

    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution)
        self.checking(tg_username, isSolve, self.homework_name)

# Create function arguments a. Return the value a. 
class TaskSeven(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(1) == 1
    
    def test_case_2(self, solution):
        return solution(-.25) == -.25
    
    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution) and self.test_case_2(solution)
        self.checking(tg_username, isSolve, self.homework_name)

# Create function arguments a. Increase the value of a to one and return.
class TaskEight(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution(1) == 2
    
    def test_case_2(self, solution):
        return solution(-.25) == .75
    
    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution) and self.test_case_2(solution)
        self.checking(tg_username, isSolve, self.homework_name)

# Create function arguments a. decrease the value of a to one and return
class TaskNine(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution(1) == 0
    
    def test_case_2(self, solution):
        return solution(-.25) == -1.25
    
    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution) and self.test_case_2(solution)
        self.checking(tg_username, isSolve, self.homework_name)

# Create function arguments a. Return the opposite value of a.
class TaskTen(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution(1) == -1
    
    def test_case_2(self, solution):
        return solution(-.25) == .25
    
    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution) and self.test_case_2(solution)
        self.checking(tg_username, isSolve, self.homework_name)

q1 = TaskOne("basic_func01", "basic_function")
q2 = TaskTwo("basic_func02", "basic_function")
q3 = TaskThree("basic_func03", "basic_function")
q4 = TaskFour("basic_func04", "basic_function")
q5 = TaskFive("basic_func05", "basic_function")
q6 = TaskSix("basic_func06", "basic_function")
q7 = TaskSeven("basic_func07", "basic_function")
q8 = TaskEight("basic_func08", "basic_function")
q9 = TaskNine("basic_func09", "basic_function")
q10 = TaskTen("basic_func10", "basic_function")

# def main1():
#     return 1

# q0.check(main1(), "JalilovJavohir")