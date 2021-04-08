from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def matricCode():
    return render_template('index.html')

@app.route('/save')
def save():
    text = request.args.get('text', '')
    file = open("templates/text.txt","a")
    file.write(text+"\n")
    return matricCode()

@app.route('/load')
def load():
    file = open("templates/text.txt","r")
    loaded_text = file.read()
    return render_template('index.html', loaded_text = loaded_text)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port ='5150')