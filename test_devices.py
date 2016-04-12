#!/usr/bin/env python2

from soco import SoCo
from soco import discover

from phue import Bridge

#import harmony.py
from harmony.harmony import run_sonos, run_appletv, turn_off
from time import sleep

import sys

# variables
###########

# connect to hue bridge
hue_bridge = Bridge('192.168.0.100')
hue_bridge.connect()

# get all sonos speakers
sonos_speakers = discover()



# functions
###########

# test function for hue
def hue():
    # Turn on all lights and set it to red
    for light in hue_bridge.lights:
        hue_bridge.set_light(light.name, 'on', True)
        hue_bridge.set_light(light.name, 'hue', 4000)
        hue_bridge.set_light(light.name, 'sat', 196)
        hue_bridge.set_light(light.name, 'bri', 96)



# test function for sonos
def sonos():

    # ungroup all speakers
    for sonos_speaker in sonos_speakers:
        sonos_speaker.unjoin()

    # sleep is necessary, otherwise sonos fucks up
    sleep(3) 

    # prepare all speakers
    for sonos_speaker in sonos_speakers:
        sonos_speaker.stop()
        sonos_speaker.volume = 20
        sonos_speaker.clear_queue()

    # group all speakers and play a song
    ## need to find a solution how to play a spotify playlist
    sonos_speaker.partymode()
    track = "x-sonos-spotify:spotify%3atrack%3a0dvnKnQnIoB1WEWwtaTywp?sid=9&flags=32"
    sonos_speaker.play_uri(track)


 
# test function for harmony
def harmony():
    # send a command
    run_sonos()   





# main
######

print "hey there"
#hue()
#sonos()
harmony()


