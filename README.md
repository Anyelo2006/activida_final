# Trabajo Final - Programación (Corte 1)
**Nombre:** Anyelo Rodríguez  
**Carrera:** Ingeniería de Sistemas  
**Tema:** Motor de Gráficas y Renderizado

## ¿De qué trata mi código?
Para este trabajo no quise usar el ejemplo de los carros porque ya muchos lo tenían. Decidí hacer un programa que simula cómo funciona un motor de video (como los que usan para hacer películas o juegos). 

El programa lo que hace es recibir un nombre de un proyecto y cuántas imágenes (frames) tiene que dibujar. 

## Cosas que le puse al código:
* **Seguridad de datos:** Use el doble guion bajo `__` para que nadie pueda cambiar el nombre del proyecto o los frames desde afuera sin permiso. Así protejo que el programa no falle.
* **Validación:** Le puse una regla para que si alguien intenta poner 0 o menos imágenes, el programa saque un error y no deje seguir.
* **Funciones extra:** Use algo llamado Mixins para que el programa pueda poner "filtros de brillo" y "avisar al correo" cuando termine, pero sin revolver todo el código principal.
* **Plano base:** Cree una base general para que todos los videos que se hagan sigan las mismas reglas.

## Cómo probarlo:
Solo hay que darle a "Play" en Python y en la pantallita de abajo saldrá el proceso del render con el nombre que le puse de ejemplo.
