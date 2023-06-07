import scrapers.adorama_scraper as adorama
import scrapers.amazon_scraper as amazon
import scrapers.b_h_scraper as b_h
import scrapers.best_buy_scraper as best_buy
import scrapers.cosco_scraper as cosco
import scrapers.new_egg_scraper as egg
import scrapers.sams_club_scraper as sam
import scrapers.target_scraper as target
import scrapers.toys_r_us_scraper as toy
import scrapers.walmart_scraper as walmart
import concurrent.futures
import time


def begin_search(product_name):
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    pool.submit(lambda arg: adorama.start(arg), product_name)
    pool.submit(lambda arg: amazon.start(arg), product_name)
    pool.submit(lambda arg: b_h.start(arg), product_name)
    pool.submit(lambda arg: best_buy.start(arg), product_name)
    pool.submit(lambda arg: cosco.start(arg), product_name)
    pool.submit(lambda arg: egg.start(arg), product_name)
    pool.submit(lambda arg: sam.start(arg), product_name)
    pool.submit(lambda arg: target.start(arg), product_name)
    pool.submit(lambda arg: toy.start(arg), product_name)
    pool.submit(lambda arg: walmart.start(arg), product_name)







