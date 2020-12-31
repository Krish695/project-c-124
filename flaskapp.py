from flask import Flask, jsonify,request 
app=Flask(__name__)
List=[
    {
        'id':1,
        'Name':u'Hello',
        'contact':u'100234',
        'done':False
    },
    {
        'id':2,
        'Name':u'Bye',
        'contact':u'110234',
        'done':False
    }
]

@app.route("/")
def hello_world():
    return "hello world"
@app.route("/add-data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)

    contact={
        'id':task[-1]['id'][+1],
        'Name':request.json['Name'],
        'contact':request.json.get("contact"),
        'done':False
    }

    List.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added successfuly"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":List
    })
if (__name__=="__main__"):
    app.run(debug=True)
        