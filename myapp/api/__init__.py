from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@172.18.0.2:3306/CURSOS"
#app.config["SQLALCHEMY_DATABASE_URI"] = "jdbc:mysql://172.18.0.2:3306/CURSOS"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def aloMundo():
    return 'Escrevendo uma APII !!'