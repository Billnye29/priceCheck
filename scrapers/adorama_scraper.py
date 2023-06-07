# Start function for the website scraper.
# This function will create and format files for the main thread to ingest and output.
# Each function will create a file and format it as such.
# File name will equal: product_name_store_date
# File format:
# First line:  name of store and product name
# Second Line and below: Price of product and link to buy the product
#
# File is capped to linking four product listings
# If the product doesn't exist on the site do not generate file.
# To check if the product exists look for an error message like "We were not able to find a match."
def start(product_name):
    print("Looking for " + product_name + " in " + " Adorama")
