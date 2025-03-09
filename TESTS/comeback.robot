*** Settings ***
Library           RPA.Browser.Selenium   run_on_failure=${None}
Library    RPA.Windows
Library    Telnet
Resource    ../GLOBAL/My_kw.robot
Test Teardown    Close Browser
Suite Teardown    Close All Browsers
*** Variables ***
${urls}           https://www.saucedemo.com/v1/
${username_real}    standard_user
${real_pw}        secret_sauce
${username_fake}    fakename
${fake_pw}        thisisnotapassword

*** Test Cases ***

Login Pass
    [Documentation]    Login with correct pw and username
    Open Chrome Browser    ${urls}    headless=${False}    maximized=${True}
    Set up Browser    30
    Click And Input Text    css=#user-name    ${username_real}
    Click And Input Text    css=#password    ${real_pw}
    Click Btn    element=//input[@class="btn_action"]
    ${stt_login}    Run Keyword And Return Status    Wait Until Element Is Visible    css=#inventory_filter_container > select    timeout=30
    Run Keyword If    ${stt_login}    Log To Console    Login Success
    ...    ELSE    Log To Console    Login Fail

Login Fail
    [Documentation]    """ Login fail with wrong username or pw or both. """
    Open Chrome Browser    ${urls}    headless=${False}    maximized=${True}
    Set up Browser    30
    Click And Input Text    css=#user-name    ${username_fake}
    Click And Input Text    css=#password    ${real_pw}
    Click Btn    element=//input[@class="btn_action"]
    ${stt_login}    Run Keyword And Return Status    Wait Until Element Is Visible    css=#inventory_filter_container > select    timeout=30
    Run Keyword If    ${stt_login}    Log To Console    Login Success
    ...    ELSE    Log To Console    Login Fail

Get All Product Info
    [Documentation]    """ Get all product info """
    Open Chrome Browser    ${urls}    headless=${False}    maximized=${True}
    Set up Browser    30

    Comment    Start Login
    Click And Input Text    css=#user-name    ${username_real}
    Click And Input Text    css=#password    ${real_pw}
    Click Btn    element=//input[@class="btn_action"]
    
    Comment    Get all product info
    ${LST_SP}    Get Element Count    xpath=//div[@class="inventory_item"]
    Log To Console    ${LST_SP}
    FOR    ${i}    IN RANGE    1    ${LST_SP}+1
        ${name}    Get text Element    xpath=//div[@class="inventory_item"][${i}]/div[2]/a/div
        Log To Console    ${name}
        ${price}    Get text Element    xpath=//div[@class="inventory_item"][${i}]/div[3]/div 
        Log To Console    ${price}
    END
