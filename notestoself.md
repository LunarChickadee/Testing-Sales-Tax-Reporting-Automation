Hi! 

so, it turns out if you direct the elements correctly, the webdriver will keep doing things on the "current" page even if you've left it. So you should use element calls instead of pyautogui calls. 

in "testgetbacktowindow" you found out you can use a while loop to sit on the window until you type intot he terminal