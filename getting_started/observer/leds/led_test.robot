*** Settings *** 
Library             ./SetAllLeds.py
Library             ./set_single_led_robot_mod.py

*** Test Cases ***

#Test Keywords From Library
#    Test Leds

#Test single led
#    Singleled

## näiden library on toistaiseksi SetAllLeds.py

#Wake up RVR
#    Wake Rvr

#Shut down RVR
#    Shutdown Rvr

#Move Forward
#    Wake Rvr
#    Drive Forward
#    Shutdown Rvr

Detect color
    Wake Rvr
    Detect Color
    set test variable  ${color}
    log to console  ${color}
    Shutdown Rvr









