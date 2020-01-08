*** Settings *** 
Library             ./led_control_observer.py

*** Test Cases ***

Test Keywords From Library
    Turn Leds Off
    Set All Leds Rgb    123      231      213
    Sleep               5 seconds
    Turn Leds Off
    Set All Leds Rgb    255      255      255   
    Turn Leds Off



