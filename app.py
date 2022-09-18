from flask import Flask
from bs4 import *
import requests					
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! v1'

@app.route('/math/<string:method>/<string:m>/<string:n')
def math(method,m,n):
    m,n=int(m),int(n)
    if(method == "sum" or method =="add"):
        result = m+n
    elif(method == "mul"):
        result = m*n
    elif(method == "sub"):
        result = m-n
    elif(method=="div"):
        result = m/n
    elif method=="pow":
        result = m**n
    else:
        result = "invaild"
    return str(result)


@app.route('/sum/<string:n>/<string:m>')
def sum(n,m):
    a = int(n)+int(m)
    return str(a)

@app.route('/web/<string:name>')
def web(name):
    from websearch import WebSearch
    web = WebSearch(name)
    return web.pages

@app.route('/web/<string:name>/<string:ext>')
def web_(name,ext):
    from websearch import WebSearch
    web = WebSearch(f"{name} filetype:{ext}")
    return web.pages

@app.route('/wiki/<string:q>')
def wiki(q):
    import wikipedia as wiki
    return wiki.summary(q, sentences =10 )


if __name__ == "__main__" :
    app.run(debug=True)
