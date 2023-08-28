# rpi_remote_mqtt

# Testing MQTT
## Install
`sudo apt install mosquitto-clients`

# Testing
- `mosquitto_sub -h host -p 8883 -u user -P pass -v -t '#' -F "%I %t %p"`
- `mosquitto_pub -h host -p 8883 -u user -P pass -t mac/in/R/relay8 -m "1"`
