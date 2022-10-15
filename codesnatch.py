import cv2
import numpy as np
import pytesseract
import pyautogui
import pyperclip
import os, sys

from PIL import ImageGrab, ImageOps
import time
import re
from pynput import keyboard

# Maually Configure Postions (True - All Values must be entered in config(), False - You'll get a small Setup-Wizard)
enable_manual_config = False # False automatic

def config():
    if enable_manual_config == True:

# -------- Configure Manually ------------------
        # Corner 1
        x1, x2 = 0,0
        # Corner 2
        x2, y2 = 0,0
        # Textbox (Codefield)
        xt, yt = 0,0
        # Redeem Button
        xr, yr = 0,0

        # For some places like EpicGames you need to confirm the redeem
        xc, yc = 0,0

        return x1,y1,x2,y2,xt,yt,xr,yr,xc,yc

# --------- End of Manual Configuration ---------


    # Starts Auto-Config
    elif enable_manual_config == False:
        print('-----------------------------------')
        print('   Welcome to the Code-Snatcher    ')
        print('-----------------------------------\n')
        print('To get started you have to point your mouse in the first corner\nwhere the codes would appear and confirm with the ESC-Key')
        wait_for_esc()
        x1,y1 = pyautogui.position()
        print('Corner 1 set. Now move to the 2nd corner and confirm with ESC')
        wait_for_esc()
        x2,y2 = pyautogui.position()
        print('Well done, second corner set. Now do the same with the text box to input the code')
        wait_for_esc()
        xt,yt = pyautogui.position()
        print('Now find the redeem button')
        wait_for_esc()
        xr,yr = pyautogui.position()
        print('And lastly the confirm button')
        wait_for_esc()
        xc,yc = pyautogui.position()
        clearConsole()
        print('----------------------------------------------------')
        print('Got Following Positions:')
        print('Corner 1 x: %s y: %s , Corner 2: x: %s y: %s'%(str(x1),str(y1),str(x2),str(y2)))
        print('Textbox x: %s y: %s , RedeemBtn: x: %s y: %s'%(str(xt),str(yt),str(xr),str(yr)))
        print('Confirm Button x: %s y: %s'%(str(xc),str(yc)))
        print('----------------------------------------------------\n')
        return x1,y1,x2,y2,xt,yt,xr,yr,xc,yc

# Listening for ESC
def on_press(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
def wait_for_esc():
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()

# OS Check
TESSERACT_DIR = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if sys.platform == "linux" or sys.platform == "darwin":
    pytesseract.pytesseract.tesseract_cmd = "tesseract"
else:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_DIR

# Initializing OCR
def ocr_scan(x1,y1,x2,y2):
    # Sets OCR positon
    cap = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    # Set Scanning into Grayscale
    gray = ImageOps.grayscale(cap)
    # Generates a Numpy Array
    cap_arr = np.array(gray)
    # Shows OCR Window (Comment out if dont needed)
    cv2.imshow("", cap_arr)
    # Picks Text from Image
    text = pytesseract.image_to_string(cap_arr)
    text = text.strip()
    return text

def search_code(scan):
    # Defines RegEx for Epic-Codes
    regepic = re.compile("((\S{5}-){3})\S{5}")
    try:
        epic = regepic.search(scan).group()
        # Checks and returns the Epic Code
        if re.match('((\S{5}-){3})\S{5}',epic):
            return epic
        else:
            return ''
    except:
        return ''

def input_code(code, xt,yt,xr,yr,xc,yc):
    # Moves Mouse to the Textbox
    pyautogui.moveTo(xt,yt)
    pyautogui.leftClick()
    time.sleep(0.1)
    # Types in the code
    pyperclip.copy(code)
    pyautogui.hotkey('ctrl', 'v')
    # Moves to Redeem Button
    pyautogui.moveTo(xr,yr)
    pyautogui.leftClick()
    # Moves and clicks Confirm
    pyautogui.moveTo(xc,yc)
    pyautogui.leftClick()
    #done

# Defines clearConsole to clear the Console
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

x1,y1,x2,y2,xt,yt,xr,yr,xc,yc = config()

while True:

    scanned = ocr_scan(x1,y1,x2,y2)

    if len(scanned)>20:
        print(scanned)

    code = search_code(scanned)

    if code != '':
        input_code(code, xt,yt,xr,yr,xc,yc)
        time.sleep(5)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()




