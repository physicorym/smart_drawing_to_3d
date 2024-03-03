import FreeCAD as App
import Part

import FreeCAD as App
import Part

class PartBuilder:
    def __init__(self):
        self.doc = App.newDocument("MyDocument")
        self.base_object = None

    def create_box(self, length, width, height):
        self.base_object = Part.makeBox(length, width, height)
        self.add_to_document(self.base_object, "Box")

    def extrude_cylinder(self, radius, height, position=App.Vector(0, 0, 0)):
        if self.base_object:
            cylinder = Part.makeCylinder(radius, height)
            cylinder.translate(position)
            extrusion = self.base_object.extrude(cylinder)
            self.add_to_document(extrusion, "ExtrudedCylinder")
        else:
            print("Error: No base object created yet.")

    def subtract_cylinder(self, radius, height, position):
        if self.base_object:
            cylinder = Part.makeCylinder(radius, height)
            cylinder.translate(position)
            result = self.base_object.cut(cylinder)
            self.add_to_document(result, "Result")
        else:
            print("Error: No base object created yet.")

    def create_groove_as_box(self, groove_length, groove_width, groove_height, groove_position):
        if self.base_object:
            groove_box = Part.makeBox(groove_length, groove_width, groove_height)
            groove_box.translate(groove_position)
            result = self.base_object.cut(groove_box)
            self.add_to_document(result, "GrooveBox")
        else:
            print("Error: No base object created yet.")

    def add_to_document(self, shape, name):
        self.doc.addObject("Part::Feature", name).Shape = shape
        App.ActiveDocument.recompute()

    def export_stl(self, file_path):
        if self.base_object:
            mesh = self.base_object.toMesh()
            mesh.exportStl(file_path)
        else:
            print("Error: No base object created yet.")



# class PartBuilder:
#     def __init__(self):
#         self.doc = App.newDocument("MyDocument")
#         self.base_object = None

#     def create_box(self, length, width, height):
#         self.base_object = Part.makeBox(length, width, height)
#         self.add_to_document(self.base_object, "Box")

#     def extrude_cylinder(self, radius, height):
#         if self.base_object:
#             cylinder = Part.makeCylinder(radius, height)
#             extrusion = self.base_object.extrude(cylinder)
#             self.add_to_document(extrusion, "ExtrudedCylinder")
#         else:
#             print("Error: No base object created yet.")

#     def subtract_cylinder(self, radius, height, position):
#         if self.base_object:
#             cylinder = Part.makeCylinder(radius, height)
#             cylinder.translate(position)
#             result = self.base_object.cut(cylinder)
#             self.add_to_document(result, "Result")
#         else:
#             print("Error: No base object created yet.")

#     def create_groove_as_box(self, groove_length, groove_width, groove_height, groove_position):
#         if self.base_object:
#             groove_box = Part.makeBox(groove_length, groove_width, groove_height)
#             groove_box.translate(groove_position)
#             result = self.base_object.cut(groove_box)
#             self.add_to_document(result, "GrooveBox")
#         else:
#             print("Error: No base object created yet.")

#     def add_to_document(self, shape, name):
#         self.doc.addObject("Part::Feature", name).Shape = shape
#         App.ActiveDocument.recompute()

#     def export_stl(self, file_path):
#         if self.base_object:
#             mesh = self.base_object.toMesh()
#             mesh.exportStl(file_path)
#         else:
#             print("Error: No base object created yet.")

# # Пример использования класса и сохранения в STL
# builder = PartBuilder()

# # Создаем параллелепипед
# builder.create_box(10.0, 5.0, 3.0)

# # Вытягиваем цилиндр
# builder.extrude_cylinder(1.0, 2.0)

# # Создаем отверстие
# builder.subtract_cylinder(0.5, 1.0, App.Vector(5.0, 2.5, 1.0))

# # Сохраняем в STL
# builder.export_stl("/путь/к/вашему/файлу.stl")
