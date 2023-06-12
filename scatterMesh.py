import maya.cmds as cmds
import random

def createPolyCube(amount, rangeSpread, typeObj="none"):
    createdMesh = []

    randomObj = typeObj =="random"

    for i in range(amount):
        if randomObj:
            typeObj = random.choice(["cube", "sphere", "torus", "cone", "cylinder"])
        if typeObj == "cube":
            transform_node = cmds.polyCube()[0]
        elif typeObj == "sphere":
            transform_node = cmds.polySphere()[0]
        elif typeObj == "torus":
            transform_node = cmds.polyTorus()[0]
        elif typeObj == "cone":
            transform_node = cmds.polyCone()[0]
        elif typeObj == "cylinder":
            transform_node = cmds.polyCylinder()[0]
        else:
            print("Please give some of Object")
            return None

        setPosition(transform_node, rangeSpread)
        createdMesh.append(transform_node)

    cmds.group(createdMesh, name="CubeGroup")
    cmds.select(clear=True)

def setPosition(transform_node, spread):
    tx = random.randint(-spread, spread)
    ty = random.randint(0, spread)
    tz = random.randint(-spread, spread)

    rx = random.randrange(360)
    ry = random.randrange(360)
    rz = random.randrange(360)

    # sx = random.random()
    # sy = random.random()
    # sz = random.random()

    cmds.setAttr(f"{transform_node}.translate", tx, ty, tz, type="double3")
    cmds.setAttr(f"{transform_node}.rotate", rx, ry, rz, type="double3")
    # cmds.setAttr(f"{transform_node}.scale", sx, sy, sz, type="double3")

cmds.file(f=True, new=True)

# createPolyCube -> amount of object, spread area, type of objects
# type of objects = ["cube", "sphere", "torus", "cone", "cylinder"] or random
action = createPolyCube(100, 20, "random")




print(f"{action} has been created")