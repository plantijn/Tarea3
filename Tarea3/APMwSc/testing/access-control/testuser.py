'''
Created on 06/05/2015

@author: Carlos Plantijn 10-10572
@author: Luis Colorado   09-11086
'''

import sys
sys.path.append('../../business/access-control')
from user import *
import unittest

class ClsUserTester(unittest.TestCase):
    
   #def testSearchUser(self):
    
    #caso frontera
    def test1UserInsertTrue(self):
        user1 = clsUser()
        self.assertTrue(user1.insertUser(fullname = 'sah', username = 'ssgfwguewhdioweflwefweflwhlwehflehfah',password = 'al', email = '@ls', id_dpt = 1, id_role = 1))
    '''
    #caso frontera
    def test2UserInsertFalse(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sah', username = 'sgfwguewhdioweflwefweflwhlwehflehfah',password = 'al', email = '@ls', iddpt = 1, idrole = 1))
    
    #caso frontera externa
    def test3UserInsertNoUser(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sah', username = '',password = 'al', email = '@?lds', iddpt = 1, idrole = 1))
    
    #caso frontera interna 
    def test4UserInsert1char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'a',password = '12234', email = 'xxx@gmail.com', iddpt = 800, idrole = 45))
    
            
    #caso malicia
    def test99999UserNoParam(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = '', username = '',password = '', email = '', iddpt = None, idrole = None))
    
    '''