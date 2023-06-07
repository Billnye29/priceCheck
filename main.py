import concurrent.futures
import time
import selenium


# Prints out thread_id and the name of product that thread is assigned to look for.
# Executes product_searcher.py to search for the product
# product_searcher.py returns a file with product information.
# Returned file will be named after the product being searched for and searched date.
def launch_price_check(product_name, thread_id):
    print("Thread ID: ")
    print(thread_id)
    print("Launching checker for: " + product_name)


# File should be formatted as shown.
# item_Name
# item_Name should be a string with the least amount of words possible to describe the item.
# For instance the product: "LEGO - Star Wars 501st Clone Troopers Battle Pack 75345".
# Should be simplified to "501st Clone Troopers Battle Pack".
# There should only be one product perline in the "items.txt" file.
def file_io():
    it_count = 0
    thread_id = 0
    fin = open("items.txt", 'r')
    line = fin.readlines()
    for line in line:
        it_count += 1
    fin.close()
    print(it_count)
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=it_count)

    fin = open("items.txt", 'r')
    line = fin.readlines()
    for line in line:
        pool.submit(lambda arg, arg_2: launch_price_check(arg, arg_2), line, thread_id)
        thread_id += 1

    fin.close()
    pool.shutdown(wait=True)


file_io()
