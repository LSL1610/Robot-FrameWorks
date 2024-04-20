*** Settings ***
Library           RPA.Browser

*** Variables ***
${urls}           https://www.google.com/

*** Test Cases ***
demo
    Open Browser    ${urls}    Chrome    executable_path=D:\\Lam_report\\chromedriver\\chromedriver.exe
    Maximize Browser Window
    Set Selenium Implicit Wait    10
    Set Selenium Speed    0.5
    Set Selenium Timeout    30
    sleep    5
    Close All Browsers

