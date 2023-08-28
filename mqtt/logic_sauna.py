import os, sys

import rpi_peripherals_sauna as rpi_peripherals
from logic_common import *

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from common import log

logger = log.get()


class Temperature:
    def __init__(self, index, name):
        self.timeout = 10000
        self.timestamp = 0
        self.mqtt = None
        self.mqtt_last = None
        self.name = "temperature_" + name
        self.index = index
        self.temperature = None
        self.testing = False

    def init(self):
        pass

    def get(self):
        return self.temperature.get()

    def read(self):
        self.temperature = rpi_peripherals.temperature_sensors[self.index]

    def set(self, value):
        self.temperature = value
        self.mqtt = self.get()
        self.testing = True

    def loop(self):
        if common.millis_passed(self.timestamp) >= self.timeout or self.timestamp == 0:
            self.timestamp = common.get_millis()
            if not self.testing:
                self.read()
                self.mqtt = self.get()

    def has_mqtt(self):
        return self.mqtt != None and self.mqtt != self.mqtt_last

    def get_mqtt(self):
        if self.has_mqtt():
            self.mqtt_last = self.mqtt
            self.mqtt = None
            return self.name, self.mqtt_last
        return None, None


class Relay:
    def __init__(self, name, index):
        self.mqtt = None
        self.mqtt_last = None
        self.name = name
        self.index = index

    def init(self):
        pass

    def get(self):
        return rpi_peripherals.relays[self.index].get()

    def set(self, state):
        rpi_peripherals.relays[self.index].set(state)
        self.mqtt = state

    def loop(self):
        pass

    def has_mqtt(self):
        return self.mqtt != None and self.mqtt != self.mqtt_last

    def get_mqtt(self):
        if self.has_mqtt():
            self.mqtt_last = self.mqtt
            self.mqtt = None
            return self.name, self.mqtt_last
        return None, None


uptime = Uptime()
ip = Ip()
temperature_inside = Temperature(1, "inside")
heater_1 = Relay("heater_1", 1)


def init():
    logger.info("[LGC]: init begin")
    global init_status
    rpi_peripherals.init()
    uptime.init()
    ip.init()
    temperature_inside.init()
    heater_1.init()
    logger.info("[LGC]: init end")


def get_mqtt():
    if uptime.has_mqtt(): return uptime.get_mqtt()
    if ip.has_mqtt(): return ip.get_mqtt()
    if temperature_inside.has_mqtt(): return temperature_inside.get_mqtt()
    if heater_1.has_mqtt(): return heater_1.get_mqtt()
    return None, None


def set_mqtt(topic, message):
    logger.info("[LGC]: set_mqtt %s %s" % (topic, message))
    if topic == heater_1.name:
        heater_1.set(int(message))
    elif topic == temperature_inside.name:
        temperature_inside.set(float(message))


def loop_unblocking():
    uptime.loop()
    ip.loop()
    heater_1.loop()


def loop_blocking():
    temperature_inside.loop()


def loop_test():
    init()
    while True:
        loop_unblocking()
        loop_blocking()


if __name__ == "__main__":
    import readline
    import rlcompleter
    import code

    readline.parse_and_bind("tab: complete")
    code.interact(local=locals())
