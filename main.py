#---------------CallMe!----------------------------
#          A Skype like VoIP Client
#Author: Tim Windelschmidt, Gunnar Wachenfeld
#
#--------------------------------------------------

import logging

#--------------------------------------------------
#Global Variables
#--------------------------------------------------


#--------------------------------------------------
#Logger
#--------------------------------------------------

logger = logging.getLogger('CallMe')
hdlr = logging.FileHandler('/tmp/callMe.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.WARNING)

#--------------------------------------------------
#Programm Code
#--------------------------------------------------
