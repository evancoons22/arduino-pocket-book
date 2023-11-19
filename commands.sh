#!/bin/bash

arduino-cli compile --fqbn esp8266:esp8266:d1_mini_clone sketch_nov10a
arduino-cli upload -p /dev/cu.usbserial-130 --fqbn esp8266:esp8266:d1_mini_clone sketch_nov10a
