Inizia anche tu a guardare grandi serie TV e film. È gratis per un mese!

https://www.netflix.com/us/n/f2f5b557-83b7-45da-94ee-da177278b4dd

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

'''opts = Options()
opts.set_headless()
assert opts.headless'''
browser = Firefox()
browser.get('http://detectportal.firefox.com')
assert "Vodafone" in browser.title
print(browser.title)

consentcookies = browser.find_element_by_class_name('acceptButton')
consentcookies.click()
time.sleep(1)
redirect_form = browser.find_element_by_link_text('Try 15 mins. Free trial >')
redirect_form.click()

print(browser.title)

email_form = browser.find_element_by_id('email')
email_form.send_keys('xueigtsdalvb@dropmail.me')
time.sleep(2)

passwd_form = browser.find_element_by_id('password')
passwd_form.send_keys('vodapwd123')
time.sleep(2)

repeat_passwd_form = browser.find_element_by_id('register_repeat-password') 
repeat_passwd_form.send_keys('vodapwd123')
time.sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

checkbox_form = browser.find_element_by_id('register_terms')
checkbox_form.click()
time.sleep(2)
submit_form = browser.find_element_by_id('signup')
submit_form.click()
time.sleep(2)

browser.close()
