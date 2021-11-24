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
            red.on()
        elif state=="0":
            red.off()
    index.exposed = True
cherrypy.config.update({'server.socket_port': 8099,
                        'server.socket_host': '0.0.0.0'})
cherrypy.engine.restart()
cherrypy.quickstart(demoExample())