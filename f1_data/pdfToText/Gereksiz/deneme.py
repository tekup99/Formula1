import http.client

conn = http.client.HTTPSConnection("ergast.com")
payload = ''
headers = {}
conn.request("GET", "/api/f1/2021/1/laps/1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))