import maya.cmds as cmds


def componentToJoint():
    if cmds.objectType(cmds.ls(sl=1)[0]) != "mesh":
        return
    # return the selection as a list
    selList = getSelection()
    print selList
    componentType = selList[0][selList[0].index(".") + 1:selList[0].index("[")]
    componentCenters = []
    # if you selected a face or edge, make our joints at those component's centers
    if componentType == "f" or componentType == "e":
        for c in selList:
            p = cmds.xform(c, q=1, t=1, ws=1)
            # find the average of all our x,y,z points. That's our center
            componentCenters.append([sum(p[0::3]) / len(p[0::3]),
                                     sum(p[1::3]) / len(p[1::3]),
                                     sum(p[2::3]) / len(p[2::3])])
            for loc in componentCenters:
                cmds.select(cl=1)
                cmds.joint(n="joint#", p=loc, rad=.25)

    # else make a joint at the location of each vertex
    else:
        for c in selList:
            cmds.select(cl=1)
            # make a joint at the position of each selected vertex
            cmds.joint(n="joint#", p=cmds.pointPosition(c), rad=.25)
    cmds.select(cl=1)


def getSelection():
    components = cmds.ls(sl=1)
    selList = []
    objName = components[0][0:components[0].index(".")]
    # go through every component in the list. If it is a single component ("pCube1.vtx[1]"), add it to the list. Else,
    # add each component in the index ("pCube1.vtx[1:5]") to the list
    for c in components:
        if ":" not in c:
            selList.append(c)
        else:
            print c
            startComponent = int(c[c.index("[") + 1: c.index(":")])
            endComponent = int(c[c.index(":") + 1:c.index("]")])
            componentType = c[c.index(".") + 1:c.index("[")]
            while startComponent <= endComponent:
                selList.append(objName + "." + componentType + "[" + str(startComponent) + "]")
                startComponent += 1

    return selList

componentToJoint()

https://gist.github.com/benmorgantd/d2a578bd5280a6fab76568373d3930f7