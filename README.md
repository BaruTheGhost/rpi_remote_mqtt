# rpi_remote_mqtt

# Testing MQTT
## Install
`sudo apt install mosquitto-clients`

# Testing
- `mosquitto_sub -h host -p 8883 -u user -P pass -v -t '#' -F "%I %t %p"`
- `mosquitto_pub -h host -p 8883 -u user -P pass -t sauna/output/relay_1 -m "1"`

# Dependencies
`sudo gpasswd -a pi wheel`
`sudo apt install python3-pip`
`sudo apt install python3-paho-mqtt`
`pip install sdnotify`

# Add credentials
`cp mqtt/credentials.py.template mqtt/credentials.py`
Edit the file as needed.

# Test run

`python mqtt/main.py`
