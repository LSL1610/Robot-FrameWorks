*** Settings ***
Library           RPA.Browser

*** Variables ***
${urls}           https://www.saucedemo.com/v1/
${username_real}    standard_user
${real_pw}        secret_sauce
${username_fake}    fakename
${fake_pw}        thisisnotapassword

*** Test Cases ***
Login Pass
    [Documentation]    Login with correct pw and username
    Open Browser    ${urls}    Chrome    executable_path=D:\\Lam_report\\chromedriver\\chromedriver.exe
    Maximize Browser Window
    Set up Browser    30
    Click And Input Text    css=#user-name    ${username_real}
    Click And Input Text    css=#password    ${real_pw}
    Click Btn    css=#login-button
    ${stt_login}    Run Keyword And Return Status    Wait Until Element Is Visible    css=#inventory_filter_container > select    timeout=30
    Run Keyword If    ${stt_login}    Log To Console    Login Success
    ...    ELSE    Log To Console    Login Fail
    Close All Browsers

Login Fail
    [Documentation]    Login fail with wrong username or pw or both.
    Open Browser    ${urls}    Chrome    executable_path=D:\\Lam_report\\chromedriver\\chromedriver.exe
    Maximize Browser Window
    Set up Browser    30
    Click And Input Text    css=#user-name    ${username_fake}
    Click And Input Text    css=#password    ${real_pw}
    Click Btn    css=#login-button
    ${stt_login}    Run Keyword And Return Status    Wait Until Element Is Visible    css=#inventory_filter_container > select    timeout=30
    Run Keyword If    ${stt_login}    Log To Console    Login Success
    ...    ELSE    Log To Console    Login Fail
    Close All Browsers

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
    Wait Until Element Is Visible    ${element}    timeout=30
    Click Element    ${element}
