from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/')
def homerun():
    return render_template("home.html")

@app.route('/', methods=["GET","POST"]) 
# ADD A GET METHOD TOO.
# As we are both sending data to backend and receiving it back,
# We have to enable both GET and POST Methods.
def index():

    if request.method == "POST":
        note = request.form.get("note")
        # Do not use args, use form instead, get will be as usual.
        notes.append(note)
        return render_template("home.html", notes=notes)
    else :
        return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)

"""
Changes made in HTML FILE:
in form tag, fill action = "/" as the input control 
belongs to home page only.
# and we have to add method = "post", as we are 
# postion our data to the backend.
"""