from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

#print(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')

'''
@app.route("/works.html")
def work():
    return render_template('works.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')


@app.route("/components.html")
def components():
    return render_template('components.html')
'''

#---Note: Can do the following instead of copy, past modify for each page:

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# @app.route("/blog")
# def blog():
#     return "Welcome to my blog :("


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     return "Form submitted!"


# def write_to_txt(data):
#     with open('database.txt', mode='a') as db:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = db.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            #write_to_db(data)
            write_to_csv(data)
            return redirect("/thanks.html")
        except:
            return "Something went wrong. Did not save to database."