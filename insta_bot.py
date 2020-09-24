from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
from selenium.webdriver.common.action_chains import ActionChains

drive_path = 'C:/Users/akash/Downloads/edgedriver_win64/msedgedriver.exe'
webdriver = webdriver.Edge(executable_path=drive_path)
sleep(2)
print("\n webdriver found")

webdriver.get('https://www.instagram.com/')
sleep(randint(3, 5))
print("\n website found")

u_n = webdriver.find_element_by_name("username")
u_n.send_keys("ars.onethetechnoguy@gmail.com")
sleep(randint(3, 6))

ps = webdriver.find_element_by_name("password")
ps.send_keys("akash@1997")
sleep(randint(3, 6))
print("\n username and passward given, clicking Login button")

webdriver.find_element_by_id("loginForm").click()
sleep(randint(3, 6))

a = ["tech", "programmer", "techworld", "robotics"]
for q in a:
    webdriver.get("https://www.instagram.com/explore/tags/"+str(q)+"/")
    print("\n hastag submitted")

    print("\n "+webdriver.session_id)
    sleep(2)
        
    #First post of the Hastag
    webdriver.find_element_by_class_name('_9AhH0').click()
    print("First iteam selected")
    sleep(randint(2, 4))

    for n in range (1, 5):
        print("\n "+q)
        try:
            #Like Module  
            one = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div/div[1]/div[2]')
            actionChains = ActionChains(webdriver)
            actionChains.double_click(one).perform()
            sleep(3)
        
            #Comment Module  
            webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
            sleep(2)
            com2 = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
            sleep(2)
            n = randint(1, 4)
            if n == 1:
                com2.send_keys("Beautiful post. for awsome posts like this. follow @onweworld")
            elif n == 2:
                com2.send_keys("wawoo... look at me folk here : @onweworld")
            elif n == 3:
                com2.send_keys("Hey, that is super hit. hit htis, you will be blown away. @onweworld")
            else:
                com2.send_keys("Nice one..Follow @onweworld for nicer")

            sleep(randint(3, 6))
            webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
            sleep(randint(2, 5))
            print("\n "+str(n))
            
            #next  
            webdriver.find_element_by_class_name('_65Bje').click()
            sleep(randint(4, 9))
        except:
            #next  
            webdriver.find_element_by_class_name('_65Bje').click()
            sleep(randint(4, 9))
    print("\n "+q+" completed")
    sleep(3)
'''
    #Follow Module  
    webdriver.find_element_by_class_name('Ppjfr')
    sleep(1)
    two = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
    if two.text == "Follow":
        two.click()
        print("\n following successfull")
    else:
        print("already followed")
    sleep(randint(3, 4))

'''
#Unfollow Module 

webdriver.get("https://www.instagram.com/onweworld/")
sleep(randint(3, 6))
print("\n Onweworld found")

for n in range (1, 10):
    webdriver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a").click()
    sleep(randint(2,4))
    print("\n Starting unfollowing")

    for m in range (1, 6):
        webdriver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(m)+"]/div/div[3]/button").click()
        sleep(randint(6,10))
        webdriver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
        sleep(randint(8,12))
        print("\n "+str(m))

    print("\n "+str(n)+" finished")
    webdriver.refresh()
    
print("\n Unfolling Done")    

webdriver.get("https://www.instagram.com/onweworld/")
sleep(2)

webdriver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
sleep(3)

webdriver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > div:nth-child(3) > div > div.uo5MA._2ciX.tWgj8.XWrBI > div._01UL2 > div > div').click()
print("\n Log Out complete")



