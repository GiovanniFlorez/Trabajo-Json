from modelo import _Modelo
from vista import Vista
from controlador import Controlador

if __name__ == "__main__":
    modelo = _Modelo('datos_privados.json')
    vista = Vista()
    controlador = Controlador(modelo, vista)
    controlador.ejecutar()  
