
# -*- coding: utf-8 -*-. 
'''
Created on 04/05/2015
@author: Carlos Plantijn 10-10572
@author: Luis Colorado   09-11086
'''

from flask import Flask

from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)

class clsUser():
    
    def insertar(self):
        print("Hola Mundo")
        pass
        
    def buscar(self):
        pass
        
    def modificar(self):
        pass
        
    def eliminar(self):
        pass

if __name__ == '__main__':
    aux = clsUser()
    aux.insertar()
    manager.run()       