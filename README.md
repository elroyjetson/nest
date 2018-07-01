# Nest

Get environmental data from a Nest thermostat

## Getting Started

To begin, you have to get a pin from Nest for your device. [Instructions](https://developers.nest.com/documentation/cloud/how-to-auth)
After you have obtained your pin, you need to get an access token. See get_token.py

Once you have an access token, nest.py will allow you to get temperature and humidity readings from your Nest thermostat.

```
Usage: nest.py [OPTION]...
  Display current temperature and humidity at the Nest Thermostat

  --help          Display usage
  --json          Return a json string containing both current temperature and humidity
  -t, --temp      Display current temperature
  -h, --humidity  Display current humidity
```

### Secrets format

The secrets file is a yaml file containing the private authorization information for accessing your thermostat.

```
---
token: [Replace with Access Token]
device_id: [Replace with Device Id]
pin_code: [Replace with Pin Code]
client_id: [Replace with Client Id]
client_secret: [Replace with Client Secret]
```

### Todo

- Currently only gets the ambient temperature in Fahrenheit, add option for Celsius
- implement more fully the Nest Termostat API [API Documentation](https://developers.nest.com/documentation/cloud/thermostat-guide)