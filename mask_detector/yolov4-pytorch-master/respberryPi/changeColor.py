import urllib.request
import urllib.parse

url = "localhost:8888/"

def changeLightsColor(color):
    color = {
        'mask' : color
    }
    postData = urllib.parse.urlencode(color).encode("utf-8")
    req = urllib.request.Request(url, postData)
    req.add_header( "User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36")
    response = urllib.request.urlopen(req)
    print(response.read().decode("utf-8"))