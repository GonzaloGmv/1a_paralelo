from scrape import scrape

urls = ["a.com", "b.com", "c.com", "d.com"]

def secuencial():
    output = []
    for url in urls:
        result = scrape(url)
        output.append(result)
    print('\n')
    for i in output:
        print(i)