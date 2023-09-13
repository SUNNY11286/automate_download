

################################################################
##            one-drive automatic donload file                ##
################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = 'your one drive share point url!!'


class ODD_Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def run(self):
        self.driver.get(url)

        sleep(2)

        fb_btn = self.driver.find_element(
            "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div[1]/span/span[1]/button')
        fb_btn.click()
        sleep(2)
        print('xpath is found')

        popup_1 = self.driver.find_element(
            "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div[3]/div/div[1]/span/span[1]/button')
        popup_1.click()
        sleep(2)
        print('xpath 2 is found')

        # Sort by naze Z to A on website

        # //*[@id="header18-displayNameColumn_1111"]
        drop = self.driver.find_element(
            "xpath", '//*[@id="header18-displayNameColumn_1111"]')
        drop.click()
        sleep(2)
        print('xpath ', drop, ' is found')

        # /html/body/div[6]/div/div/div/div/div/div/ul/li[2]/button
        sort = self.driver.find_element(
            "xpath", '//button[normalize-space()="Z to A"]')
        sort.click()
        sleep(2)
        print('xpath ', flair, ' is found')

        num = 541

        # individual elements initiated
        for i in range(1, 542):  # total elements are 501, therefor range is from 1 to 502
            # entering elements
            id1 = self.driver.find_element(
                "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div['+str(i)+']/div/div/div[3]/div/div[1]/span/span[1]/button')
            # idx = self.driver.find_element(By.CSS_SELECTOR,"UCSF-PDGM-0473_nifti")
            id1.click()
            sleep(5)
            print('xpath ', id1, ' is found')

            # for e in id1:
            # print(id1.get_attribute("value"))

            # break

            # sleep(300)
            print('in for')

            try:
                print('in try')
                # flair donloader
                # flair = self.driver.find_element("xpath",'//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[11]/div/div/div[3]/div/div[1]/span/span[1]/button')
                # flair = self.driver.find_element(By.ID ,"UCSF-PDGM-0473_FLAIR.nii.gz")
                flair = self.driver.find_element(
                    "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % num+'_FLAIR.nii.gz"]')
                flair.click()  # titile = UCSF-PDGM-0473_FLAIR.nii.gz
                sleep(5)
                print('xpath ', flair, ' is found')
                flair = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[8]/div/div/div/div[4]/span/span[1]/button')
                # flair = self.driver.find_element("xpath",'//button[normalize-space()="Download"]')
                # //*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[8]/div/div/div/div[4]/span/span[1]/button
                flair.click()
                sleep(2)
                print('xpath ', flair, ' is found')
                flair = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[6]/button')
                # flair = self.driver.find_element("xpath",'//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[@name="Close"]/button')
                # //*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[6]/button
                flair.click()
                sleep(2)
                print('xpath ', flair, ' is found')
                #
                # TI donloader
                t1 = self.driver.find_element(
                    "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % num+'_T1.nii.gz"]')
                t1.click()
                sleep(5)
                print('xpath ', t1, ' is found')
                t1 = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[7]/div/div/div/div[4]/span/span[1]/button')
                t1.click()
                sleep(2)
                print('xpath ', t1, ' is found')
                t1 = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[6]/button')
                t1.click()
                sleep(2)
                print('xpath ', t1, ' is found')
                #
                # TIC donloader
                t1c = self.driver.find_element(
                    "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % num+'_T1c.nii.gz"]')
                # //*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[12]/div/div/div[3]/div/div[1]/span/span[1]/button
                t1c.click()
                sleep(5)
                print('xpath ', flair, ' is found')
                t1c = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[5]/div/div/div/div[4]/span/span[1]/button')
                t1c.click()
                sleep(2)
                print('xpath ', flair, ' is found')
                t1c = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[6]/button')
                t1c.click()
                sleep(2)
                print('xpath ', flair, ' is found')
                # //*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[6]/button

                #

                # T2 donloader
                t2 = self.driver.find_element(
                    "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % num+'_T2.nii.gz"]')
                t2.click()
                sleep(5)
                print('xpath ', flair, ' is found')
                t2 = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[3]/div/div/div/div[4]/span/span[1]/button')
                t2.click()
                sleep(2)
                print('xpath ', flair, ' is found')
                t2 = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[6]/button')
                t2.click()
                sleep(2)
                print('xpath ', flair, ' is found')
                #

                # segment donloader
                seg = self.driver.find_element(
                    "xpath", '//button[normalize-space()="UCSF-PDGM-'+"%04d" % num+'_tumor_segmentation.nii.gz"]')
                seg.click()
                sleep(5)
                print('xpath ', flair, ' is found')
                seg = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[1]/div/div/div/div[4]/span/span[1]/button')
                seg.click()
                sleep(2)
                print('xpath ', flair, ' is found')
                seg = self.driver.find_element(
                    "xpath", '//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[6]/button')
                seg.click()
                sleep(2)
                print('xpath ', seg, ' is found')

                sleep(15)
                num -= 1
            except:
                print('in catch')
                num -= 1

            back = self.driver.find_element(
                "xpath", '//*[@id="appRoot"]/div/div[2]/div/div/div[2]/div[2]/main/div/div/div[1]/div/div/div/div/div/div/ol/li[4]/div/div/button')
            back.click()
            sleep(2)
            print('xpath back is found')
        sleep(10)

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()


bot = ODD_Bot()
bot.run()
