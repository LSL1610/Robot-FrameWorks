*** Settings ***
Suite Setup       OpenBrowserProfile
Suite Teardown    DelFolderImgAndCloseAllBrowser
Test Setup
Resource          ../GLOBAL/Tai.resource

*** Test Cases ***
TestcaseSetup
    Create File For First Run

Check Phieu Nap
    [Documentation]    tai khoan: atlpaypay
    [Template]    Template_Check
    #Url    Brand
    #${URL_SUN}    SUN
    ${URL_789}    789
    #${URL_MAN}    MAN

Check Phieu Rut
    [Template]    Template_Check
    #Url    Brand
    #${URL_SUN}    SUN
    ${URL_789}    789
    ${URL_MAN}    MAN

demo_profile
    log    history
