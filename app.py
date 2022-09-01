import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgP8WlAzYzRsixdQlZf_Gyb7GFRRQ-LpLN67QeuqnELpwjvOmeXWZXOw6-Kjuj3ejCAwP8ePszd6tbwX3CsThGmZN8Vft5LmoQr5p8Cx4gGMktXYJpX8qUeHnfexcTj-3OeJSf9cCxYkuylMrirw1REh3ZAy8dMqsmPWjg3Vstvwe_Qu3m-73dRinFVRw/s16000/coming%20soon.png", code=302)

if __name__ == '__main__':
    app.run()