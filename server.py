from flask import Flask
import random 

app = Flask(__name__)

@app.route('/')
def index():
    return 'random : <strong>' + str(random.random()) + '</strong>'

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/') # <> 사이에 이름을 지정하고 이를 파라미터로 하면, 동적으로 가능 
def read(id):
    print(id)
    return 'Read '+id

app.run(port=5001, debug=True) # 디버깅 모드로 플라스크 실행 # 서버를 재부팅하지 않아도, 자동으로 서버가 재부팅됨.