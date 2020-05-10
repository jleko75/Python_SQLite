import sqlite3
from employee import Employee

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# budući baza podataka već postoji ovo nam ne treba
# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#             )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

# način na koji unosimo podatke u tablicu
c.execute("INSERT INTO employees VALUES ('Jozo', 'Leko', 60000)")

# način na koji selektiramo podatke iz tablice
c.execute("SELECT * FROM employees WHERE last='Leko'")
print(c.fetchone())



def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
emp_3 = Employee('Mirela', 'Doe', 80000)
emp_4 = Employee('Klara', 'Doe', 75000)
emp_5 = Employee('Ema', 'Doe', 85000)
emp_6 = Employee('Ante', 'Leko', 95000)

# insert_emp(emp_1)
# insert_emp(emp_2)
# insert_emp(emp_3)
# insert_emp(emp_4)
# insert_emp(emp_5)
# insert_emp(emp_6)
print(emp_3.first)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)


conn.commit()
conn.close()
