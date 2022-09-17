from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


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
