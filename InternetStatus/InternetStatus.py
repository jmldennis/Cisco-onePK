# John Mark Dennis - 2015
# Tested running Python 2.7.8
# Simple App used with Raspberry Pi to display basic router
# status information using Tkinter
# Be sure to grab to python SDK off Cisco Developer Network

from onep.element.NetworkElement import NetworkElement  
from onep.element.SessionConfig import SessionConfig  
from onep.core.util import tlspinning
from onep.interfaces.InterfaceStatistics import InterfaceStatistics
from Tkinter import *
from threading import *

router_ip = "192.168.1.110"
connection_name = "Internet Status"
username = "cisco"
password = "cisco"
width = 1024
height = 768
connected = 0
pixel = width/100
origin_pixel = [width/6,height/2]
position = origin_pixel
logo_stage = 0
connect_attempt = 0
temp = 0
  
# TLS Connection
class PinningHandler(tlspinning.TLSUnverifiedElementHandler):  
   def __init__(self, pinning_file):  
       self.pinning_file = pinning_file  
   def handle_verify(self, host, hashtype, finger_print, changed):  
       return tlspinning.DecisionType.ACCEPT_ONCE  

#Connect to Network Element with Thread to Allow GUI to function properly
def ConnectNE():
   global frame
   global connect_attempt
   global ne
   global username
   global password

   ne = NetworkElement(router_ip,connection_name)
   config = SessionConfig(None)  
   config.set_tls_pinning('', PinningHandler(''))  
   config.transportMode = SessionConfig.SessionTransportMode.TLS
   if (ne.is_connected()!=1):
      try:
           ne.connect(username, password, config)
      except:
           connect_attempt = connect_attempt + 1
           ConnectNE()

#Currently Unused
def connected_bg():
   global frame

   #Start Displaying Live Data
   tick()

   
 
#Wait for connection handleer
def loading():
   global frame
   global pixel
   global logo_stage
   global position
   global ne
   global connect_attempt

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
      frame.delete("all")
      background()
      frame.create_text(width/2,height-100,text="Connection Attempt # "+str(connect_attempt),fill="White",font="Helvetica 24")
      logo_stage=0
      origin_pixel[0] = width/6
      origin_pixel[1] = height/2
      if (ne.is_connected() == 1):
         logo_stage = 10



def tick():
   global frame
   global ne
   global position
   global temp

   if (logo_stage != 10):
      loading()
      frame.after(100,tick)
      return

   frame.delete("all")
   
   background()

   #Draw Cisco Logo
   position[0] = width/6
   position[1] = height/4+pixel*3
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



   #Calculate System Uptime
   #Convert Seconds to Weeks, Days, Hours, Minutes, Seconds
   uptime_sec = ne.properties.sys_uptime

   #Extract Values
   seconds = uptime_sec % 60
   uptime_sec = uptime_sec - seconds
   years = uptime_sec/(60*60*24*7*52)
   uptime_sec = uptime_sec - years*(60*60*24*7*52)
   weeks = uptime_sec/(60*60*24*7)
   uptime_sec = uptime_sec - weeks*(60*60*24*7)
   days = uptime_sec/(60*60*24)
   uptime_sec = uptime_sec-days*(60*60*24)
   hours = uptime_sec/(60*60)
   uptime_sec = uptime_sec-hours*(60*60)
   minutes = uptime_sec/60

   #Calculate percentage to print in blocks of 10%
   years_percent = years+1
   weeks_percent = weeks*100/52
   if (weeks_percent > 0 and weeks_percent < 10):
      weeks_percent =  2
   elif (weeks_percent > 97 and weeks_percent < 100):
      weeks_percent = 11
   else:
      weeks_percent = weeks_percent/10 + 1
   days_percent = days*10/7+1
   hours_percent = hours*100/24
   if (hours_percent > 0 and hours_percent < 10):
      hours_percent = 2
   elif (hours_percent > 97 and hours_percent < 100):
      hours_percent = 11
   else:
      hours_percent = hours_percent/10 + 1     
   minutes_percent = minutes*100/60
   if (minutes_percent > 0 and minutes_percent < 10):
      minutes_percent = 2
   elif (minutes_percent > 97 and minutes_percent < 100):
      minutes_percent = 11
   else:
     minutes_percent = minutes_percent/10 + 1      
   seconds_percent = seconds*100/60
   if (seconds_percent > 0 and seconds_percent < 10):
      seconds_percent = 2
   elif (seconds_percent > 97 and seconds_percent < 100):
      seconds_percent = 11
   else:
      seconds_percent = seconds_percent/10 + 1


   #Print Values in blocks of 10
   position[0] = width-pixel*14
   position[1] = height-65

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Seconds",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,seconds_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = width-pixel*14
   position[1] = height-100

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Minutes",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,minutes_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = width-pixel*14
   position[1] = height-135

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Hours",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,hours_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = width-pixel*14
   position[1] = height-170

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Days",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,days_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = width-pixel*14
   position[1] = height-205

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Weeks",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,weeks_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = width-pixel*14
   position[1] = height-240

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Years",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,years_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = width-pixel*5
   position[1] = height-275

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Router Uptime",fill="White")





   #Get System Memory in bytes
   memory_free = ne.get_free_system_memory()
   memory_total = ne.get_total_system_memory()
   memory_used = memory_total - memory_free

   memory_free_k = memory_free/1024
   memory_free_m = memory_free_k/1024

   memory_total_k = memory_total/1024
   memory_total_m = memory_total_k/1024

   memory_used_k = memory_used/1024
   memory_used_m = memory_used_k/1024

   memory_tens = memory_used*10 / memory_total + 1

   position[0] = 100
   position[1] = height-65

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Memory",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,memory_tens,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel



   #Get CPU data
   cpu_percent = ne.get_system_cpu_utilization()

   cpu_tens = cpu_percent/10 + 1
   position[0] = 100
   position[1] = height-100

   frame.create_text(position[0]-40,position[1]+pixel/2,text="CPU",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,cpu_tens,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel







#   transmit_rate = ne.properties.sys_uptime
#   receive_rate = ne.interfaces.



   frame.after(100,tick)
   

   

def background():
   global frame
   
   frame.create_rectangle(0,0,width,height,fill="Black")
   frame.create_text(width/2,30,text="OnePK Python SDK",fill="White",font="Helvetica 36")


  

#Setup Tkinter
root = Tk()
root.title("Internet Status")

#Create frame widthxheight
frame = Canvas(root, width=width, height=height)
frame.pack()

#Load background
background()

#Load initial connection connection attempt
connect_attempt = 1
frame.create_text(width/2,height-100,text="Connection Attempt # "+str(connect_attempt),fill="White",font="Helvetica 24")

#Connect to Network Element in Thread
Connect_Thread = Thread(target=ConnectNE)
Connect_Thread.start()

#Start loading screen / Start Connection Handler
tick()


#set focus for keyboard input
frame.focus_set()

#Mainloop
mainloop()
  
# Disconnect the Network Element
ne.disconnect()  
