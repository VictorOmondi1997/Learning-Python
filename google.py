from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Downloads\\Compressed\\chromedriver.exe")

driver.get("file:///C:/Users/user/Documents/Vick/index.html")
# driver.find_element_by_id("fullname").send_keys("Victor Omondi")
# driver.find_element_by_id("email").send_keys("vick@victoromondi.ml")
# driver.find_element_by_id("message").send_keys("Hi Vick! I was requesting you to send me the resources for todays meetup")
driver.find_element_by_id("submit").click()
html = driver.page_source
print(html)