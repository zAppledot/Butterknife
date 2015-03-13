import c4d
from c4d import gui

doc = c4d.documents.GetActiveDocument()
selected = doc.GetActiveObjects(0)

def main():
    if len(selected) > 0: # we have one or more selected objects in the scene
        for ob in selected:
            if ob.GetTypeName() == "Polygon":
                print (ob.GetName() + ' - ' + ob.GetTypeName()),
                bb = ob.GetRad()
                print c4d.Vector(bb)
                c4d.CallCommand(12187) # Polygons
                c4d.CallCommand(1016030) # Knife
        
            else:
                print "Drat"

def getBoundingBox(ob):
    print ob.GetRad()
    

if __name__=='__main__':
    main()
