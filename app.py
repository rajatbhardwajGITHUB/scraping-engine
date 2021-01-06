from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lucifer123#321@127.0.0.1/flaskapp'
db = SQLAlchemy(app)

class exam(db.Model):  #model for emails
    __tablename__ = 'cred' 
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.Text)

    def __init__(self,  email):
        self.email = email


@app.route('/home', methods=['GET','POST'])
def home():

    if request.method == 'POST':
       email = request.form.get("email")
       print(email)
       em = exam(email) #object for storing emails
       db.session.add(em)
       db.session.commit()

    return render_template('index.html')
  

@app.route('/home/resources/v1/pages/courses/cs', methods=['GET', 'POST'])
def courses():
    return render_template('courses.html')

@app.route('/home/resources/v1/pages/courses/marketing', methods=['GET', 'POST'])
def market():
    return render_template('marketing.html')

@app.route('/home/resources/v1/pages/courses/medical', methods=['GET', 'POST'])
def medical():
    return render_template('medical.html')

@app.route('/home/resources/v1/pages/links/youltube_links', methods=['GET', 'POST'])
def links():
    return render_template('you_links.html')

@app.route('/home/resources/v1/pages/links/pdfs', methods=['GET', 'POST'])
def pdf():
    return render_template('pdfs.html')


if __name__  == '__main__':
    app.run(debug=True)