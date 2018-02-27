from flask import Flask, render_template, request
from stuff import *

app = Flask(__name__)

def change(data):
    owner_name = "Owner Display Name: " + data["owner"]["displayName"] + "<br><br>"
    name = "Complaint Name: " + data["name"] + "<br>"
    descrip = "Description: " + data["description"]
    descrip.replace("\u2019", "'")
    return name + owner_name + descrip

@app.route("/", methods=['GET','POST'])
def root():
    if (request.method == 'GET'):
        setup()
        get_names()
        options = get_names()
        return render_template("select.html", options = options)
    else:
        name = request.form["name"]
        info = change(query_name(name)[0])
        return render_template("select.html", info = info)

    
if __name__ == '__main__':
    app.debug = True
    app.run()
