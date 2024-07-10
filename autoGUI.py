import pyautogui
import time

# Pause for 2 seconds before starting
time.sleep(2)

# Move the mouse to (100, 100) and click
pyautogui.moveTo(1000, 1000)
pyautogui.click()

# Type "Hello, world!" with a short interval between each character
pyautogui.write('Hello, world!', interval=0.1)

# Press the Enter key
pyautogui.press('enter')

# Take a screenshot and save it
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')




### takes screenshot after every 10 sec
import pyautogui
import time

for i in range(5):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    # Save the screenshot with a unique name
    screenshot.save(f'screenshot_{i}.png')
    # Wait for 10 seconds
    time.sleep(10)

