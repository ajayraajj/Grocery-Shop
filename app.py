from flask import Flask, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Define the database engine
engine = create_engine("mysql+pymysql://sql6693232:yDntHLHaqy@sql6.freesqldatabase.com/sql6693232?charset=utf8mb4")

# Function to load employees from the database
def loadEmployeesFromDb():
  with engine.connect() as conn:
      result = conn.execute(
          text("SELECT id, name, salary, department, gender, hireDate, address, email, phone, birthDate, EmployeePhoto FROM employees"))
      employees = []
      for row in result:
          employee_dict = {
              "id": row[0],
              "name": row[1],
              "salary": float(row[2]),
              "department": row[3],
              "gender": row[4],
              "hireDate": str(row[5]),
              "address": row[6],
              "email": row[7],
              "phone": row[8],
              "birth_date": str(row[9]),
              "EmployeePhoto": row[10]
          }
          employees.append(employee_dict)
      return employees

# Route for the Home page
@app.route("/Home")
def HomePage():
    return render_template("home.html")

# Route for the Products page
@app.route("/Products")
def ProductPage():
    return render_template("products.html")

# Route for the Employees page
@app.route("/Employees")
def EmployeePage():
    employees = loadEmployeesFromDb()
    return render_template("employees.html", Emp=employees)

# Route for the Feedback page
@app.route("/Feedback")
def FeedbackPage():
    return render_template("feedback.html")

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
