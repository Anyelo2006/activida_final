# 🚗 Sistema de Gestión de Vehículos - Uniguajira
**Estudiante:** Anyelo  
**Facultad:** Ingeniería
**programa:**ingenieria en sistema 
**Asignatura:** Programacion avanzada  


---

## 📝 Descripción del Proyecto
Este proyecto es una solución integral diseñada en **Python** que aplica los pilares fundamentales de la POO mediante una analogía de gestión de sucursales automotrices[cite: 19]. El sistema integra el control de flota, registros de mantenimiento y validación de pólizas de seguro en una única interfaz de software.

---

## 🛠️ Conceptos de Programación Aplicados
Para cumplir con los requisitos de la actividad final, se implementaron los siguientes conceptos:

***Abstracción (ABC):** Se definió una clase padre abstracta `Gestion_vehiculos` que establece el contrato obligatorio para todas las sucursales.
***Herencia Múltiple:** La clase final `VehiculoFinal` hereda simultáneamente de tres clases diferentes para combinar funcionalidades.
***Encapsulamiento Robusto:** Uso de atributos protegidos (`_`) y privados (`__`) para garantizar la integridad de los datos técnicos.
***Decoradores (@property):** Implementación de *Getters* y *Setters* con validación lógica para el control de kilometraje.
***Polimorfismo:** Demostración de métodos heredados ejecutándose en múltiples instancias de objetos.

---

## 🚀 Instrucciones de Uso
Para ejecutar el script y verificar las pruebas de validación, sigue estos pasos:

1.  Asegúrate de tener instalado **Python 3.10+**.
2.  Clona o descarga este repositorio.
3.  Abre una terminal en la carpeta del proyecto.
4.  Ejecuta el comando:
    ```bash
    python ejercicio.py
    ```

---

## 📊 Estructura de la Clase Final
La clase `VehiculoFinal` integra los siguientes módulos:
1.  **Gestión Base:** Control de sucursal y lista de unidades.
2.  **Mantenimiento:** Seguimiento de fechas de revisión técnica.
3.  **Seguridad:** Validación de pólizas de seguro activas.

---
> [cite_start]**Nota para el Evaluador:** El código incluye el bloque `if __name__ == "__main__":` para realizar pruebas automáticas de encapsulamiento y polimorfismo según los criterios exigidos[cite: 15, 46].
