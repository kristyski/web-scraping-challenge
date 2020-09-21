# Step 2 - MongoDB and Flask Application
# look in activity 12 03 01-07

# import necessary libraries
# and pymongo library, which connects Flask app to our Mongo database.
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection, from activity 12-03-09
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    
    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scrape():
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape_all()
    mars_info.update({}, mars_data, upsert=True)
    
    # return redirect(url_for("index"), code=302)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)