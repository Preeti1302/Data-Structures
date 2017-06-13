import unittest
from selenium import webdriver
import time 
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
import sys

class SearchTests(unittest.TestCase):
    global ip,cloudname
    sys.stdout.write("Enter IP address: ")
    sys.stdout.flush()
    ip = sys.stdin.readline()
    print("you entered: " + ip) 
    sys.stdout.write("Enter the cloudname: ")
    sys.stdout.flush()
    cloudname = sys.stdin.readline()
    print("you entered: " + cloudname) 
                                 
        
    
    @classmethod
    def setUpClass(cls): 
        
        cls.driver=webdriver.Chrome()
        
        
        cls.driver.get("http://" +ip+ "/za")
        
    def test_login(self):
        
        
        self.search_field=self.driver.find_element_by_name("loginName")
        self.search_field.clear()
        self.search_field.send_keys("admin@" +cloudname)
        time.sleep(3)
        
        search_field=self.driver.find_element_by_name("password")
        search_field.clear()        
        search_field.send_keys("admin")
        time.sleep(3)
        
        search_field=self.driver.find_element_by_name("submit")
        search_field.click()
        time.sleep(3)

        self.driver.find_element(by=By.XPATH, value='//*[@id="r"]/table[1]/tbody/tr[1]/td[3]/a[2]/img').click()
        time.sleep(3)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="r"]/table[1]/tbody/tr[1]/td[3]/a[2]/img').click()
        time.sleep(3)
        
        search_field=self.driver.find_element_by_name("name")
        search_field.clear()        
        search_field.send_keys("shaunak12345")
        
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="r"]/form/table[1]/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/select').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="r"]/form/table[1]/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/select/option[1]').click()
        
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="r"]/form/table[1]/tbody/tr[3]/td/table/tbody/tr[3]/td[4]/select').click()
        
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="r"]/form/table[1]/tbody/tr[3]/td/table/tbody/tr[3]/td[4]/select/option[4]').click()
        


        search_field=self.driver.find_element_by_name("domains")
        search_field.clear()        
        search_field.send_keys("shaunak12345.com")
        
        
        search_field=self.driver.find_element_by_name("admPwd")
        search_field.clear()        
        search_field.send_keys("Zscaler123#")
        time.sleep(5)
        
        search_field=self.driver.find_element_by_name("admPwd2")
        search_field.clear()        
        search_field.send_keys("Zscaler123#")
        
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="r"]/form/table[1]/tbody/tr[5]/td/table/tbody/tr[3]/td[4]/select').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="r"]/form/table[1]/tbody/tr[5]/td/table/tbody/tr[3]/td[4]/select/option[2]').click()
        time.sleep(1)
    
        self.driver.find_element(by=By.XPATH, value='//*[@id="sec1_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="sec1_status"]/option[2]').click()
        time.sleep(1)
        
        search_field=self.driver.find_element_by_name("sec1_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
        
        #works fine till above
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="sec2_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="sec2_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("sec2_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
        #Manage-Standard
        self.driver.find_element(by=By.XPATH, value='//*[@id="man1_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="man1_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("man1_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
        
        #manage-advanced
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="man2_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="man2_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("man2_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
        
        #manage-bw-control
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="man3_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="man3_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("man3_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    #Comply
    
        self.driver.find_element(by=By.XPATH, value='//*[@id="com1_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="com1_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("com1_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    #Analyze
        self.driver.find_element(by=By.XPATH, value='//*[@id="ana1_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="ana1_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("ana1_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
        
    #Zscaler SyncBridge Agent
        self.driver.find_element(by=By.XPATH, value='//*[@id="sync_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="sync_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("sync_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    #VPN-site-to-site
        self.driver.find_element(by=By.XPATH, value='//*[@id="s2s_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="s2s_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("s2s_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
    #Zscaler ez Agent
        self.driver.find_element(by=By.XPATH, value='//*[@id="ezagent_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="ezagent_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("ezagent_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
    #Zscaler Report Builder
        self.driver.find_element(by=By.XPATH, value='//*[@id="rptBldr_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="rptBldr_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("rptBldr_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
    
    #Dedicated-Proxy-ports
        self.driver.find_element(by=By.XPATH, value='//*[@id="ddctPort_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="ddctPort_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("ddctPort_portCount")
        search_field.clear()        
        search_field.send_keys("2")
        time.sleep(2)
    
        search_field=self.driver.find_element_by_name("ddctPort_stdt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2017")
        time.sleep(2)
    
        
        search_field=self.driver.find_element_by_name("ddctPort_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
    
    #Custom Root Cert
        self.driver.find_element(by=By.XPATH, value='//*[@id="customCert_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="customCert_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("customCert_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
        
        
    #ZscalerApp
        self.driver.find_element(by=By.XPATH, value='//*[@id="mobSecAgent_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="mobSecAgent_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("mobSecAgent_stdt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2017")
        time.sleep(2)
    
        
        search_field=self.driver.find_element_by_name("mobSecAgent_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    #Zscaler Auth Bridge
        self.driver.find_element(by=By.XPATH, value='//*[@id="zab_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="zab_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("zab_stdt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2017")
        time.sleep(2)
    
        
        search_field=self.driver.find_element_by_name("zab_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    #Cloud Sandbox
        self.driver.find_element(by=By.XPATH, value='//*[@id="baPolicy_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="baPolicy_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("baPolicy_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    #FW Basic
        self.driver.find_element(by=By.XPATH, value='//*[@id="firewallBasic_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="firewallBasic_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("firewallBasic_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
    #FW Advanced
        self.driver.find_element(by=By.XPATH, value='//*[@id="firewallAdvanced_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="firewallAdvanced_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("firewallAdvanced_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
    #FW Full Loggin
        self.driver.find_element(by=By.XPATH, value='//*[@id="firewallExtLog_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="firewallExtLog_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("firewallExtLog_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
    #nss status
        self.driver.find_element(by=By.XPATH, value='//*[@id="nss_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="nss_status"]/option[2]').click()
        time.sleep(1)
        
        
        search_field=self.driver.find_element_by_name("nss_stdt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2017")
        time.sleep(2)
        
        search_field=self.driver.find_element_by_name("nss_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
    #nss Firewall Log
        #self.driver.find_element(by=By.XPATH, value='//*[@id="nssFirewallLog_status"]').click()
        #time.sleep(1)
        
        #self.driver.find_element(by=By.XPATH, value='//*[@id="nssFirewallLog_status"]/option[2]').click()
        #time.sleep(1)
        
        #search_field=self.driver.find_element_by_name("nssFirewallLog_empCount")
        #search_field.clear()        
        #search_field.send_keys("1")
        #time.sleep(2)
    
        #search_field=self.driver.find_element_by_name("nssFirewallLog_stdt")
        #search_field.clear()        
        #search_field.send_keys("08-Jun-2017")
        #time.sleep(2)
    
    
        #search_field=self.driver.find_element_by_name("nssFirewallLog_enddt")
        #search_field.clear()        
        #search_field.send_keys("08-Jun-2020")
        #time.sleep(2)
    
    
    #vzen small
        self.driver.find_element(by=By.XPATH, value='//*[@id="vzen_status_small"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="vzen_status_small"]/option[2]').click()
        time.sleep(1)
        
        search_field=self.driver.find_element_by_name("vzen_empCount_small")
        search_field.clear()        
        search_field.send_keys("2")
        time.sleep(2)
    
        search_field=self.driver.find_element_by_name("vzen_stdt_small")
        search_field.clear()        
        search_field.send_keys("08-Jun-2017")
        time.sleep(2)
    
    
        search_field=self.driver.find_element_by_name("vzen_enddt_small")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    #vzen medium
        self.driver.find_element(by=By.XPATH, value='//*[@id="vzen_status_medium"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="vzen_status_medium"]/option[2]').click()
        time.sleep(1)
        
        search_field=self.driver.find_element_by_name("vzen_empCount_medium")
        search_field.clear()        
        search_field.send_keys("2")
        time.sleep(2)
    
        search_field=self.driver.find_element_by_name("vzen_stdt_medium")
        search_field.clear()        
        search_field.send_keys("08-Jun-2017")
        time.sleep(2)
    
    
        search_field=self.driver.find_element_by_name("vzen_enddt_medium")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    #vzen large
        self.driver.find_element(by=By.XPATH, value='//*[@id="vzen_status_large"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="vzen_status_large"]/option[2]').click()
        time.sleep(1)
        
        search_field=self.driver.find_element_by_name("vzen_empCount_large")
        search_field.clear()        
        search_field.send_keys("2")
        time.sleep(2)
    
        search_field=self.driver.find_element_by_name("vzen_stdt_large")
        search_field.clear()        
        search_field.send_keys("08-Jun-2017")
        time.sleep(2)
    
    
        search_field=self.driver.find_element_by_name("vzen_enddt_large")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
    #ICAP
        self.driver.find_element(by=By.XPATH, value='//*[@id="icap_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="icap_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("icap_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
    #ICAP - Response
        self.driver.find_element(by=By.XPATH, value='//*[@id="icap_response_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="icap_response_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("icap_response_stdt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2017")
        time.sleep(2)
    
        search_field=self.driver.find_element_by_name("icap_response_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    #Cloud Identity Broker
        self.driver.find_element(by=By.XPATH, value='//*[@id="cIdBroker_status"]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="cIdBroker_status"]/option[2]').click()
        time.sleep(1)
    
        search_field=self.driver.find_element_by_name("cIdBroker_enddt")
        search_field.clear()        
        search_field.send_keys("08-Jun-2020")
        time.sleep(2)
    
    
        self.search_field=self.driver.find_element_by_name("businessContactName")
        self.search_field.clear()
        self.search_field.send_keys("shaunak123")
        time.sleep(1)
        
        
        self.search_field=self.driver.find_element_by_name("businessContactEmail")
        self.search_field.clear()
        self.search_field.send_keys("admin@shaunak123.com")
        time.sleep(1)
        
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="b1"]').click()
        time.sleep(6)
        
        
    @classmethod
    def tearDownClass(cls):  
        cls.driver.quit()
        
     
     
        
if __name__=='__main__':
    unittest.main()
    
    
    
    


