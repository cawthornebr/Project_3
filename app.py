from flask import Flask, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def index():
    print("----------------------")
    print("index called")
    print("----------------------")
    return render_template('index.html')

@app.route("/index1")
def index1():
    print("----------------------")
    print("index called")
    print("----------------------")
    return render_template('index1.html')

@app.route("/ml")
def ml():
    print("----------------------")
    print("ML called")
    print("----------------------")
    return render_template('ML.html')

@app.route("/ml1")
def ml1():
    print("----------------------")
    print("ML called")
    print("----------------------")
    return render_template('ML1.html')

@app.route("/unemployment")
def unemployment():
    print("----------------------")
    print("unemployment called")
    print("----------------------")
    return render_template('unemployment_map.html')

@app.route("/unemployment1")
def unemployment1():
    print("----------------------")
    print("unemployment called")
    print("----------------------")
    return render_template('unemployment_dashboard.html')

@app.route("/other-data")
def otherdata():
    print("----------------------")
    print("other-data called")
    print("----------------------")
    return render_template('other_data.html')

if __name__ == '__main__':
    app.run(debug=True)