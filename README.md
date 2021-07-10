# 8-puzzle

_El 8-puzzle un pequeño juego que consiste en llevar de un estado inicial a un estado final.
Se conforma de 9 casillas y 8 fichas numeradas, gracias al hueco que se forma es posible realizar movimientos._

<img src="https://raw.githubusercontent.com/YisusYaro/8-puzzle/master/ss.png">

### Instalación 🔧

_Instalar librerías por pip o pip3_

```
pip3 install numpy matplotlib tk
```

_Usando Docker :whale:_

```
docker build -t 8-puzzle .  
```

## Ejecución 📦

_Usar el siguiente comando_

```
python3 main.py
```

_Usando Docker :whale:_

```
docker run -it --rm \
    --user=$(id -u $USER):$(id -g $USER) \
    --env="DISPLAY" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    8-puzzle  
```

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [numpy](http://www.dropwizard.io/1.0.2/docs/) - Soporte para vectores y matrices
* [matplotlib](https://maven.apache.org/) - Generación de gráficos
* [tkinter](https://rometools.github.io/rome/) -  Binding de la biblioteca gráfica Tcl/Tk

## Autores ✒️

* **Jesús Alejandro Yahuitl Rodríguez** - [YisusYaro](https://github.com/YisusYaro)

## Licencia 📄

Este proyecto está bajo la Licencia (MIT License) - mira el archivo [LICENSE](LICENSE) para detalles

---
⌨️ con ❤️
