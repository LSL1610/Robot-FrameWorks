*** Settings ***
Library           RPA.Browser.Selenium
Library    RPA.Windows
*** Keywords ***
Set up Browser
    [Arguments]    ${timeout}
    Set Selenium Implicit Wait    10
    Set Selenium Speed    0.5
    Set Selenium Timeout    ${timeout}
    sleep    5

Click And Input Text
    [Arguments]    ${element}    ${text}
    Wait Until Element Is Visible    ${element}    timeout=30
    Click Element    ${element}
    Input Text    ${element}    ${text}

Click Btn
    [Arguments]    ${element}
    Wait Until Page Contains Element    ${element}    timeout=30
    Click Element    ${element}    action_chain=${True}

Click By Java
    [Arguments]    ${jv_scp}
    Execute Javascript    ${jv_scp}

Get text Element
    [Arguments]    ${element}
    Wait Until Page Contains Element    ${element}    timeout=30
    ${text}    RPA.Browser.Selenium.Get Text    ${element}

    RETURN    ${text}
