from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/s1")
def view1():

    
    return render_template("story1.html")


if __name__=="__main__":
    app.run(debug=True)