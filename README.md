# rpi_remote_mqtt

# Testing MQTT
## Install
`sudo apt install mosquitto-clients`

# Testing
- `mosquitto_sub -h host -p 8883 -u user -P pass -v -t '#' -F "%I %t %p"`
- `mosquitto_pub -h host -p 8883 -u user -P pass -t sauna/output/heater_1 -m "1"`
- `mosquitto_pub -h host -p 8883 -u user -P pass -t sauna/output/temperature_inside -m "99.4"`

# Dependencies
- `sudo gpasswd -a pi wheel`
- `sudo apt install python3-periphery`
- `sudo apt install python3-paho-mqtt`
- `sudo apt install python3-sdnotify`
- `pip install sdnotify`

# Add credentials
- `cp mqtt/credentials.py.template mqtt/credentials.py`
- Edit the file as needed.

# Test run

`python mqtt/main.py`
