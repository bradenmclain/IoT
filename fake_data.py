import cherrypy
import numpy
from gpiozero import LED

red = LED(17)

class demoExample:
    @cherrypy.expose
    def index(self):
        return repr(numpy.random.random())
    @cherrypy.expose
    def led(self,state):
        if state=="1":
            print("do the things")
        elif state=="0":
            print("do not the things")
    index.exposed = True
cherrypy.config.update({'server.socket_port': 8099})
cherrypy.engine.restart()
cherrypy.quickstart(demoExample())