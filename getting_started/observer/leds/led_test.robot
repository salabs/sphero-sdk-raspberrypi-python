*** Settings ***
Library             OperatingSystem
Library             Dialogs
Library             ./SetAllLeds.py
Library             ./set_single_led_robot_mod.py
Variables           ./SetAllLeds.py

#Suite Setup  Wake RVR
#Suite Teardown  Shutdown RVR

*** Variables ***
#${color_detected_data}

*** Test Cases ***
#Which drive will be executed?
#        ask_value



Run a query for actions
    ${selections}=  Get Selections From User   Select which actions will RVR execute:  Drive Forward Crawling  Drive Forward Rallying  Drive Backwards  Turn Right  Turn Left  Go Lightspeed (WARNING!!! need SPACE!)  Park RVR and Exit
      FOR  ${var}  IN  @{selections}
	        Run Keyword If 	'${var}' == 'Drive Forward Crawling' 	                Run keyword  Crawling
	        Run Keyword If 	'${var}' == 'Drive Forward Rallying' 	                log to console  RALLY
	        Run Keyword If 	'${var}' == 'Drive Backwards' 	                        log to console  BACKWARDS
	        Run Keyword If 	'${var}' == 'Turn Right'               	                log to console  TURN RIGHT
	        Run Keyword If 	'${var}' == 'Turn Left'               	                log to console  TURN LEFT
	        Run Keyword If 	'${var}' == 'Go Lightspeed (WARNING!!! need SPACE!)' 	log to console  LIGHTSPEED
	        Run Keyword If 	'${var}' == 'Park RVR and Exit' 	                    log to console  EXIT
	        END



#Crawling Route 1
#    Drive Forward Rally
#    Drive Forward Crawl
#    Drive Forward Lightspeed
#    Drive Backward
#    Righty
#    Lefty



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

*** Keywords ***
Crawling
    Wake Rvr
    Drive Forward Crawl
    Shutdown Rvr
