#Copyright Maximilian Oancea (2018) All rights reservered.

from selenium import webdriver
import os
import time


driver = webdriver.Firefox()
driver.get("https://www.brd.ro/en/exchange-rates")
#extract cursuri Fx in functie de xpath
fxcpv = driver.find_elements_by_xpath('//*[@id="tabAccountExchangeRates"]/div/div[1]/div[4]/p')
fxcbuy = driver.find_elements_by_xpath('//*[@id="tabAccountExchangeRates"]/div/div[1]/div[6]/p')
fxcsell = driver.find_elements_by_xpath('//*[@id="tabAccountExchangeRates"]/div/div[1]/div[7]/p')
#//*[@id="tabAccountExchangeRates"]/div/div[1]/div[7]/p[2]
# print out all the values ; changed value to 8 because some values were null
num_page_itmes = 2
for i in range(num_page_itmes):            
    print(fxcpv[i].text + " , " + fxcbuy[i].text +" , " + fxcsell[i].text)
    
        
with open('Cursuri.csv','w+') as output:
     for i in range(num_page_itmes): 
       data = fxcpv[i].text + " , " + fxcbuy[i].text +" , " + fxcsell[i].text + '\n'
       output.write(str(data))
 
driver.get("https://www.unicredit.ro/ro/institutional/Diverse/SchimbValutar.html")
Fxc_unicreditc = driver.find_elements_by_xpath('//*[@id="currency_list_table"]/tr[1]/td[1]')
Fxc_unicreditb = driver.find_elements_by_xpath('//*[@id="currency_list_table"]/tr[1]/td[3]')
Fxc_unicredits = driver.find_elements_by_xpath('//*[@id="currency_list_table"]/tr[1]/td[4]')
#//*[@id="currency_list_table"]/tr[1]

num_page_itmes = len(Fxc_unicreditc)
with open('Cursuri.csv','a') as output:
      for i in range(num_page_itmes): 
          unicredit ="Unicredit Bank" + '\n'+ Fxc_unicreditc[i].text + " , " +Fxc_unicreditb[i].text +" , " + Fxc_unicredits[i].text 
          print(unicredit)
          output.write(str(unicredit))
 

driver.get("https://www.alphabank.ro/ro-ro/info-utile/cursuri-valutare/cursuri-valutare")
fxc_alphabank = driver.find_elements_by_xpath('//*[@id="dnn_ctr2756_ModuleContent"]/div[2]/table[1]/tbody/tr[9]/td[1]')
fxb_alphabank = driver.find_elements_by_xpath('//*[@id="dnn_ctr2756_ModuleContent"]/div[2]/table[1]/tbody/tr[9]/td[3]')
fxs_alphabank = driver.find_elements_by_xpath('//*[@id="dnn_ctr2756_ModuleContent"]/div[2]/table[1]/tbody/tr[9]/td[4]')  
num_page_itmes = len(fxc_alphabank)
with open('Cursuri.csv','a') as output:
      for i in range(num_page_itmes): 
          alphabank ='\n'+"AlphaBank" + '\n'+ fxc_alphabank[i].text + " , " +fxb_alphabank[i].text +" , " + fxs_alphabank[i].text 
          print(alphabank)
          output.write(str(alphabank))
 
    
driver.get("https://www.bancatransilvania.ro/curs-valutar-spot/")
fxc_tran = driver.find_elements_by_xpath('/html/body/section[1]/div[1]/div[2]/table[2]/tbody/tr[2]/td[1]')
fxb_tran = driver.find_elements_by_xpath('/html/body/section[1]/div[1]/div[2]/table[2]/tbody/tr[2]/td[3]')
fxs_tran = driver.find_elements_by_xpath('/html/body/section[1]/div[1]/div[2]/table[2]/tbody/tr[2]/td[4]')  
num_page_itmes = len(fxc_tran)
with open('Cursuri.csv','a') as output:
      for i in range(num_page_itmes): 
          tran ='\n'+"Transilvania Bank" + '\n'+'EUR'+ " , " +fxb_tran[i].text +" , " + fxs_tran[i].text 
          print(tran)
          output.write(str(tran))
           
driver.get("https://www.ing.ro/ing-in-romania/informatii-utile/curs-valutar")
fxc_ingb = driver.find_elements_by_xpath('//*[@id="exchange-first-tab"]/table/tbody/tr[1]/td[2]')
fxb_ingb = driver.find_elements_by_xpath('//*[@id="exchange-first-tab"]/table/tbody/tr[1]/td[3]')
fxs_ingb = driver.find_elements_by_xpath('//*[@id="exchange-first-tab"]/table/tbody/tr[1]/td[4]')  
num_page_itmes = len(fxc_ingb)
with open('Cursuri.csv','a') as output:
      for i in range(num_page_itmes): 
          ingb ='\n'+"ING Bank" + '\n'+ fxc_ingb[i].text + " , " +fxb_ingb[i].text +" , " + fxs_ingb[i].text 
          print(ingb)
          output.write(str(ingb))
          
driver.get("https://www.cec.ro/curs-valutar")
fxc_cecc = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/section/div[3]/table/tbody/tr[5]/td[2]')
fxb_cecc = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/section/div[3]/table/tbody/tr[5]/td[4]')
fxs_cecc = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/section/div[3]/table/tbody/tr[5]/td[5]')  
num_page_itmes = len(fxc_cecc)
with open('Cursuri.csv','a') as output:
      for i in range(num_page_itmes): 
          cecc ='\n'+"CEC Bank" + '\n'+ fxc_cecc[i].text + " , " +fxb_cecc[i].text +" , " + fxs_cecc[i].text 
          print(cecc)
          output.write(str(cecc))

driver.get("https://www.otpbank.ro/curs-valutar")
fxc_otpr = driver.find_elements_by_xpath('//*[@id="cursCurrent"]/table/tbody/tr[1]/td[1]')
fxb_otpr = driver.find_elements_by_xpath('//*[@id="cursCurrent"]/table/tbody/tr[1]/td[3]')
fxs_otpr = driver.find_elements_by_xpath('//*[@id="cursCurrent"]/table/tbody/tr[1]/td[4]')  
num_page_itmes = len(fxc_otpr)
with open('Cursuri.csv','a') as output:
      for i in range(num_page_itmes): 
          otpr ='\n'+"OTP Bank" + '\n'+ fxc_otpr[i].text + " , " +fxb_otpr[i].text +" , " + fxs_otpr[i].text 
          print(otpr)
          output.write(str(otpr))
          
driver.get("http://www.piraeusbank.ro/Banca/Unelte/Istoric-Curs-Valutar.html")
fxc_pirb = driver.find_elements_by_xpath('//*[@id="ctl00_contentPlaceHolder_ctl02_gvIstoricCursValutar_ctl02_lbCodValuta"]')
fxb_pirb = driver.find_elements_by_xpath('//*[@id="ctl00_contentPlaceHolder_ctl02_gvIstoricCursValutar_ctl02_lbCumparare"]')
fxs_pirb = driver.find_elements_by_xpath('//*[@id="ctl00_contentPlaceHolder_ctl02_gvIstoricCursValutar_ctl02_lbVanzare"]')  
num_page_itmes = len(fxc_pirb)
with open('Cursuri.csv','a') as output:
      for i in range(num_page_itmes): 
          pirb ='\n'+"Piraeus Bank" + '\n'+ fxc_pirb[i].text + " - " +fxb_pirb[i].text +" - " + fxs_pirb[i].text 
          pirb = pirb.replace(",",".")
          pirb = pirb.replace("-",",")
          print(pirb)
          output.write(str(pirb))
try:          
    driver.get("https://www.raiffeisen.ro/persoane-fizice/curs-valutar/")
    fxc_rbrb = driver.find_elements_by_xpath('//*[@id="_0"]/td[2]')
    fxb_rbrb = driver.find_elements_by_xpath('//*[@id="_0"]/td[4]')
    fxs_rbrb = driver.find_elements_by_xpath('//*[@id="_0"]/td[5]')  
    num_page_itmes = len(fxc_rbrb)
    with open('Cursuri.csv','a') as output:
          for i in range(num_page_itmes): 
              rbrb ='\n'+"Raiffeisen Bank" + '\n'+ fxc_rbrb[i].text + " - " +fxb_rbrb[i].text +" - " + fxs_rbrb[i].text 
              rbrb = rbrb.replace(",",".")
              rbrb = rbrb.replace("-",",")
              print(rbrb)
              output.write(str(rbrb))
except:
    pass
try:           
    driver.get("https://www.bcr.ro/ro/curs-valutar")
    fxc_bcr= driver.find_elements_by_xpath('//*[@id="content"]/div[4]/div/div/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[2]')
    fxb_bcr = driver.find_elements_by_xpath('//*[@id="content"]/div[4]/div/div/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[3]')
    fxs_bcr = driver.find_elements_by_xpath('//*[@id="content"]/div[4]/div/div/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[4]')  
    num_page_itmes = len(fxc_bcr)
    with open('Cursuri.csv','a') as output:
          for i in range(num_page_itmes): 
              bcr ='\n'+"Banca Comerciala Romana" + '\n'+ fxc_bcr[i].text + " - " +fxb_bcr[i].text +" - " + fxs_bcr[i].text 
              bcr = bcr.replace(",",".")
              bcr = bcr.replace("-",",")
              print(bcr)
              output.write(str(bcr))
except:
    pass          
          
driver.close()
path1 = 'C:\Data\Cursuri\\' + time.strftime("%Y%m%d%H%M%S.csv")
os.rename("Cursuri.csv", path1)
