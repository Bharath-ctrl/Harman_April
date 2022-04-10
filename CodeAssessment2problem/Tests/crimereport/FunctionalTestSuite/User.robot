*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${web_url}   http://127.0.0.1:5000
${email}    abcdef@gmail.com
${password}     123

*** Test Cases ***
User Registeration
    [Documentation]  Can user able to register?
    [Tags]  user
    open browser    ${web_url}   chrome
    maximize browser window
    input text  name:name   Charlie
    sleep  1s
    input text  name:address    whitefield
    sleep  1s
    input text  name:email      ${email}
    sleep  1s
    input text  name:phone      890981111
    sleep  1s
    input text  name:password   ${password}
    sleep  1s
    click button  xpath=//html/body/div/div/div/form/table/tbody/tr[6]/td[2]/button
    sleep  1s

User Login
    [Documentation]  Once Registered,user can able to login?
    [Tags]  user
    input text  name:mail  ${email}
    sleep  1s
    input text  name:password   ${password}
    sleep  1s
    click button  xpath=//html/body/div/div/div/form/table/tbody/tr[3]/td[2]/button
    sleep  5s

Report Crime
    [Documentation]  Can Register able to report crime?
    [Tags]  user
    click element  class:btn-danger
    sleep  2s
    input text  name:date   09042022
    sleep  2s
    input text  name:description  My house was robbed , all the cctv footages are being deleted and the cameras are also been broken down.
    sleep   1s
    input text  name:remark    I have suspision on my relatives
    sleep  3s
    click button  class:btn-success
    sleep  1s

Edit User Profile
    [Documentation]  Register can view and modify account details
    [Tags]  user
    click link  xpath=//html/body/nav/section[2]/div/a
    sleep  3s
    input text  name:email  ${email}
    sleep  3s
    click button  class:btn-success
    sleep  2s
    input text  name:name   Bharath
    sleep  3s
    input text  name:phone   8908908908
    sleep  3s
    click button  class:btn-primary
    sleep  3s

User Logout
    [Documentation]  Is Register not able to access after logout
    [Tags]  userlogout
    click link  xpath=//html/body/nav/section[3]/div/a
    sleep  4s
    close browser


*** Keywords ***