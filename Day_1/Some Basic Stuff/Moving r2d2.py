import pybullet as p
import time
import pybullet_data
import os
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
planeId = p.loadURDF("plane.urdf")
roboStartPos = [2,2,1]
roboStartOrientation = p.getQuaternionFromEuler([0,0,0])
#roboId = p.loadURDF("r2d2.urdf",roboStartPos, roboStartOrientation)
roboId = p.loadURDF(os.path.join(script_dir, "r2d2.urdf"),roboStartPos, roboStartOrientation)
robo2StartPos = [0,0,1]
robo2StartOrientation = p.getQuaternionFromEuler([0,0,0])
#robo2Id = p.loadURDF("r2d2.urdf",robo2StartPos, robo2StartOrientation)
robo2Id = p.loadURDF(os.path.join(script_dir, "r2d2.urdf"),robo2StartPos, robo2StartOrientation)
x=0.0
for i in range (10000):
    if x<6.92:
     x=x+0.01
    else:
     x=0
     p.removeBody(roboId) 
     p.removeBody(robo2Id) 
     roboId = p.loadURDF(os.path.join(script_dir, "r2d2.urdf"),roboStartPos, roboStartOrientation)
     robo2Id = p.loadURDF(os.path.join(script_dir, "r2d2.urdf"),robo2StartPos, robo2StartOrientation)
    p.setGravity(-x,-x,0) 
    p.stepSimulation()
    time.sleep(1./240.)
 
    

p.disconnect()
