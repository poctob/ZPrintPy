# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Alex Pavlunenko <alexp at xpresstek.net>"
__date__ ="$Apr 14, 2014 8:41:42 AM$"

import asyncore
import socket
from db.DBManager import DBManager
import MySQLdb as mdb
import thread
import time

class RAWService(asyncore.dispatcher):
    
    def __init__(self, properties):
        asyncore.dispatcher.__init__(self)
        self.properties = properties
        self.host = properties['listen_address']
        self.port = properties['listen_port']
        self.buffer_size = properties['receive_buffer_size']
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((self.host, self.port))
        self.running = True
        self.listen(5)
        
    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = RAWDataHandler(sock, self.buffer_size)

    def start(self):
        try:
            thread.start_new_thread(self.listen, ())
            
        except:
            print "Error! Unable to start server thread!"
            

    def stop(self):
        self._set_running(False)

    def _set_running(self, p_running):
        self.running = p_running

    def _get__running(self):
        return self.running
    
    def save_to_db(self, data, address):
        try:
            dbman = DBManager(self.properties)
            dbman.connect()
                       
            dbman.insert_raw_job(address, data)
        
            dbman.disconnect()
            
        except mdb.Error, e:
            print "Exception: %d: %s" % (e.args[0], e.args[1])
        
        
class RAWDataHandler(asyncore.dispatcher_with_send):
    
        def __init__(self, sock, bsize):
            asyncore.dispatcher_with_send.__init__(self, sock)
            self.buffer_size = bsize
    
        def handle_read(self):
            data = self.recv(self.buffer_size)
            if(data):
                 print 'Data: ', data
    

