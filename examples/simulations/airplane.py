# Draw the shadow and trailing lines of 2 planes. This is not really
# a simulation.. just a way to illustrate how to move objects around!
from vedo import *
import numpy as np

settings.useDepthPeeling = False

world = Box([0,0,0], 30, 15, 8).wireframe()

plane1 = Mesh(dataurl+"cessna.vtk").c("green").addTrail()
plane1.addShadow(plane='z', point=-4)
plane1.addShadow(plane=Plane(pos=(0, 7.5, 0), normal=(0, 1, 0)))

# Setup the scene
show(world, plane1, axes=1, viewup="z", interactive=0)

for t in np.arange(0, 3.2, 0.01):
    plane1.pos(9*t-15, 2-t, sin(3-t)).rotateX(0+t) # make up some movement
    plotter = show(world, plane1)
    if plotter.escaped: break  # if ESC button is hit during the loop

interactive().close()
