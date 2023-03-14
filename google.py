from selenium import webdriver

# create a new Chrome browser
browser = webdriver.Chrome()

# navigate to the Google website
browser.get('https://www.google.com')

# close the browser
browser.quit()
#comments
