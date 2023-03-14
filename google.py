import webbrowser

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
url = 'https://www.google.com'
webbrowser.get(chrome_path).open(url)

#hello