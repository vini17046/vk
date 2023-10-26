from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

   # MongoDB Configuration
client = MongoClient("mongodb://localhost:27017/")
db = client.mydb
form_data_collection = db.form_data

@app.route('/')
def index():
       return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
       name = request.form['name']
       email = request.form['email']
       form_data_collection.insert_one({"name": name, "email": email})
       return redirect('/')

if __name__ == '__main__':
       app.run(debug=True)