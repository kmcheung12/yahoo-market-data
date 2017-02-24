from urllib.request import Request, urlopen
from urllib.parse import urlencode
import io
import csv
from bs4 import BeautifulSoup
from . import util

class Symbols:
    URLS = {
        "nasdaq": "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download",
        "nyse": "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download",
        "amex": "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download",
        "hkgem": "http://www.hkexnews.hk/hyperlink/hyperlist_gem.htm",
        "hkex": "http://www.hkexnews.hk/hyperlink/hyperlist.htm"
            }

    @staticmethod
    def curl(key):
        url = Symbols.URLS[key]
        return util.curl(url)

    @staticmethod
    def to_csv_reader(s):
        f = io.StringIO(s)
        return csv.reader(f, delimiter=',')

    @staticmethod
    def nasdaq():
        content = Symbols.curl("nasdaq")
        reader = Symbols.to_csv_reader(content)
        next(reader) # discard header row
        return [row[0] for row in reader]

    @staticmethod
    def nyse():
        content = Symbols.curl("nyse")
        reader = Symbols.to_csv_reader(content)
        next(reader) # discard header row
        return [row[0] for row in reader]
    
    @staticmethod
    def amex():
        content = Symbols.curl("amex")
        reader = Symbols.to_csv_reader(content)
        next(reader) # discard header row
        return [row[0] for row in reader]

    @staticmethod
    def hkex():
        content = Symbols.curl("hkex")
        soup = BeautifulSoup(content, 'lxml')
        return [tr.find_all('td')[0].text.strip() + '.HK' for tr in soup.tbody.tbody.find_all('tr')][1:]

    @staticmethod
    def hkgem():
        content = Symbols.curl("hkgem")
        soup = BeautifulSoup(content, 'lxml')
        return [tr.find_all('td')[0].text.strip() + '.HK' for tr in soup.tbody.find_all('tr')][1:]
