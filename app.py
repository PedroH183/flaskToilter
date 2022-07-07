from flask import Flask

app = Flask(__name__)

@app.route("/") #definindo a rota do site 
 
def index():
    return "Hello World"

if __name__ == "__main__": # 
    app.run()
