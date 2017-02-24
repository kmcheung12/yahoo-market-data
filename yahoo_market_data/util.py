from urllib.request import Request, urlopen
def curl(url):
    req = Request(url)
    res = urlopen(req)
    return res.read().decode().strip()
