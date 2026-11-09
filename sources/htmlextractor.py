from urllib import request,parse

def HTMLExtractor(url):
    url = str(url)
    if parse.urlparse(url).scheme not in ("http","https"):
        print("Absolute URL only")
    else:
        object = request.Request(
        url,
        headers={
            "User-Agent":"Duck"
        }
    )
        html = request.urlopen(object).read().decode("UTF-8",errors="replace")
        return html

