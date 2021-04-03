# Python BMI Calc with Flask
# import Flask and request libraries
# render_template: renders the html templates or pages
# is returned in our function

from flask import Flask, request, render_template

app = Flask(__name__)  # flask instance

"""
@app.route('/')
Runs on local server at http://127.0.0.1:5000/

@app.route('/janets')
Runs on local server at http://127.0.0.1:5000/janets 

Directory/file structure
------------------------
PythonFlask>                'project folder'
        static>             'CSS, images & other files stored in this folder'
            style.css
            my.mp3
            my_pic.jpg
        templates>          'HTML web pages stored in this folder
            homepage.html
            page1.html
            page2.html
        venv>               'PyCharm virtual environment
        app.py              'Our web app'
            
"""


@app.route('/', methods=['POST', 'GET'])
def root_page():
    name = ''
    kg = ''  # weight
    m = ''   # height
    bmi = 0
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        kg = request.form.get('user_kg')
        m = request.form.get('user_m')
        bmi = round(float(kg)/float(m)**2)
        # inputs are string, so convert to float
    return render_template("index.html", name=name, kg=kg, m=m, bmi=bmi)


app.run()

"""
BMI = kg / m**2
"""