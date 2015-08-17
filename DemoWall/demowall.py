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

#router_ip = "192.168.1.110"
router_ip = "10.3.14.38"
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
internet_interface = "GigabitEthernet1"
uplink_bps = 1*1024*1024*1024
downlink_bps = 1*1024*1024*1024
  
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
   global logo_stage

   if (logo_stage != 10):
      loading()
      frame.after(100,tick)
      return

   #Working on Reconnect
   if (ne.is_connected()!=1):
      connect_attempt = 1
      logo_stage = 0
      Connect_Thread = Thread(target=ConnectNE)
      Connect_Thread.start()
      tick()
      return

   #Get Data/Re-Connect if Disconnected
   if (ne.is_connected()==1):
      try:
         #Get Uptime
         uptime_sec = ne.properties.sys_uptime
         #Get CPU percent used
         cpu_percent = ne.get_system_cpu_utilization()
         #Get Memory free and total
         memory_free = ne.get_free_system_memory()
         memory_total = ne.get_total_system_memory()
         #Get INET Interface Data
         INET_interface = ne.get_interface_by_name(internet_interface)
         INET_interface_Statistics =  INET_interface.get_statistics()
      except:
         print "Failed to get data from Network Element"
         connect_attempt = 1
         logo_stage = 0
         Connect_Thread = Thread(target=ConnectNE)
         Connect_Thread.start()
         tick()
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

   #Print Values in blocks of 10
   position[0] = pixel*10
   position[1] = height-pixel*4

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Seconds",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*60+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,seconds+1,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*10
   position[1] = height-pixel*7

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Minutes",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*60+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,minutes+1,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*10
   position[1] = height-pixel*10

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Hours",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*24+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,hours+1,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*10
   position[1] = height-pixel*13

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Days",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*7+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,days+1,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*10
   position[1] = height-pixel*16

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Weeks",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*52+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,weeks+1,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*19
   position[1] = height-pixel*19

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Router Uptime",fill="White")




   #Get Interface Statistics

   #print INET_interface_Statistics
   rx_ucast =  INET_interface_Statistics.receive_unicast
   rx_mcast =  INET_interface_Statistics.receive_multicast
   rx_bcast =  INET_interface_Statistics.receive_broadcast
   rx_total =  INET_interface_Statistics.receive_cum_packet
   rx_bytes = INET_interface_Statistics.receive_rate_cum_byte
   rx_bytes_per_second = INET_interface_Statistics.receive_rate_bps
   rx_load = INET_interface_Statistics.receive_load

   tx_ucast =  INET_interface_Statistics.transmit_unicast
   tx_mcast =  INET_interface_Statistics.transmit_multicast
   tx_bcast =  INET_interface_Statistics.transmit_broadcast
   tx_total =  INET_interface_Statistics.transmit_cum_packet
   tx_bytes = INET_interface_Statistics.transmit_rate_cum_byte
   tx_bytes_per_second = INET_interface_Statistics.transmit_rate_bps
   tx_load = INET_interface_Statistics.transmit_load

   rx_tx_bytes = rx_bytes + tx_bytes


   #Calculated the Rx percentages
   rx_ucast_percent = rx_ucast*100/rx_total
   if (rx_ucast_percent > 0 and rx_ucast_percent < 10):
      rx_ucast_percent = 2
   elif (rx_ucast_percent > 97 and rx_ucast_percent < 100):
      rx_ucast_percent = 11
   else:
     rx_ucast_percent = rx_ucast_percent/10 + 1

   rx_mcast_percent = rx_mcast*100/rx_total
   if (rx_mcast_percent > 0 and rx_mcast_percent < 10):
      rx_mcast_percent = 2
   elif (rx_mcast_percent > 97 and rx_mcast_percent < 100):
      rx_mcast_percent = 11
   else:
     rx_mcast_percent = rx_mcast_percent/10 + 1  

   rx_bcast_percent = rx_bcast*100/rx_total
   if (rx_bcast_percent > 0 and rx_bcast_percent < 10):
      rx_bcast_percent = 2
   elif (rx_bcast_percent > 97 and rx_bcast_percent < 100):
      rx_bcast_percent = 11
   else:
     rx_bcast_percent = rx_bcast_percent/10 + 1

   rx_bytes_percent = rx_bytes*100/rx_tx_bytes
   if (rx_bytes_percent > 0 and rx_bytes_percent < 10):
      rx_bytes_percent = 2
   elif (rx_bytes_percent > 97 and rx_bytes_percent < 100):
      rx_bytes_percent = 11
   else:
     rx_bytes_percent = rx_bytes_percent/10 + 1

   rx_load_percent = rx_load*100/255
   if (rx_load_percent > 0 and rx_load_percent < 10):
      rx_load_percent = 2
   elif (rx_load_percent > 97 and rx_load_percent < 100):
      rx_load_percent = 11
   else:
     rx_load_percent = rx_load_percent/10 + 1

   #Calculated the Tx percentages
   tx_ucast_percent = tx_ucast*100/tx_total
   if (tx_ucast_percent > 0 and tx_ucast_percent < 10):
      tx_ucast_percent = 2
   elif (tx_ucast_percent > 97 and tx_ucast_percent < 100):
      tx_ucast_percent = 11
   else:
     tx_ucast_percent = tx_ucast_percent/10 + 1

   tx_mcast_percent = tx_mcast*100/tx_total
   if (tx_mcast_percent > 0 and tx_mcast_percent < 10):
      tx_mcast_percent = 2
   elif (tx_mcast_percent > 97 and tx_mcast_percent < 100):
      tx_mcast_percent = 11
   else:
     tx_mcast_percent = tx_mcast_percent/10 + 1  

   tx_bcast_percent = tx_bcast*100/tx_total
   if (tx_bcast_percent > 0 and tx_bcast_percent < 10):
      tx_bcast_percent = 2
   elif (tx_bcast_percent > 97 and tx_bcast_percent < 100):
      tx_bcast_percent = 11
   else:
     tx_bcast_percent = tx_bcast_percent/10 + 1

   tx_bytes_percent = tx_bytes*100/rx_tx_bytes
   if (tx_bytes_percent > 0 and tx_bytes_percent < 10):
      tx_bytes_percent = 2
   elif (tx_bytes_percent > 97 and tx_bytes_percent < 100):
      tx_bytes_percent = 11
   else:
     tx_bytes_percent = tx_bytes_percent/10 + 1

   tx_load_percent = tx_load*100/255
   if (tx_load_percent > 0 and tx_load_percent < 10):
      tx_load_percent = 2
   elif (tx_load_percent > 97 and tx_load_percent < 100):
      tx_load_percent = 11
   else:
     tx_load_percent = tx_load_percent/10 + 1


   
   #Print Rx Values in blocks of 10
   position[0] = pixel*63
   position[1] = height-pixel*27

   frame.create_text(position[0]-50,position[1]+pixel/2,text="Rx BCast",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,rx_bcast_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*63
   position[1] = height-pixel*30

   frame.create_text(position[0]-50,position[1]+pixel/2,text="Rx MCast",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,rx_mcast_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*63
   position[1] = height-pixel*33


   frame.create_text(position[0]-50,position[1]+pixel/2,text="Rx UCast",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,rx_ucast_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*63
   position[1] = height-pixel*36


   frame.create_text(position[0]-50,position[1]+pixel/2,text="Rx Percent",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,rx_bytes_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*63
   position[1] = height-pixel*39


   frame.create_text(position[0]-50,position[1]+pixel/2,text="Rx Load",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,rx_load_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*72
   position[1] = height-pixel*42


   frame.create_text(position[0]-40,position[1]+pixel/2,text="Rx Internet",fill="White")

   #Print Tx Values in blocks of 10
   position[0] = pixel*35
   position[1] = height-pixel*27

   frame.create_text(position[0]-50,position[1]+pixel/2,text="Tx BCast",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,tx_bcast_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*35
   position[1] = height-pixel*30

   frame.create_text(position[0]-50,position[1]+pixel/2,text="Tx MCast",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,tx_mcast_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*35
   position[1] = height-pixel*33

   frame.create_text(position[0]-50,position[1]+pixel/2,text="Tx UCast",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,tx_ucast_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*35
   position[1] = height-pixel*36

   frame.create_text(position[0]-50,position[1]+pixel/2,text="Tx Percent",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,tx_bytes_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*35
   position[1] = height-pixel*39

   frame.create_text(position[0]-50,position[1]+pixel/2,text="Tx Load",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,tx_load_percent,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel

   position[0] = pixel*45
   position[1] = height-pixel*42

   frame.create_text(position[0]-50,position[1]+pixel/2,text="Tx Internet",fill="White")



   #Get System Memory in bytes

   memory_used = memory_total - memory_free

   memory_free_k = memory_free/1024
   memory_free_m = memory_free_k/1024

   memory_total_k = memory_total/1024
   memory_total_m = memory_total_k/1024

   memory_used_k = memory_used/1024
   memory_used_m = memory_used_k/1024

   memory_tens = memory_used*10 / memory_total + 1

   position[0] = pixel*86
   position[1] = height-pixel*7

   frame.create_text(position[0]-40,position[1]+pixel/2,text="Memory",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,memory_tens,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel



   #Get CPU data
   

   cpu_tens = cpu_percent/10 + 1
   position[0] = pixel*86
   position[1] = height-pixel*10

   frame.create_text(position[0]-40,position[1]+pixel/2,text="CPU",fill="White")
   frame.create_rectangle(position[0]-2,position[1]-2,position[0]+pixel*10+2,position[1]+pixel+2,fill="Black",outline="White")
   for i in range(1,cpu_tens,1):
            frame.create_rectangle(position[0],position[1]+pixel*(i-1),position[0]+pixel,position[1]+pixel*i,fill="White")
            position[0] = position[0]+pixel
            position[1] = position[1]-pixel


   position[0] = pixel*96
   position[1] = height-pixel*13

   frame.create_text(position[0]-50,position[1]+pixel/2,text="System Health",fill="White")


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
