import cv2
import numpy as np
import pyautogui
from tkinter import *
from threading import Thread
global running
running=False
def screen_rec(size=pyautogui.size(),fps=20.0):
  global running
  running=True
  status.insert(END,"File will be saved at: \n"+vpath+"\n")
  fourcc= cv2.VideoWriter_fourcc(*"XVID")
  out=cv2.VideoWriter(vpath,fourcc, fps, (size))
  status.insert(END,"Recording...\n")
  i=0
  while True:
    img=pyautogui.screenshot()
    frame=np.array(img)
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    i=i+1
    if stop==1:
      break
  status.insert(END,"Recording Completed\nFile Saved at "+vpath+"\n")
  status.insert(END,str(int(i/20))+"seconds.\n\n")
  cv2.destroyAllWindows()
  out.release()
def start_thread():
  global stop
  stop=0
  global vpath
  vpath=path.get()
  if running==False:
    t=Thread(target =screen_rec)
    t.start()
def stop():
  global stop
  stop=1
  global running
  running=False
root=Tk()
root.title("PyScreen")
root.geometry("290x235")
app=Frame(root)
app.grid()

path=Entry(app)
path.insert(0,"output.avi")
path.pack(side=TOP,anchor=N, fill=X)

fmb=Frame(app)
start=Button(fmb, text="START REC", command=start_thread).pack(side=LEFT,ipadx=30)
stop=Button(fmb, text="STOP REC", command=stop).pack(side=LEFT,ipadx=30)
fmb.pack(side=TOP,pady=5)

fms=Frame(app)
status=Text(fms, height=10, width =30)
scroll=Scrollbar(fms, command=status.yview)
status.configure(yscrollcommand=scroll.set)
status.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
status.insert(END,"##Welcome to PyScreen##\nStatus::\n")
fms.pack(side=BOTTOM)
root.mainloop()
