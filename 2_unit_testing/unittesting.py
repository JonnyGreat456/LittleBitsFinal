#http://flask.pocoo.org/docs/0.12/testing/ 
#The code in the setUp() method creates a new test client and initializes a new database. This function is called before each individual test function is run
#This file was called and run for each function the mainlogdemo2.py
#The 'DATABaSE' corresponds to our multiple databses we used like "employeeshiftsdb.db", "orderstatus.db"
import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()