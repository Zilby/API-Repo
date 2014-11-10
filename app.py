from flask import Flask, render_template , request , url_for

app = Flask(__name__)

@app.route("/")
def mainpage():
  return render_template("home.html")

if __name__ == "__main__":
  app.run(debug=True)

client = pytumblr.TumblrRestClient(
  'MSMhEiEKpmPQJtJvRUbaQlWgKoWacSP7GtmocqVZqS4UXL7TmB',
  'E6cOTcJh2S6B6rzXOYgAR171Q80ST5xus10SnBTjEAKjjQ6tBz',
  'rdayXgngXVTIJnTmlM7hN5m6r9AIgNGXgsJFgEQVXFPSaNek57',
  'v6bxEmKLGYRS7Xicfvfz4INgeVEsi7KmHo169dVT3adCPr5PDk'
)

client.info()
