from scrape import scrape

urls = ["a.com", "b.com", "c.com", "d.com"]
output = []
for url in urls:
    result = scrape(url)
    output.append(result)