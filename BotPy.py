from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

driver = webdriver.Firefox (executable_path='c:\geckodriver.exe') 

sleep(2)
driver.get("https://www.instagram.com/")
sleep(3)

button_cookies = driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]')
button_cookies.click()
sleep(3)

username = driver.find_element_by_name('username')
username.send_keys('********')
passoword = driver.find_element_by_name('passoword')
passoword.send_keys('**********')
button_login = driver.fing_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
button_login.click()
sleep(5)
print('Sesión iniciada')

hashtag_list = ['perro' , 'gato' , 'ave']

for hashtag in hashtag_list:
    driver.get('https://www.instagram.com/explore/tags/' + hashtag)
    sleep(5)

    first_thumbnail = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/article/div[1]/div/div/div[1]/div[1]')
    first_thumbnail,click()
    sleep(5)
    for n in range(5):
        try:
            button_like = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]')
            button_like.click()
            sleep(random.randint(1,5))

            reactions = ['que lindo', "wow" , "que feo"]
            try:
                input_comment = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                input_comment.click()

            except:
                pass
            input_comment = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
            input_comment.send_keys(random.choice(reactions))
            input_comment.send_keys(Keys.ENTER)
            sleep(random.randint(1,5))

            print('Post' + str(n) + 'en #' + hashtag)

            button_next = driver.find_element_by_css_selector('.coreSpriteRightPaginationArrow')
            button_next.click()
            sleep(random.randint(3,5))
        except:
                print('Ocurrio una exepcion')
    print('#' + hashtag + 'completad')