from flask import Flask, render_template
from db import engine


app = Flask(__name__)


@app.route("/Home")
def HomePage():
    return render_template("home.html")


@app.route("/Products")
def ProductPage():
    return render_template("products.html")


@app.route("/Employees")
def EmployeePage():
    employees = loadEmployeesFromDb()
    return render_template("employees.html", Emp=employees)



@app.route("/Feedback")
def FeedbackPage():
  
      return render_template("feedback.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000, debug=True)

def loadEmployeesFromDb():
  with engine.connect() as conn:
      result = conn.execute(
          text("SELECT id, name, salary, department, gender,                       hire_date, address, email, phone, birth_date,                           EmployeePhoto FROM employees"))
      employees = []
      for row in result:
          employee_dict = {
              "id": row[0],
              "name": row[1],
              "salary": float(row[2]),
              "department": row[3],
              "gender": row[4],
              "hire_date": str(row[5]),
              "address": row[6],
              "email": row[7],
              "phone": row[8],
              "birth_date": str(row[9]),
              "EmployeePhoto": row[10]
          }
          employees.append(employee_dict)
      return employees



