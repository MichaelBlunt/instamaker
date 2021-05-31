from selenium import webdriver
import random
import time
import json
import names
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

while True: #constantly loop the program

    #launch chromewebdriver
    browser = webdriver.Chrome('/usr/bin/chromedriver')
    browser.maximize_window()
    browser.delete_all_cookies()

    i = 0
    while i < 1:
        mode =  "1" #input('Type "0" for manual name/age verfication, type "1" for automatic name/age verification')
        #50/50 for male or female user
        gender = random.choice([0, 1]) 

        if gender == 0:
            #generate name (male)
            gender = 'male'
            firstName = names.get_first_name(gender='male')
            middleName = names.get_first_name(gender='male')
            lastName = names.get_last_name()
            firstInitial = firstName[0]
            middleInitial = middleName[0]
            lastInitial = lastName[0]
            firstRest = firstName[1:]
            middleRest = middleName[1:]
            lastRest = lastName[1:]
            firstEnd = firstName[-1]
            middleEnd = middleName[-1]
            lastEnd = lastName[-1]
            name = str(str(firstName) + " " + str(lastName))
        if gender == 1:
            #generate name (female)
            gender = 'female'
            firstName = names.get_first_name(gender='female')
            middleName = names.get_first_name(gender='female')
            lastName = names.get_last_name()
            firstInitial = firstName[0]
            middleInitial = middleName[0]
            lastInitial = lastName[0]
            firstRest = firstName[1:]
            middleRest = middleName[1:]
            lastRest = lastName[1:]
            firstEnd = firstName[-1]
            middleEnd = middleName[-1]
            lastEnd = lastName[-1]
            name = str(str(firstName) + " " + str(lastName))

        #percentage based username selection
        userNumber = random.randint(0,20)

        if userNumber == 0 or userNumber == 1 or userNumber == 2:
            username = str(str(firstName) + "." + str(lastName) + str(random.randint(1,10)))
            
        if userNumber == 3:
            username = str(str(firstInitial) + "." + str(firstRest) + "_" + str(lastName) + str(random.randint(1,10)))

        if userNumber == 4:
            username = str(str(firstInitial) + "." + str(firstRest) + "." + str(lastName) + str(random.randint(1,10)))

        if userNumber == 5:
            username = str(str(firstInitial) + str(firstEnd) + "." + str(lastName) + str(userNumber))

        if userNumber == 6:
            username = str(str(firstName) + str(firstEnd) + "." + str(lastInitial) + str(userNumber))

        if userNumber == 7:
            username = str(str(lastInitial) + str(firstRest) + "." + str(firstInitial) + str(lastRest) + str(userNumber))

        if userNumber == 8 or userNumber == 9 or userNumber == 10:
            username = str(str(firstName) + str(middleInitial) + str(lastName) + str(userNumber))

        if userNumber == 11 or userNumber == 12 or userNumber == 13:
            username = str(str(firstName) + "." + str(lastName) + str(random.randint(1,100)) + str(userNumber))

        if userNumber == 14 or userNumber == 15:
            username = str(str(firstName) + "_" + str(lastName) + str(userNumber))

        if userNumber == 16 or userNumber == 17:
            username = str(str(lastName) + "_" + str(firstName) + str(userNumber))

        if userNumber == 18 or userNumber == 19:
            username = str(str(lastName) + "." + str(firstName) + str(userNumber))

        if userNumber == 20:
            username = str(str(firstInitial) + str(firstEnd) + "." + str(lastName))

        if mode == "0":
            userApprove = input('Name is "' + name + '" and username is "' + username + '. Is this ok? (Y/N)  ')
            if userApprove != 'Y':
                i = 0
            else:
                i = 1
        else:
            browser.get("https://rhiever.github.io/name-age-calculator")
            print("loading name/age verification")

            #Enter name into text box
            nameField = browser.find_element_by_id('NamePicker')
            nameField.send_keys(firstName)

            #Set the correct gender in dropdown box
            genderPicker = Select(browser.find_element_by_id('GenderPicker'))
            if gender == 'male':
                genderPicker.select_by_value('M')
            elif gender == 'female':
                genderPicker.select_by_value('F')
            else:
                print('error with gender picker in name/age verification')

            #Submit the request
            submitButton = browser.find_element_by_xpath('//*[@id="name_form"]/input[2]')
            submitButton.click()

            #Verify name is acceptable
            verifyName = browser.find_element_by_id('chart').text
            firstPosition = verifyName.find('from')
            trimmedString = verifyName[firstPosition:len(verifyName)]
            trimmedString = trimmedString[5:]
            trimmedList = trimmedString.split(' ')
            predictedAge = int(trimmedList[0])

            if predictedAge < 26:
                ageVerification = 'good'
                i = 1
            else:
                ageVerification = 'old'
                i = 0

            print(name + "'s predicted age is " + str(predictedAge))
            
    #open email generator
    browser.get("https://temp-mail.org/en/")

    #wait for loading
    print("loading email page")
    time.sleep(5)

    #click copy button
    createEmail = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/button[1]')
    createEmail.click()
    print("copying email")
    time.sleep(1)

    #new tab
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])

    #open instagram
    browser.get("https://www.instagram.com/accounts/emailsignup/")
    print("waiting for instagram to load")
    time.sleep(5) #time.sleep count can be changed depending on the Internet speed.

    #Fill the email value
    email_field = browser.find_element_by_name('emailOrPhone')
    email_field.send_keys(Keys.CONTROL, 'v') #paste email in
    time.sleep(0.5) #looks cursed when it just instantly fills up

    #Fill the fullname value
    fullname_field = browser.find_element_by_name('fullName')
    fullname_field.send_keys(name)
    time.sleep(0.5)

    #Fill username value
    username_field = browser.find_element_by_name('username')
    username_field.send_keys(username)
    time.sleep(0.5)

    #Fill password value
    password_field = browser.find_element_by_name('password')
    password = ('Password123!'+lastName)
    password_field.send_keys(password) #You can set another password here.
    time.sleep(0.5)


    submit = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[7]/div/button')
    submit.click()
    print("load birthday portion of signup")
    time.sleep(5)

    #Fill in year value
    yearNumber = random.randint(2003,2004)
    year = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
    year.click()
    time.sleep(2)
    if yearNumber == 2003:
        select = Select(browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select'))
        select.select_by_value('2003')

    if yearNumber == 2004:
        select = Select(browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select'))
        select.select_by_value('2004')

    #Fill in day value
    dayNumber = random.randint(1,28)
    select = Select(browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select'))
    select.select_by_value(str(dayNumber))

    #Fill in month value
    monthNumber = random.randint(1,12)
    select = Select(browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select'))
    select.select_by_value(str(monthNumber))

    submit = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
    submit.click() #enable this to actually send the email
    print("sent the email")
    time.sleep(2)

    #Switch to first tab
    browser.switch_to.window(browser.window_handles[0])
    print("waiting for email")
    time.sleep(20)
    
    #Open the email and copy code
    openEmail = browser.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[3]/div[2]/a')
    openEmail.location_once_scrolled_into_view
    openEmail.click()
    print("opening email")
    time.sleep(5)
    instaCode = browser.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]').text
    print("copying validation code")
    time.sleep(1)

    #paste code
    browser.switch_to.window(browser.window_handles[1])
    codeBox = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')
    codeBox.send_keys(instaCode)

    #submit...dangerous only use in conjunction with a vpn
    submitCode = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
    '''submitCode.click()''' # <-- the dangerous part, ask michael why it is dangerous if you don't know
    
    #put relevant data into json file
    data = {}
    data['instagram'] = []
    data['instagram'].append({
        'name': name,
        'username': username,
        'password': password,
        'year': yearNumber,
        'month': monthNumber,
        'day': dayNumber,
        'gender': gender,
        'age': predictedAge,
    })

    with open(('C:/Users/micha/Desktop/Programing/Selenium/Instagram_Accounts/' + firstName + lastName + '.json'), 'w') as outfile:
        json.dump(data, outfile)
