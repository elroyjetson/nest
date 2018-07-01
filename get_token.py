import http.client,yaml

conf = yaml.load(open("secrets"))

pin_code = conf['pin_code']
client_id = conf['client_id']
client_secret = conf['client_secret']

conn = http.client.HTTPSConnection("api.home.nest.com")

payload = "code=" + pin_code + "&client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=authorization_code"

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "/oauth2/access_token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

