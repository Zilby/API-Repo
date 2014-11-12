#Must manually install pytumblr with pip install

from flask import Flask, render_template , request , url_for, g, flash, redirect
import json, pytumblr, time

search=""
data=[]

app = Flask(__name__)
client = pytumblr.TumblrRestClient('MSMhEiEKpmPQJtJvRUbaQlWgKoWacSP7GtmocqVZqS4UXL7TmB')

@app.route("/", methods=['GET','POST'])
def home():
    global search,data
    if request.method=="POST":
        search = request.form.get("search", None)
        dic = client.tagged(search,before=time.time())
        #cannot set limit higher, or change offset with tumblr's api
        #however, one can change the timestamp of the posts
        dic=dic+client.tagged(search,before=time.time()-100000)
        dic=dic+client.tagged(search,before=time.time()-200000)
        dic=dic+client.tagged(search,before=time.time()-300000)
        dic=dic+client.tagged(search,before=time.time()-400000)
        print len(dic)
        data=[]
        for each in dic:
            if "photos" in each:
                data.append(each["photos"][0]['original_size']['url'])
        return redirect(url_for('results'))
    return render_template("home.html")

@app.route("/results")
def results():
    global search,data
    l=len(data)
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    count=-1
    for each in data:
        if count<(l/4):
            d1.append(each)
        elif count<(l/2):
            d2.append(each)
        elif count<(l*3/4):
            d3.append(each)
        else:
            d4.append(each)
        count+=1
        """
    print len(d1)
    print len(d2)
    print len(d3)
    print len(d4)
    """
    return render_template("results.html",search=search,d1=d1,d2=d2,d3=d3,d4=d4)

    
if __name__ == "__main__":
    app.debug=True
    app.run(host="127.0.0.1",port=5678)
