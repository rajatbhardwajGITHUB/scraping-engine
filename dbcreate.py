from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lucifer123#321@127.0.0.1/flaskapp'
db = SQLAlchemy(app)

class python_table(db.Model):
    __tablename__ = 'python_table'
    id = db.Column('id', db.Integer, primary_key=True, nullable = False)
    topic = db.Column('topic',db.Text(20), nullable = False)
    link = db.Column('link', db.Text(150), nullable = False)
    pdf = db.Column('pdf', db.Text(150), nullable = False)

    def __init__(self, topic, link, pdf):
        
        self.topic = topic
        self.link = link
        self.pdf = pdf



class java_table(db.Model):
    __tablename__= 'java_table'
    id = db.Column('id', db.Integer, primary_key=True, nullable = False)
    topic = db.Column('topic',db.Text(20), nullable = False)
    link= db.Column('link', db.Text(150), nullable = False)
    pdf = db.Column('pdf', db.Text(150), nullable = False)

    def __init__(self,  topic, link, pdf):
        
        self.topic = topic
        self.link = link
        self.pdf  = pdf



class js_table(db.Model):
    __tablename__= 'js_table'
    id = db.Column('id', db.Integer, primary_key=True, nullable = False)
    topic = db.Column('topic',db.Text(20), nullable = False)
    link = db.Column('link', db.Text(150), nullable = False)
    pdf = db.Column('pdf', db.Text(150), nullable = False)

    def __init__(self, topic_3, link_3, pdf_3):
        
        self.topic = topic
        self.link = link
        self.pdf = pdf

if __name__ == "__main__":
    app.run(debug=True)
