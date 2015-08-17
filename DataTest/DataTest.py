# John Mark Dennis - 2015
# Tested running Python 2.7.8
# Basic Connectivity App Testing onePK connectivity to CSR1000V using tls_pinning
# Grabbed this example program from jerrwong
# https://communities.cisco.com/thread/44820

from onep.element.NetworkElement import NetworkElement  
from onep.element.SessionConfig import SessionConfig
from onep.interfaces import InterfaceStatistics
from onep.interfaces import NetworkInterface
from onep.core.util import tlspinning  
  
# TLS Connection
class PinningHandler(tlspinning.TLSUnverifiedElementHandler):  
   def __init__(self, pinning_file):  
       self.pinning_file = pinning_file  
   def handle_verify(self, host, hashtype, finger_print, changed):  
       return tlspinning.DecisionType.ACCEPT_ONCE  
  
# Connection to onePK enabled Network Element  
config = SessionConfig(None)  
config.set_tls_pinning('', PinningHandler(''))  
config.transportMode = SessionConfig.SessionTransportMode.TLS  
ne = NetworkElement('192.168.1.110', 'HelloWorld')  
ne.connect('cisco', 'cisco', config)  
  
# Print some info around the NetworkElement
print ne
print "System Name:            ", ne.properties.sys_name
print "System Uptime:          ", ne.properties.sys_uptime
print "Total System Memory:    ", ne.total_system_memory
print "Free System Memory:     ", ne.free_system_memory
print "System CPU Utilization: ", ne.system_cpu_utilization, "%"
print "System Connect Time:    ", ne.get_connect_time()
print "System Disconnect Time:  ", ne.get_disconnect_time()


GigabitEthernet1 = ne.get_interface_by_name('GigabitEthernet1')
GigabitEthernet1_Statistics =  GigabitEthernet1.get_statistics()
print ne.properties.product_id
print ne.properties.udi
print ne.properties.SerialNo
print ne.host_address
print ne.get_interface_list





  
# Disconnect the Network Element
ne.disconnect()  
