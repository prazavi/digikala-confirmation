from selenium import webdriver
import selenium
driver=webdriver.Chrome()
#driver.maximize_window()
driver.get('https://www.digikala.com/users/login')
user=driver.find_element_by_name('login[email_phone]')
password=driver.find_element_by_name('login[password]')
button=driver.find_element_by_class_name('btn-login')
user.clear()
password.clear()
print('should i enter?')
s=input()
if s=='yes':
    user.send_keys('peimanrazavi@yahoo.com')
    password.send_keys('p1661374')
    button.click()
    button2=driver.find_element_by_class_name('c-semi-modal__secondary-btn')
    print('do you want to confirm your number?')
    st=input()
    if st=='yes':
        button3=driver.find_element_by_partial_link_text('رسال کد تایید')
        button3.click()
        print('what was the code sent to you')
        code=input()
        confirm=driver.find_element_by_name('confirm[code]')
        confirm.send_keys(int(code))
    else:
        button2.click()
else:
    driver.close()