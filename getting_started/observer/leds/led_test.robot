*** Settings ***
Library             OperatingSystem
Library             ./SetAllLeds.py
Library             ./set_single_led_robot_mod.py
Variables           ./SetAllLeds.py


*** Variables ***
${color_detected_data}

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


#Turn Left 2
#    Wake Rvr
#    Lefty
#    Shutdown rvr

Crawling Route 1
    Wake Rvr
#    Drive Forward Rally
#    Drive Backward
#    Righty
    Drive Forward Crawl
#    Righty
#    Drive Backward
#    Drive Forward Lightspeed
    Shutdown Rvr

#    Do the dance


#Color detection
#    Wake Rvr
#    Detect Color    ${5}
#    Sleep  7
#    ${content}=    Get file    color.txt
#    Log    ${content}  console=True
#    Shutdown Rvr

#Detect color
#    Wake Rvr
#    ${log}=  Detect Color  ${10}
#    #${detect_color}=  color_detected_handler
#    log to console  ${log}
#    Shutdown Rvr









