import win32api, win32con
import time, random
#from pynput import ket,listener
from pynput import keyboard
from threading import Thread
import pyautogui
import ctypes
from pynput.mouse import Button, Controller
mouse = Controller()
from pymouse import PyMouse
m = PyMouse()
i = 0
ThreadL = []
Start= False
x = 2038
y = 855
Boosters = [[1291, 654], [1326, 654], [1354, 654]]
Potion = [652, 845]
Dung80 = [[684, 842], [1807,609], [1838, 610], [1871, 610], [2274, 997], [2305, 997]]
MOUSEEVENTF_RIGHTDOWN = 0x0008 # right button down 
MOUSEEVENTF_RIGHTUP = 0x0010 # right button up


def click(xcord, ycord):
    global i
    xcord = xcord + random.randint(-5, 5)
    ycord = ycord + random.randint(-5, 5)
    win32api.SetCursorPos((xcord,ycord))
    """
    time.sleep(random.uniform(0.6, 1.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,xcord,ycord,0,0)
    t1 = time.time()
    time.sleep(random.uniform(0.1, 0.3))
    #print time.time() - t1
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,xcord,ycord,0,0)
    """
    '''
    time.sleep(random.uniform(0.6, 1.3))
    pyautogui.mouseDown(button='right')
    t1 = time.time()
    time.sleep(random.uniform(0.1, 0.3))
    #print time.time() - t1
    pyautogui.mouseUp(button='right')
    '''
    '''
    time.sleep(random.uniform(0.6, 1.3))
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN) # left down
    t1 = time.time()
    time.sleep(random.uniform(0.1, 0.3))
    #print time.time() - t1
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP)
    '''
    '''
    time.sleep(random.uniform(0.6, 1.3))
    mouse.press(Button.right)
    t1 = time.time()
    time.sleep(random.uniform(0.1, 0.3))
    #print time.time() - t1
    mouse.release(Button.right)
    '''
    time.sleep(random.uniform(0.6, 1.3))
    #mouse.press(Button.right)
    m.press(2038, 855, 2)
    t1 = time.time()
    time.sleep(random.uniform(0.1, 0.3))
    m.release(2038, 855, 2)
    #print time.time() - t1
    #mouse.release(Button.right)
    #print xcord, ycord
    #i += 1
    #if (i%100 == 0):
    #    for x in Boosters:
    #        win32api.SetCursorPos((x[0],x[1]))
    #        time.sleep(random.uniform(0.3, 0.7))
    #        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,xcord,ycord,0,0)
    #        time.sleep(random.uniform(0.3, 0.7))
    #        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,xcord,ycord,0,0)
    #        time.sleep(random.uniform(0.1, 0.3))
    #        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,xcord,ycord,0,0)
    #print i
def clickDung():
    for cord in Dung80:
        xcord = cord[0] + random.randint(-5, 5)
        ycord = cord[1] + random.randint(-5, 5)
        win32api.SetCursorPos((xcord,ycord))
        time.sleep(random.uniform(0.1, 0.3))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,xcord,ycord,0,0)
        time.sleep(random.uniform(0.150, 0.3))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,xcord,ycord,0,0)
        
def GetMousePos():
    x,y = win32api.GetCursorPos()
    print x, y

def start_click():
    global Start
    while Start == True:
        click(x, y)
        #clickDung()

def on_press(key):
    global i, Start
    try:
        if str(key) == 'Key.f5':
            Start = True
            ThreadL.append(Thread(target=start_click, args=()))
            ThreadL[len(ThreadL)-1].start()
            print 'Start'
        if str(key) == 'Key.f8':
            GetMousePos();
            
        if str(key) == 'Key.f9':
            Start = False
            ThreadL[len(ThreadL)-1].join()
            print 'Stop'
            
        
    except AttributeError:
        print(key)

def on_release(key):
    pass
    #print('{0} released'.format(
     #   key))
    #if key == keyboard.Key.esc:
        # Stop listener
     #   return False

# Collect events until released
def Listener():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    

t1 = Thread(target=Listener, args=())
t1.start()

t2 = Thread(target=start_click, args=())
#t2.start()

t3 = Thread(target=click, args=(x, y))
#t3.start()
    

