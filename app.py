from getData.getUser import dataDictionary
from getData.automatically import azureDictionary
from turtle import title
from flask import Flask, render_template, request, request_started
from flask_sqlalchemy import SQLAlchemy
import os
from getData.getUser import dataDictionary
from getData.automatically import azureDictionary

app = Flask(__name__)

# -------- FORM ---------
app.secret_key = 'replace later'

# ------ DOCUMENTATION CODE -------
ENVIROMENT = "dev"

db_user = os.environ.get('DB_USER_PSQL')
db_password = os.environ.get('DB_PASSWORD_PSQL')
fullCredentials = f"postgresql://{db_user}:{db_password}@localhost/inventory2"

if ENVIROMENT == "dev":
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = fullCredentials

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class MyModel(db.Model):
    __tablename__ = 'modelInventory'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200), unique=True)
    brand = db.Column(db.String(200))
    model = db.Column(db.String(200))
    serialNumber = db.Column(db.String(200), unique=True)
    ram = db.Column(db.Float)
    operatingSystem = db.Column(db.String(200))
    licence = db.Column(db.String(200))
    azureAdJoined = db.Column(db.String(200))
    azureAdPrt = db.Column(db.String(200))
    isDeviceJoined = db.Column(db.String(200))
    isUserAzureAD = db.Column(db.String(200))
    macAddress = db.Column(db.String(200), unique=True)

    def __init__(self, user, brand, model, serialNumber, ram, operatingSystem, licence, azureAdJoined, azureAdPrt, isDeviceJoined, isUserAzureAD, macAddress):
        self.user = user
        self.brand = brand
        self.model = model
        self.serialNumber = serialNumber
        self.ram = ram
        self.operatingSystem = operatingSystem
        self.licence = licence
        self.azureAdJoined = azureAdJoined
        self.azureAdPrt = azureAdPrt
        self.isDeviceJoined = isDeviceJoined
        self.isUserAzureAD = isUserAzureAD
        self.macAddress = macAddress


@app.route("/")
def home_page():
    return render_template("index.html", title="Home", data=dataDictionary,
                           azureData=azureDictionary)


@app.route('/form')
def myForm():
    return render_template('myForm.html', title="Form", data=dataDictionary,
                           azureData=azureDictionary)


# ________________________________________________


@app.route('/toying')
def myBase():
    return render_template('toyBase.html', title="Toying section")


@app.route('/form2')
def myData():
    return render_template('toyForm.html', title="Toying Form")

# __________________________________________________________


@app.route("/automate", methods=['POST', 'GET'])
def automatically_page():

    if request.method == 'GET':
        render_template("automate.html", title="Automate", data=dataDictionary,
                        azureData=azureDictionary)

    elif request.method == 'POST':
        if request.form['send'] == "sending_data":
            user = dataDictionary.username
            brand = dataDictionary.brand
            model = dataDictionary.model
            serialNumber = dataDictionary.serialNumber
            ram = dataDictionary.ram
            operatingSystem = dataDictionary.operatingSystem
            licence = dataDictionary.licence

            azureAdJoined = azureDictionary.AzureAdJoined
            azureAdPrt = azureDictionary.AzureAdPrt
            isDeviceJoined = azureDictionary.IsDeviceJoined
            isUserAzureAD = azureDictionary.IsUserAzureAD
            macAddress = azureDictionary.macAddress

            if db.session.query(MyModel).filter(MyModel.user == user).count() == 0:
                data = MyModel(user, brand, model, serialNumber, ram, operatingSystem, licence,
                               azureAdJoined, azureAdPrt, isDeviceJoined, isUserAzureAD, macAddress)
                db.session.add(data)
                db.session.commit()
                return render_template("automate.html", title="Automate", data=dataDictionary,
                                       azureData=azureDictionary)
    return render_template("automate.html", title="Automate", data=dataDictionary,
                           azureData=azureDictionary)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route("/exit")
def exit_page():
    return render_template("exit.html", title="Exit")


@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        brand = request.form['brand']
        model = request.form['model']
        serialNumber = request.form['serialNumber']
        ram = request.form['ram']
        operatingSystem = request.form['operatingSystem']
        licence = request.form['licence']
        azureAdJoined = request.form['azureAdJoined']
        azureAdPrt = request.form['azureAdPrt']
        isDeviceJoined = request.form['isDeviceJoined']
        isUserAzureAD = request.form['isUserAzureAD']
        macAddress = request.form['macAddress']
        print(user, brand, model, serialNumber, ram, operatingSystem, licence,
              azureAdJoined, azureAdPrt, isDeviceJoined, isUserAzureAD, macAddress)
        inputtList = [user, brand, model, serialNumber, ram, operatingSystem, licence,
                      azureAdJoined, azureAdPrt, isDeviceJoined, isUserAzureAD, macAddress]
        for oneInput in inputtList:
            if oneInput == '':
                return render_template('index.html', message='Please enter requiered info')
        if db.session.query(MyModel).filter(MyModel.user == user).count() == 0:
            data = MyModel(user, brand, model, serialNumber, ram, operatingSystem, licence,
                           azureAdJoined, azureAdPrt, isDeviceJoined, isUserAzureAD, macAddress)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        return render_template('success.html', message='You have already Submitted')


if __name__ == "__main__":
    app.run()
