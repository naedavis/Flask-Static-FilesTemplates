#Add a route called times and accept a variable called number
# The program should now do a multiplication table up to 10 based on the number that you have accepted
# Hint. You will need a for loop statement and the loop is terminated by {%endfor%} statement.
# Display the following dictionary details on homepage:
# student_ages= {"Naeemah": 25, "godwin": 26, "Thapelo": 47, "Jason": 23}. Display the records in a table with the following headings Student_name, Student_Age

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    # Dictionary that holds all the values to be displayed in the table
    student_ages = {"Naeemah": 25, "godwin": 26, "Thapelo": 47, "Jason": 23}
    return render_template('homepage.html', students=student_ages)

@app.route('/loop/<int:number>')
def loop(number):
    return render_template('numberspage.html', number=number)


if __name__ == "__main__":
    app.debug = True
    app.run()
