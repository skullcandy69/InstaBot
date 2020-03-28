from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from tkinter import *
import random


class instabot():
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password
        self.driver = webdriver.Chrome(
            executable_path='C:\\Users\\skullcandy\\Desktop\\tinder_bot\\chromedriver.exe')
        self.driver.get("http://instagram.com")
        sleep(2)

    def main(self):
        try:
            self.login()
            j = 1
            for i in range(1, 11):
                self.explore()
                self.follow(j)
                j = j+1
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
                j = j+1
                self.follow(j)
                j = j+1
                self.follow(j)
                j = j+1
            self.driver.close()
        except Exception:
            self.driver.close()

    def login(self):
        id = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        id.send_keys(self.userid)
        password = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        password.send_keys(self.password)
        login = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")
        login.click()
        sleep(5)
        notnow = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[3]/button[2]")
        notnow.click()

    def explore(self):
        explore = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
        explore.click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/h2/a').click()
        sleep(2)
        self.driver.refresh()
        sleep(5)

    def follow(self, i):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div[2]/div/div/div["+str(i)+"]/div[3]/button").click()
        sleep(2)

    def gotohome(self):
        home = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a')
        home.click()
        sleep(2)
        self.driver.refresh()
        sleep(5)

    def scroll(self):
        for i in range(0, 5):
            sleep(2)
            actionChain = webdriver.ActionChains(self.driver)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            sleep(2)

    def like_explore(self, i):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
        sleep(2)
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div[2]/div/div[1]/div[1]/div/a/div[1]/div["+str(i)+"]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div[3]/button").click()


window = Tk()
window.title("Welcome to LikeGeeks app")

window.geometry('300x150')

lbl = Label(window, text="Enter User Name:")

lbl.grid(column=0, row=0)

usid = Entry(window, width=25)

usid.grid(column=2, row=0)

pas = Label(window, text="Enter Password:")

pas.grid(column=0, row=2)

password = Entry(window, width=25)

password.grid(column=2, row=2)


def clicked():
    bot = instabot(usid.get(), password.get())
    bot.main()


btn = Button(window, text="Run", command=clicked)

btn.grid(column=1, row=5, sticky=W,
         pady=4,)

b = Button(window, text="Quit", command=window.quit)

b.grid(column=2, row=5, sticky=W,
       pady=4)
window.mainloop()
