from dbconn import DatabaseController
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
DB = DatabaseController()
DB.DBconn()

@app.route('/', methods=['GET','POST'])
def showindexpage() :
    DB.cursor.execute("SELECT * FROM Py_Cars ORDER BY Car_MaxSpeed DESC")
    mydata = DB.cursor.fetchall()

    Car_ID = None
    if request.method == 'POST' :
        if request.form['Delete'] == "Delete car" :
            Car_ID = int(request.form['Car_ID'])
            return render_template("index.html", values = mydata, deletecar = Car_ID)
        elif request.form['Delete'] == "Yes, delete" :
            Car_ID = request.form['Car_ID']
            deleteCar(Car_ID)
            return redirect("/")
    
    return render_template("index.html", values = mydata, deletecar = Car_ID)

@app.route('/create', methods=['GET','POST'])
def showcreatepage() :
    returnMsg = ""
    if request.method == 'POST' :
        if request.form['Create'] == "Create car" :
            try :
                Model = request.form['Model']
                MaxSpeed = request.form['MaxSpeed']
                sql = "INSERT INTO Py_Cars (Car_Model, Car_MaxSpeed) VALUES (%s, %s)"
                val = (Model, MaxSpeed)
                DB.cursor.execute(sql, val)
                DB.connection.commit()
                returnMsg = "Car succesfully added :)"
            except Exception as ex :
                print(ex)
                returnMsg = "Error occured adding the car :("

    return render_template("create.html", returnMsg = returnMsg)

def deleteCar(Car_ID) :
    print("DELETE CAR "+Car_ID)
    sql = "DELETE FROM Py_Cars WHERE Car_ID='"+Car_ID+"'"
    DB.cursor.execute(sql)
    DB.connection.commit()

if __name__ == '__main__' :
    app.run('localhost', 4449)