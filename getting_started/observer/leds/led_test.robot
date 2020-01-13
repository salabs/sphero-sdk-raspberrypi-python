*** Settings ***
Library             OperatingSystem
Library             Dialogs
Library             ./SetAllLeds.py
Library             ./set_single_led_robot_mod.py
Variables           ./SetAllLeds.py

Suite Setup  Wake Rvr
Suite Teardown  Shutdown Rvr

*** Test Cases ***

Run a query for RVR actions
    Ask Driver for directions

*** Keywords ***

Ask Driver for directions
    ${selections}=  Get Selections From User   Select which actions RVR will execute:  Drive Forward Crawling  Drive Forward Rallying  Drive Backwards  Turn Right  Turn Left  Led Show
      FOR  ${option}  IN  @{selections}
	        Run Keyword If 	'${option}' == 'Drive Forward Crawling' 	                Run keyword  Crawling
	        Run Keyword If 	'${option}' == 'Drive Forward Rallying' 	                Run keyword  Rallying
	        Run Keyword If 	'${option}' == 'Drive Backwards' 	                        Run keyword  Backwards
	        Run Keyword If 	'${option}' == 'Turn Right'               	                Run keyword  Turn Right
	        Run Keyword If 	'${option}' == 'Turn Left'               	                Run keyword  Turn Left
	        Run Keyword If 	'${option}' == 'Led Show' 	                                Run keyword  Led Show
	        END
            Continue or quit

Continue or quit
    ${redrive}=  Get selection from user  Try again?  YES - New drive  NO - Quit executing tasks and exit
	        Run Keyword If 	'${redrive}' == 'YES - New drive' 	                        Run keyword  Redrive
	        Run Keyword If 	'${redrive}' == 'NO - Quit executing tasks and exit' 	    log to console  Bye bye!

Redrive
    Ask Driver for directions

Crawling
#    Wake Rvr
    Drive Forward Crawl
#    Shutdown Rvr

Rallying
#    Wake Rvr
    Drive Forward Rally
#    Shutdown Rvr

Backwards
#    Wake Rvr
    Drive Backward
#    Shutdown Rvr

Turn Right
#    Wake Rvr
    Righty
#    Shutdown Rvr

Turn Left
#    Wake Rvr
    Lefty
#    Shutdown Rvr

Lightspeed
#    Wake Rvr
    Drive Forward Lightspeed
#    Shutdown Rvr

Led Show
    Test Leds

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