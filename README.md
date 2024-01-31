# FreeCAD Docker Container

## Сборка образа

```bash
docker build -t freecad_container .
```


## Запуск контейнера

```bash
docker run -v <свой путь для сохранения модели>:/app freecad_container
```
