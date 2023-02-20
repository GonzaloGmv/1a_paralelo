from multiprocessing import Pool
from scrape import scrape

urls = ["a.com", "b.com", "c.com", "d.com"]

def multiproceso():
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()    
    print()
    for row in data:
        print(row)