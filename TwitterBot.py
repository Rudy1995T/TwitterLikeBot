from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path=r'C:\Users\Rudy\AppData\Local\Programs\Python\Python37-32\Scripts\geckodriver.exe')

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')
        time.sleep(2)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        #increase sleep time if slow internet connection
        time.sleep(3)

    #Fucntion to like tweets based on hashtag you choose
    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag +'&src=typd')
        time.sleep(2)
        for i in range(1,3):
            #scroll down the page to load in more tweets
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(3)
                except Exception as ex:
                    time.sleep(3)


user = TwitterBot('example.acc007@gmail.com', 'example_1')
user.login()
#hashtag that you want to like tweets to
user.like_tweet('technology')
