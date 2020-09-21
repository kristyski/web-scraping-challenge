# Declare Dependencies 
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd


# Choose the executable path to driver, for Windows specifically; from activity 12-01-05
executable_path = {"executable_path": "../../MyForkOfRepo/chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# NASA Mars News

# Visit NASA news url through splinter module; activity 12-01-01, 02, 03, 05, 07
url = "https://mars.nasa.gov/news/"
browser.visit(url)

# HTML object
html = browser.html

# use bs to write to html
soup = bs(html, "html.parser")


# inspect mars.nasa.gov to determine class text for title and paragraph;
# retrieve latest element that contains news title and news paragraph; activity 12-01-04, 05
news_title = soup.find("div",class_="content_title").text
news_p = soup.find("div", class_="article_teaser_body").text

# Display scrapped info 
print(news_title)
print(news_p)


# JPL Mars Space Images - Featured Image

# Visit Mars Space Images through splinter module
mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(mars_image_url)

# HTML Object 
html_image = browser.html

# Parse HTML with Beautiful Soup
soup = bs(html_image, "html.parser")

# Retrieve background image url from style tag 
featured_image_url  = soup.find("article")["style"].replace("background-image: url(","").replace(");", "")[1:-1]

# Website Url 
main_url = "https://www.jpl.nasa.gov"

# Concatenate website url with scrapped route
featured_image_url = main_url + featured_image_url

# Display full link to featured image
featured_image_url


# Mars Facts

# Visit Mars facts url; using activity 12-01-07
facts_url = "http://space-facts.com/mars/"

# Use Pandas to read/parse the url
mars_facts = pd.read_html(facts_url)

# take mars_facts DataFrame and assign to mars_df
mars_df = mars_facts[0]

# Assign columns
mars_df.columns = ["Title","Info"]

# Set the index to the `Title` column
mars_df.set_index("Title", inplace=True)
# mars_df

# Save html code
mars_df.to_html()


# Mars Hemispheres

# Visit hemispheres website through splinter module 
hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)

html_hemispheres = browser.html

# Parse HTML with Beautiful Soup
soup = bs(html_hemispheres, "html.parser")

# Retreive all items that contain mars hemispheres information
items = soup.find_all("div", class_="item")

# Create empty list for hemisphere urls 
hemisphere_image_urls = []

# Store the main_ul 
hemispheres_main_url = "https://astrogeology.usgs.gov"

# Loop through the items previously stored
for i in items: 
    # Store title
    title = i.find("h3").text
    
    # Store link that leads to full image website; use inspect web page for class
    partial_img_url = i.find("a", class_="itemLink product-item")["href"]
    
    # Visit the link that contains the full image website 
    browser.visit(hemispheres_main_url + partial_img_url)
    
    # HTML Object of individual hemisphere information 
    partial_img_html = browser.html
    
    # Parse HTML with Beautiful Soup for each hemisphere 
    soup = bs(partial_img_html, "html.parser")
    
    # Retrieve full image source; click thumbnail, inspect page for class
    img_url = hemispheres_main_url + soup.find("img", class_="wide-image")["src"]
    
    # Append the retreived information into a list of dictionaries 
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    

# Display hemisphere_image_urls
hemisphere_image_urls