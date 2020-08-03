from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 
import os 
app = Flask(__name__) 
caminho = os.path.dirname(os.path.abspath(__file__)) # sugestao do Kaue
arquivobd = os.path.join(caminho, "plantas.db") 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+arquivobd 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings 
db = SQLAlchemy(app)