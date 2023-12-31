<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>
# Dummy Transformations
[![codecov](https://codecov.io/gh/IslasGECI/dummy_transformations/graph/badge.svg?token=wyxnwZypMA)](https://codecov.io/gh/IslasGECI/clean_camera_data)
![example branch
parameter](https://github.com/IslasGECI/dummy_transformations/actions/workflows/actions.yml/badge.svg)
![licencia](https://img.shields.io/github/license/IslasGECI/dummy_transformations)
![languages](https://img.shields.io/github/languages/top/IslasGECI/dummy_transformations)
![commits](https://img.shields.io/github/commit-activity/y/IslasGECI/dummy_transformations)
![PyPI - Version](https://img.shields.io/pypi/v/dummy_transformations)

Para usar este repo como plantilla debemos hacer lo siguiente:

1. Presiona el botón verde que dice _Use this template_
1. Selecciona como dueño a la organización IslasGECI
1. Agrega el nombre del nuevo módulo de python
1. Presiona el botón _Create repository from template_
1. Reemplaza `dummy_transformations` por el nombre del nuevo módulo en:
    - `Makefile`
    - `pyproject.toml`
    - `tests\test_transformations.py`
1. Renombra el archivo `dummy_transformations\transformations.py` al nombre del primer archivo del
   nuevo módulo
1. Cambia la descripción del archivo `dummy_transformations\__init__.py`
1. Renombra el directorio `dummy_transformations` al nombre del nuevo módulo
1. Cambia el `codecov_token` del archivo `Makefile`

Los archivos del nuevo módulo los agregarás en la carpeta que antes se llamaba
`dummy_transformations` y las pruebas en la carpeta `tests`.
