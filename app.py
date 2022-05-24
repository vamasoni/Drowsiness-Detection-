from flask import Flask, render_template, request
from index import d_dtcn

app= Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("test1.html")
    else:
        # pass # unknown
        return render_template("index.html")

@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            d_dtcn()
            return render_template("index.html")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)