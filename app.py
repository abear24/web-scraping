    
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db



@app.route("/")
def home():
mars_data = mars.db.find_one()

    return render_template("index.html", mars=mars_Data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars_data = scrape_mars.scrape()

      mars.db.update({}, mars_data, upsert=True)
      
    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)