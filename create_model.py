
import FreeCAD as App
import Part
import Mesh

doc = App.newDocument("MyModel")

length = 10.0
width = 5.0
height = 3.0
box = Part.makeBox(length, width, height)

box_obj = doc.addObject("Part::Feature", "Box")
box_obj.Shape = box

stl_file_path = "/app/my_model.stl"
App.ActiveDocument=App.getDocument("MyModel")
Mesh.export([box_obj],stl_file_path)

App.closeDocument("MyModel")