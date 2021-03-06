import os
import sys
import time
from robot.api import logger

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RvrStreamingServices
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups

### This import for moving RVR tests with raw motors
from sphero_sdk import RawMotorModesEnum


#def color_detected_handler(color_detected_data):
#    logger.info('Color detection data response: {}'.format(color_detected_data))

def color_detected_handler(color_detected_data):
    with open("color.txt", 'a+') as fp:
        fp.write(color_detected_data)

class sphero_rvr:

    def test_leds(self):
        """ This program demonstrates how to set the all the LEDs.
        """
        rvr = SpheroRvrObserver()

        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

        rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in Colors.off.value]
        )

        # Delay to show LEDs change
        time.sleep(1)

        rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [255, 0, 0]]
        )

        # Delay to show LEDs change
        time.sleep(1)
        
        rvr.close()

        ###  RVR basic commands (maybe these to a setup file?)

    def wake_rvr(self):
        """ This program will wake up RVR.
        """
        rvr = SpheroRvrObserver()

        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

    def shutdown_rvr(self):
        """ This program will shut down RVR.
        """
        rvr = SpheroRvrObserver()

        time.sleep(1)

        rvr.close()


        ### RVR Drive commands

    def drive_forward_crawl(self):
        """ This program will move RVR forwards slow.
        """
        rvr = SpheroRvrObserver()

        rvr.reset_yaw()

        rvr.drive_control.drive_forward_seconds(
            speed=64,
            heading=0,  # Valid heading values are 0-359
            time_to_drive=.5
        )
        rvr.close()

    def drive_forward_rally(self):
        """ This program will move RVR forward fast.
        """
        rvr = SpheroRvrObserver()

        rvr.reset_yaw()

        rvr.drive_control.drive_forward_seconds(
            speed=128,
            heading=0,  # Valid heading values are 0-359
            time_to_drive=.5
        )
        rvr.close()

    def drive_forward_lightspeed(self):
        """ This program will move RVR forward at lightspeed.
        """
        rvr = SpheroRvrObserver()

        rvr.reset_yaw()

        rvr.drive_control.drive_forward_seconds(
            speed=255,
            heading=0,  # Valid heading values are 0-359
            time_to_drive=.2
        )
        rvr.close()

    def drive_backward(self):
        rvr = SpheroRvrObserver()

        rvr.reset_yaw()

        rvr.drive_control.drive_backward_seconds(
            speed=16,
            heading=0,  # Valid heading values are 0-359
            time_to_drive=.5
        )
        rvr.close()

    def lefty(self):
        rvr = SpheroRvrObserver()

        rvr.reset_yaw()

        rvr.drive_control.turn_left_degrees(
            heading=0,  # Valid heading values are 0-359
            amount=90
        )

    def righty(self):
        rvr = SpheroRvrObserver()

        rvr.reset_yaw()

        rvr.drive_control.turn_right_degrees(
            heading=0,  # Valid heading values are 0-359
            amount=90
        )

    #def do_the_dance(self):
    #    rvr = SpheroRvrObserver()

    #    rvr.reset_yaw()



    #def detect_color(self, obs_time):
    #    #data = "{}".format(color_detected_data)
    #    #print(data)
    #    #return data

    #    """ This method uses the color sensor on RVR (located on the down side of RVR, facing the floor)
    #        to report colors detected for obs_time seconds.
    #    """
    #    rvr = SpheroRvrObserver()
    #    rvr.close()
    #    try:
    #        rvr.wake()
    #
    #       # Give RVR time to wake up
    #       time.sleep(2)
    #
    #        rvr.enable_color_detection(is_enabled=True)
    #        rvr.sensor_control.add_sensor_data_handler(
    #            service=RvrStreamingServices.color_detection,
    #            handler=color_detected_handler
    #        )
    #        rvr.sensor_control.start(interval=250)
    #
    #        # Allow this program to run for 2 seconds
    #        time.sleep(0.25)
    #
    #    finally:
    #        rvr.sensor_control.clear()
    #
    #        # Delay to allow RVR issue command before closing
    #        time.sleep(.5)
    #
    #        rvr.close()

    #def detect_color(self, obs_time):
    #    rvr = SpheroRvrObserver()
    #    rvr.close()
    #    rvr.wake()
    #    # Give RVR time to wake up
    #    time.sleep(2)
    #    rvr.enable_color_detection(is_enabled=True)
    #    rvr.sensor_control.add_sensor_data_handler(
    #        service=RvrStreamingServices.color_detection,
    #        handler=color_detected_handler
    #    )
    #    rvr.sensor_control.start(interval=250)
    #    # Allow this program to run for obs_time seconds
    #    time.sleep(obs_time)
    #    rvr.sensor_control.clear()
    #    # Delay to allow RVR issue command before closing
    #    time.sleep(.5)

    #    rvr.close()