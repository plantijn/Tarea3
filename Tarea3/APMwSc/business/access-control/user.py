
# -*- coding: utf-8 -*-. 
'''
Created on 04/05/2015

@author: Carlos Plantijn 10-10572
@author: Luis Colorado   09-11086
'''

import sys
sys.path.append('../../data')
from model import *

'''
from flask import Flask

from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)
'''

class clsUser():
    
    def insertUser(self, fullname, username, password, email, id_dpt, id_role):
        auser = clsUser.query.filter_by(username=username).all()
        if auser == []:
            new_user = clsUser(fullname = fullname, username = username, password = password, email =email, id_dpt = id_dpt, id_role = id_role)
            if (new_user.username == '' or new_user.fullname == '' or new_user.password == '' or new_user.email == '' or new_user.iddpt == None or new_user.idrole == None):
                return False
            else:                
                db.session.add(new_user)
                db.session.commit()
                return True
        else:
            return False
        
    def findUser(self):
        pass
        
    def modifyUser(self):
        pass
        
    def deleteUser(self, username):
        auser = searchUser(username)
        if auser is None:
            return False
        else:
            db.session.delete(auser)
            return True

'''
if __name__ == '__main__':
    aux = clsUser()
    aux.insertar()
    manager.run()
'''       