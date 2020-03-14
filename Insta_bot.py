from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random 

class instabot():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path='C:\\Users\\skullcandy\\Desktop\\tinder_bot\\chromedriver.exe')
        self.driver.get("http://instagram.com")
        sleep(2)
    def main(self):
        try:
            self.login()
            j=1
            for i in range (1,11):
                self.explore()
                self.follow(j)
                j=j+1
                self.gotohome()
                self.scroll()
                sleep(2)
                self.like_explore(j)
                self.scroll()
                self.gotohome()
                self.scroll()
                sleep(2)
                self.explore()
                self.follow(j)
                j=j+1
            self.driver.close()
        except Exception:
            self.driver.close()

       
    def login(self):
        id=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        id.send_keys("ENTER YOUR USER NAME")
        password=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        password.send_keys("ENTER PASSWORD")
        login=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")
        login.click()
        sleep(5)
        notnow=self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
        notnow.click()
            
    def explore(self):
        explore=self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
        explore.click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/h2/a').click()
        sleep(2)
        self.driver.refresh()
        sleep(5)

    def follow(self,i):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div["+str(i)+"]/div[3]/button").click()
        sleep(2)
    def gotohome(self):
        home=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a')
        home.click()
        sleep(2)
        self.driver.refresh()
        sleep(5)
    def scroll(self):
        for i in range(0,5):
            sleep(2)
            actionChain = webdriver.ActionChains(bot.driver)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            sleep(2)
    def like_explore(self,i):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
        sleep(2)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div[1]/div/div[1]/div["+str(i)+"]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()
            
           
bot=instabot()
bot.main()


        
