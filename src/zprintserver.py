# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Alex Pavlunenko <alexp at xpresstek.net>"
__date__ ="$Apr 10, 2014 1:14:52 PM$"

from RAWService.RAWService import RAWService
import asyncore
#from db.DBManager import DBManager

#dbman = DBManager('localhost','ZPrint','zprint','zprint')
#dbman.connect()
properties = {'listen_address':'127.0.0.1',\
              'listen_port': 9100,\
              'receive_buffer_size': 65535,\
              'db_host': 'localhost',\
              'db_schema': 'ZPrint',
              'db_user': 'zprint',\
              'db_password': 'zprint'
}

rs = RAWService(properties)
asyncore.loop()
