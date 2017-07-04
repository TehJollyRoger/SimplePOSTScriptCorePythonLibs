import urllib, urllib.request


url = "URL"
postVars = { "postVar":postData }
params = urllib.urlencode(data)
req = urllib2.Request(url, data=params)
handle = urllib2.urlopen(req)
page = handle.read()
print(page)
