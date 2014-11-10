from flask import Flask, render_template , request , url_for, g, flash, redirect

app = Flask(__name__)

@app.route("/")
def home():
  if request.method=="POST":
    search = request.form.get("search", None)
    data = client.tagged(search)
    return render_template("home.html")
  return render_template("home.html")

if __name__ == "__main__":
  app.debug=True
  app.run(host="127.0.0.1",port=5678)
    
client = pytumblr.TumblrRestClient('MSMhEiEKpmPQJtJvRUbaQlWgKoWacSP7GtmocqVZqS4UXL7TmB')

#search for results using this
#client.tagged("example")

#outputs html code with links to many tagged images
#will have several copies of each image all in different sizes
#must check if the images are the same using regex or grab
#individually using dictionaries
#https://api.tumblr.com/console/calls/tag/tagged
