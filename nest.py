#!/usr/bin/env python3

import http.client, getopt, sys, json, yaml
from urllib.parse import urlparse

conf = yaml.load(open("secrets"))

url = "developer-api.nest.com"
token = conf['token']
device_id = conf['device_id']

def get_temp():
  resource = "/devices/thermostats/" + device_id + "/ambient_temperature_f"
  conn = http.client.HTTPSConnection("developer-api.nest.com")
  headers = {'authorization': "Bearer {0}".format(token)}
  conn.request("GET", resource, headers=headers)
  response = conn.getresponse()

  if response.status == 307:
      redirectLocation = urlparse(response.getheader("location"))
      conn = http.client.HTTPSConnection(redirectLocation.netloc)
      conn.request("GET", resource, headers=headers)
      response = conn.getresponse()
      if response.status != 200:
          raise Exception("Redirect with non 200 response")

  data = response.read()
  return data.decode("utf-8")

def get_humidity():
  resource = "/devices/thermostats/" + device_id + "/humidity"
  conn = http.client.HTTPSConnection("developer-api.nest.com")
  headers = {'authorization': "Bearer {0}".format(token)}
  conn.request("GET", resource, headers=headers)
  response = conn.getresponse()

  if response.status == 307:
      redirectLocation = urlparse(response.getheader("location"))
      conn = http.client.HTTPSConnection(redirectLocation.netloc)
      conn.request("GET", resource, headers=headers)
      response = conn.getresponse()
      if response.status != 200:
          raise Exception("Redirect with non 200 response")

  data = response.read()
  return data.decode("utf-8")

def get_json():
  temp = get_temp()
  humidity = get_humidity()
  return json.dumps({'temperature': temp, 'humidity': humidity})

def get_help():
  usage = """Usage: nest.py [OPTION]...
  Display current temperature and humidity at the Nest Thermostat

  --help          Display usage
  --json          Return a json string containing both current temperature and humidity
  -t, --temp      Display current temperature
  -h, --humidity  Display current humidity
  """
  print(usage)

def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:],"th", ["temp", "humidity", "json", "help"])
  except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

  for o, a in opts:
    if o in ("-t", "--temp"):
      print(get_temp())
    elif o in ("-h", "--humidity"):
      print(get_humidity())
    elif o == "--json":
      print(get_json())
    elif o == "--help":
      get_help()


if __name__ == "__main__":
  if(len(sys.argv[1:]) < 1):
    get_help()
  else:
    main()

