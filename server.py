from flask import Flask
import random 

app = Flask(__name__)

topics = [
    {'id':1, 'title':'html', 'body':'html is ...'},
    {'id':2, 'title':'css', 'body':'css is ...'},
    {'id':3, 'title':'javascript', 'body':'javascript is ...'}
]

def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
            </ul>
        </body>
    </html>
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/read/<int:id>/')
def reader(id):
    print(type(id))
    title=''
    body=''
    for topic in topics:
        if id==topic['id']:
            title = topic['title']
            body = topic['body']
            break
    print(title,body)
    return template(getContents(), f'<h2>{title}</h2>{body}')

@app.route('/create/')
def create():
    content = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
    '''
    return template(getContents(), content)

@app.route('/read/<id>/') # <> 사이에 이름을 지정하고 이를 파라미터로 하면, 동적으로 가능 
def read(id):
    print(id)
    return 'Read '+id

app.run(port=5001, debug=True) # 디버깅 모드로 플라스크 실행 # 서버를 재부팅하지 않아도, 자동으로 서버가 재부팅됨.