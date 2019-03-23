from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys #these 4 import the needed systems and packages


name = 's_orbital' #defines a variable - name - as 's_orbital'

def main(): #starts the function - main
    glutInit(sys.argv) #initializes system
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) #initializes display modes
    glutInitWindowSize(400,400) #sets window size
    glutCreateWindow(name) #creates window under the variable - namer
    glClearColor(0.,0.,0.,1.) 
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.] #sets variable to vector light position
    lightZeroColor = [0.8,1.0,0.8,1.0] #sets variable to the color green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition) #inserts variables to set up lighting
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor) #inserts variables to set up lighting
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1) #shadow stuff
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05) #shadow stuff
    glEnable(GL_LIGHT0)#enables lighitng
    glutDisplayFunc(display) #enables the function - display
    glMatrixMode(GL_PROJECTION) #I have tried very hard but I am unable to understand anything related to "matrix"
    gluPerspective(40.,1.,1.,40.) #sets vector perspective
    glMatrixMode(GL_MODELVIEW) 
    gluLookAt(0,0,10,
              0,0,0, 
              0,1,0) #sets vector centerpoint of window
    glPushMatrix() 
    glutMainLoop() #make all settings in main function loop
    return #ends function

def display(): #starts the function - display
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clears window
    glPushMatrix() 
    color = [1.0,0.,0.,1.] #sets the variable of the RGB vector color of objebts to red - the the first 3 numbers are RGB on a vector scale of 0-1 and the last number determines power on a vector scale of 0-1
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color) #changes the color
    glRotate(90, 1, 0, 0) #rotates the x axis of 3d window on a vector scale - first number is the angle and the last 3 are the xyz axis. The angle is distributed to the 3 axises based upon where they fall on the vector scale of 0 - 1.
    glutSolidSphere(2,50, 50) #makes a sphere - first number is radius - the last two numbers don't really matter for this particular kind of sphere
    glPopMatrix()
    glutSwapBuffers()#swaps the buffers of the window in case it's double buffered 
    return #ends function

if __name__ == '__main__': main() #publishes lighting settings etc. into window
