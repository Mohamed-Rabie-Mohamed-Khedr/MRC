import pynput
import time

run = True
speed = 13
mouseC = pynput.mouse.Controller()

def on_press(key):
     global run
     if run:
          if key == pynput.keyboard.Key.up:
               mouseC.move(0, -speed)
          elif key == pynput.keyboard.Key.down:
               mouseC.move(0, speed)
          elif key == pynput.keyboard.Key.right:
               mouseC.move(speed, 0)
          elif key == pynput.keyboard.Key.left:
               mouseC.move(-speed, 0)
          elif key == pynput.keyboard.Key.insert:
               mouseC.click(pynput.mouse.Button.left)
          elif key == pynput.keyboard.Key.end:
               mouseC.click(pynput.mouse.Button.right)
          elif key == pynput.keyboard.Key.ctrl_r:
               if not mouseC.press(pynput.mouse.Button.left):
                    mouseC.press(pynput.mouse.Button.left)
               else:
                    mouseC.release(pynput.mouse.Button.left)

     if key == pynput.keyboard.Key.ctrl_l:
          run = not run

l = pynput.keyboard.Listener(on_press=on_press)
l.start()

while True:
     time.sleep(1000000)