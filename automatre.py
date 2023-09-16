

################################################################
##            one-drive automatic donload file                ##
################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

########################################################################################################################
'''
# driver.find_element_by_id(‘mainMenuRoute’).click()
# driver.find_element_by_class_name(‘custom-col’).click()
# //*[contains(@id,"ember")]/input
# //*[starts-with(@id,"ember")]/input
'''
########################################################################################################################


url = 'enter your url'

# options = webdriver.ChromeOptions() ;
# prefs = {"download.default_directory" : "<directory_path>;
# #example: prefs = {"download.default_directory" : "C:\Tutorial\down"};
# options.add_experimental_option("prefs",prefs);
# driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=options);


class ODD_Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.options = webdriver.ChromeOptions()
        # self.prefs = {"download.default_directory" : "folders/IEEE"}
        #example: prefs = {"download.default_directory" : "C:\Tutorial\down"};
        # self.options.add_experimental_option("prefs",self.prefs)
        # self.driver = webdriver.Chrome(options=self.options)

    def run(self):
        self.driver.get(url)

        sleep(3)

        fb_btn = self.driver.find_element(
            "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div[1]/span/span[1]/button')
        fb_btn.click()
        sleep(3)
        print('xpath is found')

        popup_1 = self.driver.find_element(
            "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div[3]/div/div[1]/span/span[1]/button')
        popup_1.click()
        sleep(3)
        print('xpath 2 is found')

        # Sort by naze Z to A on website
        self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight)")
        sleep(3)

        # test = self.driver.find_element(#"link text", "PKG - UCSF-PDGM-v3 copy")
        #     "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[1]/div/div/div/div/div/div/ol/li[3]/div/div/button')#driver.find_element_by_xpath("//button[@aria-label='Close Welcome Banner']").click()
        # test.click()
        # sleep(3)
        # print('xpath is found')

        # //*[@id="header18-displayNameColumn_1111"]
        drop = self.driver.find_element(
            "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/button')
        drop.click()
        sleep(3)
        print('xpath ', drop, ' is found')

        # /html/body/div[6]/div/div/div/div/div/div/ul/li[2]/button
        for i in range(1, 100):
            try:
                sort = self.driver.find_element(
                    "xpath", '//*[@id="id__'+str(i)+'-menu"]/div/ul/li[2]/button')
                sort.click()  # //*[@id="id__7-menu"]/div/ul/li[2]/button
                sleep(3)  # //*[@id="id__91-menu"]/div/ul/li[2]/button
                print('xpath ', sort, ' is found')
                print('sorted')
            except:
                # print('continued without sorting by name')
                continue
        # Accending
        drop = self.driver.find_element(
            "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/button')
        drop.click()
        sleep(3)
        print('xpath ', drop, ' is found')

        for i in range(1, 100):
            try:
                sort = self.driver.find_element(
                    "xpath", '//*[@id="id__'+str(i)+'-menu"]/div/ul/li[7]/button')
                sort.click()  # //*[@id="id__7-menu"]/div/ul/li[2]/button
                sleep(3)  # //*[@id="id__91-menu"]/div/ul/li[2]/button
                print('xpath ', sort, ' is found')
                print('sorted')
            except:
                # print('continued without sorting by name')
                continue

        # num = 541
        num = 131
        self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight)")

        # last_height = driver.execute_script("return document.body.scrollHeight")
        # while True:
        #     # Scroll down to bottom
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #     # Wait to load page
        #     time.sleep(SCROLL_PAUSE_TIME)

        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height
        # individual elements initiated

        for i in range(1, 542):  # total elements are 501, therefor range is from 1 to 502
            # entering elements
            try:
                self.driver.execute_script(
                    "window.scrollTo(0,document.body.scrollHeight)")
                sleep(2)
                print('scrolled')

                if i == num:
                    id1 = self.driver.find_element(
                        "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % i+'_nifti"]')
                    # //*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div['+str(i)+']/div/div/div[3]/div/div[1]/span/span[1]/button
                    # idx = self.driver.find_element(By.CSS_SELECTOR,"UCSF-PDGM-0473_nifti")
                    id1.click()
                    sleep(5)
                    print('xpath ', id1, ' is found:', num)
                else:
                    print('xpath ', id1, ' is finding:', num)
            except:
                if i != num:
                    print('looking for --> UCSF-PDGM-', "%04d" %
                          num, 'currently at : --> UCSF-PDGM-', "%04d" % i)
                else:
                    print(
                        'no matching folder found     -->        UCSF-PDGM-', "%04d" % i)
                # num -= 1
                # continue

            # for e in id1:
            # print(id1.get_attribute("value"))

            # break

            # sleep(300)
            print('in for')
            if i == num:
                try:
                    print('in try')

                    # flair donloader
                    # flair = self.driver.find_element("xpath",'//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[11]/div/div/div[3]/div/div[1]/span/span[1]/button')
                    # flair = self.driver.find_element(By.ID ,"UCSF-PDGM-0473_FLAIR.nii.gz")
                    try:
                        flair = self.driver.find_element(
                            "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % num+'_FLAIR.nii.gz"]')
                        flair.click()  # titile = UCSF-PDGM-0473_FLAIR.nii.gz
                        sleep(5)
                        print('flair ', flair, ' is opend')
                        for k in range(1, 20):
                            try:
                                flair = self.driver.find_element(
                                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[8]/div/div/div/div['+str(k)+']/span/span[1]/button')
                                # flair = self.driver.find_element("xpath",'//button[normalize-space()="Download"]')
                                # //*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[8]/div/div/div/div[4]/span/span[1]/button
                                flair.click()
                                sleep(3)
                                print('flair ', flair, ' is downloaded')
                                break
                            except:
                                continue  # print('can not download')
                        for k in range(1, 20):
                            try:
                                flair = self.driver.find_element(
                                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div['+str(k)+']/div[6]/button')
                                # flair = self.driver.find_element("xpath",'//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[@name="Close"]/button')
                                # //*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[6]/button
                                flair.click()
                                sleep(3)
                                print('flair ', flair, ' is closed')
                                break
                            except:
                                continue  # print('can not close')

                    except:
                        print('error downloading flair:', num)
                    #
                    # TI donloader
                    try:
                        t1 = self.driver.find_element(
                            "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % num+'_T1.nii.gz"]')
                        t1.click()
                        sleep(5)
                        print('t1 ', t1, ' is opened')
                        for k in range(1, 20):
                            try:
                                t1 = self.driver.find_element(
                                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[7]/div/div/div/div['+str(k)+']/span/span[1]/button')
                                t1.click()
                                sleep(3)
                                print('t1 ', t1, ' is downloaded')
                                break
                            except:
                                continue  # print('can not download')
                        for k in range(1, 20):
                            try:
                                t1 = self.driver.find_element(
                                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div['+str(k)+']/div[6]/button')
                                t1.click()
                                sleep(3)
                                print('t1 ', t1, ' is closed')
                                break
                            except:
                                continue  # print('can not close')
                    except:
                        print('error downloading t1:', num)

                    #
                    # TIC donloader
                    try:
                        t1c = self.driver.find_element(
                            "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % num+'_T1c.nii.gz"]')
                        # //*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[12]/div/div/div[3]/div/div[1]/span/span[1]/button
                        t1c.click()
                        sleep(5)
                        print('t1c ', t1c, ' is opened')
                        for k in range(1, 20):
                            try:
                                t1c = self.driver.find_element(
                                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[5]/div/div/div/div['+str(k)+']/span/span[1]/button')
                                t1c.click()
                                sleep(3)
                                print('t1c ', t1c, ' is downloaded')
                                break
                            except:
                                continue  # print('can not download')
                        for k in range(1, 20):
                            try:
                                t1c = self.driver.find_element(
                                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div['+str(k)+']/div[6]/button')
                                t1c.click()
                                sleep(3)
                                print('t1c ', t1c, ' is closed')
                                break
                                # //*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[6]/button
                            except:
                                continue  # print('can not close')
                    except:
                        print('error downloading t1c:', num)
                    #
                    # T2 donloader
                    try:
                        t2 = self.driver.find_element(
                            "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % num+'_T2.nii.gz"]')
                        t2.click()
                        sleep(5)
                        print('t2 ', t2, ' is opened')
                        for k in range(1, 20):
                            try:
                                t2 = self.driver.find_element(
                                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[3]/div/div/div/div['+str(k)+']/span/span[1]/button')
                                t2.click()
                                sleep(3)
                                print('t2 ', t2, ' is downloaded')
                                break
                            except:
                                continue  # print('can not download')
                        for k in range(1, 20):
                            try:
                                t2 = self.driver.find_element(
                                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div['+str(k)+']/div[6]/button')
                                t2.click()
                                sleep(3)
                                print('t2 ', t2, ' is closed')
                                break
                            except:
                                continue  # print('can not close')
                    except:
                        print('error downloading t2:', num)
                    #
                    # segment donloader
                    try:
                        seg = self.driver.find_element(
                            "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % num+'_tumor_segmentation.nii.gz"]')
                        seg.click()
                        sleep(5)
                        print('seg ', seg, ' is opened')
                        for k in range(1, 20):
                            try:
                                seg = self.driver.find_element(
                                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[1]/div/div/div/div['+str(k)+']/span/span[1]/button')
                                seg.click()
                                sleep(3)
                                print('seg ', seg, ' is downloaded')
                                break
                            except:
                                continue  # print('can not download')
                        for k in range(1, 20):
                            try:
                                seg = self.driver.find_element(
                                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div['+str(k)+']/div[6]/button')
                                seg.click()
                                sleep(3)
                                print('seg ', seg, ' is closed')
                                break
                            except:
                                continue  # print('can not close')
                    except:
                        print('error downloading seg:', num)

                    sleep(15)
                    # num -= 1

                    # back = self.driver.find_element(
                    #     "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[1]/div/div/div/div/div/div/ol/li[4]/div/div/button')
                    # back.click()
                    # sleep(3)
                    # print('xpath back is found')

                except:
                    print('in catch')
                    # num -= 1

                # if num==i:
                num += 1
                print(num)
                # for b in range(1,20):
                #     try:

                # sleep(300)#//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[1]/div/div/div/div/div/div/ol/li[2]/div/div/button
                # b=5 #//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[1]/div/div/div/div/div/div/ol/li[4]/div/div/button
                # if b!=3:
                back = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[1]/div/div/div/div/div/div/ol/li[4]/div/div/button')
                back.click()
                sleep(3)
                print('xpath back is found')
                #         break
                # except:
                #     print('can not go back')
            else:
                continue

        sleep(10)

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()


bot = ODD_Bot()
bot.run()


# from selenium import webdriver
# import time

# browser=webdriver.Chrome()
# browser.get("https://pythonbasics.org/selenium-scroll-down/")
# time.sleep(5)
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(5)
# browser.close()


# # import module
# from selenium import webdriver
# import time

# # Create the webdriver object. Here the
# # chromedriver is present in the driver
# # folder of the root directory.
# driver = webdriver.Chrome()

# # get https://www.geeksforgeeks.org/
# driver.get("https://sqa.stackexchange.com/questions/35564/python-selenium-find-button")

# # Maximize the window and let code stall
# # for 10s to properly maximise the window.
# driver.maximize_window()
# time.sleep(10)

# # Obtain button by link text and click.
# button = driver.find_element("link text","Sign up")
# button.click()
