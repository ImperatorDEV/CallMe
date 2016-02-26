#---------------Fritz!Status----------------------------
#
#Author: Tim Windelschmidt
#
#--------------------------------------------------

import fritzconnection, logging, ConfigParser, os, Tkinter

#--------------------------------------------------
#ConfigParser
#--------------------------------------------------

config = ConfigParser.ConfigParser()

if os.path.isfile('FritzStatus.cfg'):

    config = ConfigParser.ConfigParser()
    config.read('FritzStatus.cfg')

else:
    config.add_section('FritzStatus')
    config.set('FritzStatus', 'IP_FROM_FRITZ', '192.168.178.1')
    config.set('FritzStatus', 'PORT_FROM_FRITZ', '49000')
    config.set('FritzStatus', 'USERNAME', 'admin')
    config.set('FritzStatus', 'PASSWORD', 'password')

    with open('FritzStatus.cfg', 'wb') as configfile:
        config.write(configfile)

#--------------------------------------------------
#Global Variables
#--------------------------------------------------

IP_FROM_FRITZ = config.get('FritzStatus', 'IP_FROM_FRITZ')
PORT_FROM_FRITZ = config.get('FritzStatus', 'PORT_FROM_FRITZ')
USERNAME = config.get('FritzStatus', 'USERNAME')
PASSWORD = config.get('FritzStatus', 'PASSWORD')

#--------------------------------------------------
#Logger
#--------------------------------------------------

logger = logging.getLogger('FritzStatus')
hdlr = logging.FileHandler('/tmp/Fritzstatus.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.WARNING)

#--------------------------------------------------
#Programm Code
#--------------------------------------------------

class FritzStatus(object):
 fc = fritzconnection.FritzConnection()

 @property
 def modelname(self):
     return self.fc.modelname

 @property
 def is_linked(self):
     status = self.fc.call_action('GetCommonLinkProperties')
     return status['NewPhysicalLinkStatus'] == 'Up'

 @property
 def is_connected(self):
     status = self.fc.call_action('GetStatusInfo')
     return status['NewConnectionStatus'] == 'Connected'

def update_label():
    fs = fritzconnection.FritzStatus()
    modelname.config(text="Modell: %s" % fs.modelname)
    bytes_sent.config(text="Bytes send: %s" % fs.bytes_sent)
    bytes_received.config(text="Bytes recived: %s" % fs.bytes_received)
    is_linked.config(text="Linked: %s" % fs.is_linked)
    is_connected.config(text="Connected: %s" % fs.is_connected)
    external_ip.config(text="External IP: %s" % fs.external_ip)
    str_uptime.config(text="Uptime: %s" % fs.str_uptime)
    uptime.config(text="Uptime(seconds): '{0}'".format(fs.uptime))
    max_bit_rate.config(text="Max. Bitrate: '{0}'".format(fs.max_bit_rate))
    max_byte_rate.config(text="Max. Byterate: '{0}'".format(fs.max_byte_rate))
    str_max_bit_rate.config(text="Max. Speed: '{0}'".format(fs.str_max_bit_rate))

    app_win.after(UPDATE_TIME, update_label)

UPDATE_TIME = 100 # 0,1 Sek.
app_win = Tkinter.Tk()
app_win.wm_title("FritzBox Status: '{0}'".format((IP_FROM_FRITZ)))

modelname = Tkinter.Label(app_win, relief='raised', width=40)
bytes_sent = Tkinter.Label(app_win, relief='raised', width=40)
bytes_received = Tkinter.Label(app_win, relief='raised', width=40)
is_linked = Tkinter.Label(app_win, relief='raised', width=40)
is_connected = Tkinter.Label(app_win, relief='raised', width=40)
external_ip = Tkinter.Label(app_win, relief='raised', width=40)
uptime = Tkinter.Label(app_win, relief='raised', width=40)
str_uptime = Tkinter.Label(app_win, relief='raised', width=40)
max_bit_rate = Tkinter.Label(app_win, relief='raised', width=40)
max_byte_rate = Tkinter.Label(app_win, relief='raised', width=40)
str_max_bit_rate = Tkinter.Label(app_win, relief='raised', width=40)

modelname.pack()
bytes_sent.pack()
bytes_received.pack()
is_linked.pack()
is_connected.pack()
external_ip.pack()
uptime.pack()
str_uptime.pack()
max_bit_rate.pack()
max_byte_rate.pack()
str_max_bit_rate.pack()

update_label()
app_win.mainloop()