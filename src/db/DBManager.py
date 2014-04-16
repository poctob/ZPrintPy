# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Alex Pavlunenko <alexp at xpresstek.net>"
__date__ ="$Apr 11, 2014 1:11:38 PM$"

import MySQLdb as mdb

## Database manager.  Provides functionality for the database interaction

class DBManager:
    SELECT_VERSION = "SELECT VERSION()"
    INSERT_RAW_JOB = "INSERT INTO Jobs (host, raw_data) VALUES (%s, %s)"
    
    ##Default constructor
    def __init__(self, properties):
        #connection attributes
        self.host = properties['db_host']
        self.schema = properties['db_schema']
        self.user = properties['db_user']
        self.password = properties['db_password']
        
        #connection object
        self.connection = None
        
    def connect(self):
        try:
            self.connection = mdb.connect \
            (self.host, self.user, self.password, self.schema)
            
            print "Connection established!"
            cur = self.connection.cursor()
            cur.execute(self.SELECT_VERSION)

            print "%r" % cur.fetchone()
        
        except mdb.Error, e:
            print "Exception: %d: %s" % (e.args[0], e.args[1])
            raise

                
    def disconnect(self):
        if self.connection:
            print "Closing connection"
            self.connection.close()
                
    def insert_raw_job(self, host, data):
        try:
            cur = self.connection.cursor()
            statement = self.INSERT_RAW_JOB % (host, data)
            print statement
            cur.execute(self.INSERT_RAW_JOB, (host, data, ))
            print "Number of rows updated:",  cur.rowcount
            self.connection.commit()
        except mdb.Error, e:
            print "Exception: %d: %s" % (e.args[0], e.args[1])
            raise
        
        