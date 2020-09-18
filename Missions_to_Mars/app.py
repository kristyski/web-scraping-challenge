from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    
    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scrape():
    mars_info = mongo.db.mars_info
    mars_info = scrape_mars.scrape_mars_news()
    # ?
    mars_info.update({}, mars_data, upsert=True)
    
    return redirect(url_for("index"), code=302)


if __name__ == "__main__":
    app.run(debug=True)
