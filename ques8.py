class Employee:
    def __init__(self):
        self.employee_id=""
        self.first_name=""
        self.last_name=""
        self.department=""
        self.role=""
        self.city=""
        self.salary_inr= 0
        self.scores = []

    def add_score(self,score):
        if score in range(0,101):
            self.scores.append(score)

    def average_score(self):
        if len(self.scores) == 0:
            return "N/A"
        else:
            return sum(self.scores)/len(self.scores)
        
    def add_salary(self,salary):
        if salary<0:
            self.salary_inr = 0
        else:
            self.salary_inr = salary

    def display_scores(self):
        score_str = str(self.scores[-1])
        for score_index in range(len(self.scores)-1,0,-1):
            score_str = str(self.scores[score_index-1])+", "+score_str
        return(score_str)

    def showEmpDetails(self):
        score = self.display_scores()
        avg_score = self.average_score()
        return(f"{self.employee_id} | {self.first_name} {self.last_name} | Dept = {self.department} | Role = {self.role} | City = {self.city} | Scores = {score} | Avg = {int(avg_score)} | Salary = {self.salary_inr}")
        

def main():
    e1 = Employee()
    e2 = Employee()
    e3 = Employee()

    e1.employee_id = "E1"
    e1.first_name = "Ashutosh"
    e1.last_name = "Rai"
    e1.department = "Customer Experience"
    e1.role = "TCE"
    e1.city = "Bangalore"
    e1.add_salary(38000)
    e1.add_score(23)
    e1.add_score(150)
    e1.add_score(-23)
    e1.add_score(45)
    e1.add_score(78)

    e2.employee_id = "E2"
    e2.first_name = "Gaurav"
    e2.last_name = "Rai"
    e2.department = "Development"
    e2.role = "DevOps"
    e2.city = "Bangalore"
    e2.add_salary(38000)
    e2.add_score(45)
    e2.add_score(32)
    e2.add_score(78)

    e3.employee_id = "E3"
    e3.first_name = "Aryan"
    e3.last_name = "Talukar"
    e3.department = "Customer Development"
    e3.role = "Customer Experience"
    e3.city = "Bangalore"
    e3.add_salary(33500)
    e3.add_score(57)
    e3.add_score(87)
    e3.add_score(29)

    print(e1.showEmpDetails())
    print(e2.showEmpDetails())
    print(e3.showEmpDetails())
    with open("employees_report.txt","w") as empObj:
        empObj.write(e1.showEmpDetails()+"\n")
        empObj.write(e2.showEmpDetails()+"\n")
        empObj.write(e3.showEmpDetails()+"\n")

if __name__ == "__main__":
    main()