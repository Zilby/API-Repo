#Must manually install pytumblr with pip install

from flask import Flask, render_template , request , url_for, g, flash, redirect
import json, pytumblr

search=""
data={}

app = Flask(__name__)
client = pytumblr.TumblrRestClient('MSMhEiEKpmPQJtJvRUbaQlWgKoWacSP7GtmocqVZqS4UXL7TmB')

@app.route("/", methods=['GET','POST'])
def home():
    global search,data
    if request.method=="POST":
        search = request.form.get("search", None)
        data = client.tagged(search)
        print data
        return redirect(url_for('results'))
    return render_template("home.html")
@app.route("/results")
def results():
    global search,data
    return render_template("results.html",search=search)

    
if __name__ == "__main__":
    app.debug=True
    app.run(host="127.0.0.1",port=5678)

#search for results using this
#client.tagged("example")

#outputs html code with links to many tagged images
#will have several copies of each image all in different sizes
#must check if the images are the same using regex or grab
#individually using dictionaries
#https://api.tumblr.com/console/calls/tag/tagged
