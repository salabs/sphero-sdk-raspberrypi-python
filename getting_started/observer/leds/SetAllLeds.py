import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups

### This import for moving RVR tests
from sphero_sdk import RawMotorModesEnum


class SetAllLeds:

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

    def drive_forward(self):
        """ This program will mover RVR forward.
        """
        rvr = SpheroRvrObserver()

        rvr.reset_yaw()

        rvr.raw_motors(
            left_mode=RawMotorModesEnum.forward.value,
            left_speed=64,  # Valid speed values are 0-255
            right_mode=RawMotorModesEnum.forward.value,
            right_speed=64  # Valid speed values are 0-255
        )

    def detect_color(color_detected_data):
        """ This program detects the color which caught the attention of RVR
        """

        #rvr = SpheroRvrObserver()

        print('Color detection data response: ', color_detected_data)