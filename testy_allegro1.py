# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
#dla klawisza Enter
from selenium.webdriver.common.keys import Keys

class CheckRozne(unittest.TestCase):

    #metoda setUp jest odpalana PRZED każdym z testów
    def setUp(self):
        #ścieżka do pliku z chromedriver
        self.driver=webdriver.Chrome(executable_path=r"D:\TestFiles\chromedriver.exe")
        driver=self.driver
        self.driver.maximize_window()
        #czas w sekundach jaki ma czekać proces na wyświetlenie się elementu na stronie
        self.driver.implicitly_wait(10)
        self.driver.get("https://allegro.pl/")

    #metoda testowa rozpoznawana jest po występowaniu w jej nazwie słowa "test"
    def test_inputtest(self):
        driver=self.driver
        #wciśnij "Nie zgadzam się" w wyskakującym oknie pytania o pliki cookie na stronie allegro
        driver.find_element_by_xpath("/ html / body / div[4] / div / div[2] / div / div / div / div[2] / div / div[1] / button").click()
        #pole Szukaj na stronie allegro
        element_Szukaj=driver.find_element_by_xpath('/html/body/div[3]/div[2]/nav/div/div[1]/div/form/input')
        #print('OTTO:'+element_szukaj.text)
        #wpisz "oko" w pole Szukaj
        element_Szukaj.send_keys("oko")
        #zatwierdź wpisaną wartość w polu szukaj Enterem
        #driver.find_element_by_xpath('/html/body/div[3]/div[2]/nav/div/div[1]/div/form/input').send_keys(Keys.ENTER)
        element_Szukaj.send_keys(Keys.ENTER)
        #driver.find_element_by_xpath("/html/body/div[3]/div[2]/nav/div/div[1]/div/form/button/svg/image").click()

    # metoda tearDown jest odpalana PO każdym z testów
    def tearDown(self):
        #zamyka przeglądarkę
        self.driver.quit()
#poniższe uruchamia zestaw testów
if __name__=="__main__":
    unittest.main()



