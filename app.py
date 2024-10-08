# from flask import Flask

# app = Flask(__name__)
# app.config['TESTING'] = True 

# @app.route("/")
# def hello_world():
#     return "<p>Hello, !</p>"

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
