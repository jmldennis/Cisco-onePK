# John Mark Dennis - 2015
# Tested running Python 2.7.8
# Simple App used with Raspberry Pi to display basic router
# status information using Tkinter
# Be sure to grab to python SDK off Cisco Developer Network

from onep.element.NetworkElement import NetworkElement  
from onep.element.SessionConfig import SessionConfig  
from onep.core.util import tlspinning
from Tkinter import *
from threading import *

router_ip = "192.168.1.110"
connection_name = "Internet Status"
username = "cisco"
password = "cisco"
width = 1024
height = 768
ne = NetworkElement(router_ip,connection_name)
connected = 0
pixel = width/100
origin_pixel = [width/6,height/2]
position = origin_pixel
logo_stage = 0
  
# TLS Connection
class PinningHandler(tlspinning.TLSUnverifiedElementHandler):  
   def __init__(self, pinning_file):  
       self.pinning_file = pinning_file  
   def handle_verify(self, host, hashtype, finger_print, changed):  
       return tlspinning.DecisionType.ACCEPT_ONCE  

#Connect to Network Element with Thread to Allow GUI to function properly
def ConnectNE(ne,username,password):
   global frame
   global connected
   config = SessionConfig(None)  
   config.set_tls_pinning('', PinningHandler(''))  
   config.transportMode = SessionConfig.SessionTransportMode.TLS
   ne.connect(username, password, config)
   connected = 1
 
#Wait for connection handleer
def loading():
   global frame
   global uptime
   global pixel
   global logo_stage
   global position

   position[0] = origin_pixel[0]
   position[1] = origin_pixel[1]

   #Wait for Connection Handler to Finish
   if (logo_stage == 0):
         for i in range(1,7,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]-pixel
         for i in range(1,9,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]+pixel
         for i in range(1,7,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         logo_stage = logo_stage+1
   elif (logo_stage == 1):
         position[0] = position[0]+6*pixel
         position[1] = position[1]-6*pixel
         for i in range(1,13,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]-pixel
         for i in range(1,15,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]+pixel
         for i in range(1,13,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         logo_stage = logo_stage+1
   elif (logo_stage == 2):
         position[0] = position[0]+6*pixel
         position[1] = position[1]-6*pixel        
         for i in range(1,19,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]-pixel
         for i in range(1,21,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]+pixel
         for i in range(1,19,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         logo_stage = logo_stage+1
   elif (logo_stage == 3):
         position[0] = position[0]+6*pixel
         position[1] = position[1]+6*pixel        
         for i in range(1,13,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]-pixel
         for i in range(1,15,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]+pixel
         for i in range(1,13,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         logo_stage = logo_stage+1
   elif (logo_stage == 4):
         position[0] = position[0]+6*pixel
         position[1] = position[1]+6*pixel        
         for i in range(1,7,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]-pixel
         for i in range(1,9,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]+pixel
         for i in range(1,7,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         logo_stage = logo_stage+1
   elif (logo_stage == 5):
         position[0] = position[0]+6*pixel
         position[1] = position[1]-6*pixel
         for i in range(1,13,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]-pixel
         for i in range(1,15,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]+pixel
         for i in range(1,13,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         logo_stage = logo_stage+1
   elif (logo_stage == 6):
         position[0] = position[0]+6*pixel
         position[1] = position[1]-6*pixel        
         for i in range(1,19,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]-pixel
         for i in range(1,21,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]+pixel
         for i in range(1,19,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         logo_stage = logo_stage+1
   elif (logo_stage == 7):
         position[0] = position[0]+6*pixel
         position[1] = position[1]+6*pixel        
         for i in range(1,13,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]-pixel
         for i in range(1,15,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]+pixel
         for i in range(1,13,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         logo_stage = logo_stage+1
   elif (logo_stage == 8):
         position[0] = position[0]+6*pixel
         position[1] = position[1]+6*pixel        
         for i in range(1,7,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]-pixel
         for i in range(1,9,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         position[0] = position[0]+pixel
         position[1] = position[1]+pixel
         for i in range(1,7,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
         logo_stage = logo_stage+1
   elif (logo_stage == 9):
      frame.delete(all)
      background()
      logo_stage=0
      origin_pixel[0] = width/6
      origin_pixel[1] = height/2
      if (connected == 1):
         logo_stage = 10



def tick():
   global frame
   global connected
   global ne

   if (logo_stage != 10):
      loading()
      frame.after(100,tick)
      return

   print "test"
   frame.after(100,tick)

   

def background():
   global frame
   
   frame.create_rectangle(0,0,width,height,fill="Black")
   frame.create_text(width/2,30,text="OnePK Python SDK",fill="White",font="Helvetica 36")


  
# Print some info around the NetworkElement
#print ne
#print "System Name:            ", ne.properties.sys_name
#print "System Uptime:          ", ne.properties.sys_uptime
#print "Total System Memory:    ", ne.total_system_memory
#print "Free System Memory:     ", ne.free_system_memory
#print "System CPU Utilization: ", ne.system_cpu_utilization, "%"
#print "System Connect Time:    ", ne.get_connect_time()
#print "System Disconnect Time:  ", ne.get_disconnect_time()

#Setup Tkinter
root = Tk()
root.title("Internet Status")

#Create frame widthxheight
frame = Canvas(root, width=width, height=height)
frame.pack()

#Load background
background()

#Connect to Network Element in Thread
Connect_Thread = Thread(target=ConnectNE, args=(ne,username,password))
Connect_Thread.start()

#Start loading screen / Start Connection Handler
tick()

#Initialize varibles
#uptime = frame.create_text(width/2,height/2,text=str(ne.properties.sys_uptime),fill="Black")

#set focus for keyboard input
frame.focus_set()

#Mainloop
mainloop()
  
# Disconnect the Network Element
ne.disconnect()  
