from flask import Blueprint, session, request, render_template, redirect, url_for
from employee import model
from db import db

employee_bp= Blueprint("employee", __name__)

@employee_bp.route("/employee", methods=["GET", "POST"])
def employee():
    if request.method == "GET":
         return render_template("employee_create.html")
    elif request.method == "POST":
        form_data = request.form
        name = form_data["name"]
        email = form_data["email"]
        phone = form_data["phone"]
        salary = form_data["salary"]
        hire_date = form_data["hire_date"]
        department = form_data["department"]
        print(name)

        employee = model.employee(name=name, email=email, phone=phone, salary=salary, hire_date=hire_date,department=department)
        db.session.add(employee)
        db.session.commit()

        return "your employee details has been successfully saved"

@employee_bp.route("/employee/create", methods=["GET", "POST"])
def employee_create():
    if request.method == "GET":
        if 'user' in session:

            return render_template("employee_create.html")

    if request.method=="POST":
        if 'user' in session:
            

            form_data = request.form

            name = form_data["name"]
            email = form_data["email"]
            phone = form_data["phone"]
            salary = form_data["salary"]
            hire_date = form_data["hire_date"]
            department = form_data["department"] 
            print(name)
        else :
            return "end" 


@employee_bp.route('/employee/edit/<int:employee_id>', methods=['GET', 'POST'])
def employee_edit(employee_id):
    employee = model.employee.query.get_or_404(employee_id)

    print(employee)

    if request.method == 'POST':
        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.phone = request.form['phone']
        employee.salary = request.form['salary']
        employee.hire_date = request.form['hire_date']
        employee.department = request.form['department']

        db.session.commit()

        return redirect(url_for('employee.employee'))
    else:
        return render_template('edit_employee.html', data=employee)



