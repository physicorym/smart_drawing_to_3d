
import FreeCAD as App
import Part
import Mesh

from utils.builder_detail import PartBuilder

doc = App.newDocument("MyModel")

builder = PartBuilder()


# Пример использования класса с добавлением координат для выдавливания
builder = PartBuilder()

# Создаем параллелепипед
builder.create_box(10.0, 5.0, 3.0)

# Вытягиваем цилиндр с указанием позиции
builder.extrude_cylinder(1.0, 5.0, position=App.Vector(5.0, 2.5, 3.0))

# Создаем отверстие
builder.subtract_cylinder(0.5, 1.0, App.Vector(5.0, 2.5, 1.0))

# Создаем паз в виде параллелепипеда с указанием позиции
builder.create_groove_as_box(2.0, 1.0, 3.0, App.Vector(2.0, 1.0, 0.0))

stl_file_path = "/app/my_model.stl"
App.ActiveDocument=App.getDocument("MyModel")
Mesh.export([builder],stl_file_path)

App.closeDocument("MyModel")


