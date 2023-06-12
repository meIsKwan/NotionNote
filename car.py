import maya.cmds as cmds


def createCAR(name, width=1, depth=3):
    body = createBODY(width, depth)
    tires = createTIRES(width, depth)
    assemblingCAR(body, tires)
    return name

def createBODY(body_width, body_depth):
    body = cmds.polyCube(w=body_width, depth=body_depth, height=0.3, name="Body car") [0]
    return body

def createTIRES(body_width, body_depth):
    tireSize = body_width * 0.25
    tireTX = body_width * 0.5 + tireSize * 0.5
    tireTZ = body_depth * .5
    front_tire_left = createSingleTIRE("front_tire_left", tireSize, tireTX, 0, tireTZ)
    front_tire_right = createSingleTIRE("front_tire_right", tireSize, -tireTX, 0, tireTZ)
    back_tire_left = createSingleTIRE("back_tire_left", tireSize, tireTX, 0, -tireTZ)
    back_tire_right = createSingleTIRE("back_tire_right", tireSize, -tireTX, 0, -tireTZ)

    return [front_tire_left, front_tire_right, back_tire_left, back_tire_right]

def createSingleTIRE(tireName, size, tx, ty=0, tz=0):
    myTire = cmds.polyCylinder(name=tireName, ax=(1,0,0), h=size, sc=2)[0]
    cmds.setAttr(f"{myTire}.translate", tx, ty, tz)

    return myTire

def assemblingCAR(body, tires):
    bodyGRP = cmds.group(body, name="Body Group")
    tiresGRP = cmds.group(tires, name="Tires Group")
    carGRP = cmds.group(bodyGRP, tiresGRP, name="Car Group")

action = createCAR("MyNewCar", 4, 10)

print(f"{action} is the name of my New Car")