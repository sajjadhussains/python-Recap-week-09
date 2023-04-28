# Flask Crud Operations Using Query

from flask import Flask,jsonify,request

app = Flask(__name__)
students=[{"id":1,"name":"Rahim"},{"id":2,"name":"Karim"},{"id":3,"name":"Shafiq"}]

@app.route('/')
def home():
    return jsonify(students)
@app.route('/add',methods=['POST'])
def add():
    students.append(request.get_json())
    print(request.get_json())
    return "Student added successfully",200

@app.route('/update',methods=['PUT'])
def update():
    for student in students:
        if student.get('id') ==request.get_json().get('id'):
            student.update(request.get_json())
    return "Student Updated Successfully",200

@app.route('/delete',methods=['DELETE'])
def delete():
    for i in range(len(students)):
        if str(students[i].get('id'))==request.get_json().get('id'):
            del students[i]
            break
    return "Student Deleted Successfully"

app.run(debug=True)
