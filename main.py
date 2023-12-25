import pyperclip
import time

old = ''
while True:
    s = pyperclip.paste()
    if s != old:
        with open('user_copy.txt', 'w') as file:
            file.write(s + '\n')
            old = s
    time.sleep(1)
