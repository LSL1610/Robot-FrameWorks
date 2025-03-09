*** Settings ***
Library           RPA.Browser.Selenium    run_on_failure=Nothing    timeout=20    implicit_wait=5
Library           OperatingSystem
Library           DateTime

*** Variables ***

*** Keywords ***
My Create Folder Log For Chrome Browser
    [Arguments]    ${arg0}    ${arg3}=LOG_CHROME
    [Documentation]    G:\\My Drive\\Projects\\lib\\Dat_lib\\global_keywords.resource
    ...    ../../../1_my_libs/global_keywords.resource
    ...    Set Selenium Speed 0.2
    ...    Always create folder name first
    ...    If existed will not created anymore
    ...    There are 2 folder name: Check_Alive_B1_12_Brands or Check_iframe
    ${args}    Evaluate    f"${arg0}:\\PROJECT_DAT\\LOG\\${arg3}"
    Log To Console    \nFolder Created in path: ${args}
    ${local_path}    Create Directory    ${args}
    Run Keyword And Return Status    Empty Directory    ${args}
    ${current_time}    Get Current Date    result_format=%B_%H_%M_%S
    ${log_file}    Evaluate    f"${args}\\${current_time}_chrome.log"
    Log To Console    \nNew Chrome Log created in: ${log_file}
    #Create empty chrome with options
    ${my_options}    Set Variable    add_argument("--disable-popup-blocking");add_argument("--disable-notifications");add_argument("--disable-gpu");add_argument("--disable-logging")
    Comment    ${chrome_path}    Set Variable    ${CURDIR}\\drivers\\chromedriver.exe
    Open Browser    ${EMPTY}    gc    options=${my_options}    service_log_path=${log_file}    #executable_path=${chrome_path}
    Maximize Browser Window
    Delete All Cookies
    Set Selenium Speed    0.2
    Set Browser Implicit Wait    1
    Set Selenium Timeout    30

My Open Chrome With Disable Image And Hide Info Bar
    ${prefix}    Create Dictionary    profile.default_content_setting_values.notifications=${2}    profile.managed_default_content_settings.popups=${2}    credentials_enable_service=${False}    profile.managed_default_content_settings.images=${1}
    ${disableInfoBar}    Create List    enable-automation
    ${options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    modules=selenium.webdriver
    Call Method    ${options}    add_argument    no-sandbox
    Call Method    ${options}    add_argument    disable-gpu
    Call Method    ${options}    add_experimental_option    prefs    ${prefix}
    Call Method    ${options}    add_experimental_option    excludeSwitches    ${disableInfoBar}
    Call Method    ${options}    add_experimental_option    useAutomationExtension    ${False}
    Call Method    ${options}    add_argument    dns-prefetch-disable
    ${chrome_path}    Set Variable    ${CURDIR}\\drivers\\chromedriver.exe
    Create Webdriver    Chrome    options=${options}    #executable_path=${chrome_path}
    Maximize Browser Window
    Set Selenium Speed    0.2
