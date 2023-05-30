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
        return solution == 0
    
    def check(self,solution, tg_username):
        isSolve = self.test_case_1(solution)
        self.checking(tg_username, isSolve, self.homework_name)


q0 = TaskOne("basic_func01", "basic_function")