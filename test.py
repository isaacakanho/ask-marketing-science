from flask import Flask, request, render_template
import csv

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':

        dt = [['the_question 1', 'the_answer 1'], ['the_question 2', 'the_answer 2'],
              ['the_question 3', 'the_answer 3'], ['the_question 4', 'the_answer 4']]

        return render_template("index.html", dt=dt)

    elif request.method =='POST':
        question = request.form['question']
        with open("test_data.csv", "ab") as test_data:
            data_writer = csv.writer(test_data, delimiter=",", dialect="excel")
            test_data.flush()
            data_writer.writerow([question])
        print question
        #return question
        return render_template("question.html", question=question)
@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
