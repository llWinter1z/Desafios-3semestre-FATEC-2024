from flask import Flask
from flask import render_template

app = Flask("__name__")

@app.route("/")
def sobremim ():
    return render_template ('sobremim.html')

@app.route("/sobremim.html")
def sobremim2 ():
    return render_template ('sobremim.html')

@app.route("/artes.html")
def artes ():
    return render_template ('artes.html')

if __name__ == '__main__':
    app.run(debug=True)