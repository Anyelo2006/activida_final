# 🚗 Sistema de Gestión de Vehículos - Uniguajira
**Estudiante:** Anyelo  
**Facultad:** Ingeniería de Sistemas  
**Asignatura:** Programación Orientada a Objetos (POO)  
**Corte:** #1

---

## 📝 Descripción del Proyecto
[cite_start]Este proyecto es una solución integral diseñada en **Python** que aplica los pilares fundamentales de la POO mediante una analogía de gestión de sucursales automotrices[cite: 19]. [cite_start]El sistema integra el control de flota, registros de mantenimiento y validación de pólizas de seguro en una única interfaz de software[cite: 12].

---

## 🛠️ Conceptos de Programación Aplicados
[cite_start]Para cumplir con los requisitos de la actividad final[cite: 9, 44], se implementaron los siguientes conceptos:

* [cite_start]**Abstracción (ABC):** Se definió una clase padre abstracta `Gestion_vehiculos` que establece el contrato obligatorio para todas las sucursales[cite: 19, 20].
* [cite_start]**Herencia Múltiple:** La clase final `VehiculoFinal` hereda simultáneamente de tres clases diferentes para combinar funcionalidades[cite: 36].
* [cite_start]**Encapsulamiento Robusto:** Uso de atributos protegidos (`_`) y privados (`__`) para garantizar la integridad de los datos técnicos[cite: 38].
* [cite_start]**Decoradores (@property):** Implementación de *Getters* y *Setters* con validación lógica para el control de kilometraje[cite: 39, 40].
* [cite_start]**Polimorfismo:** Demostración de métodos heredados ejecutándose en múltiples instancias de objetos[cite: 42].

---

## 🚀 Instrucciones de Uso
[cite_start]Para ejecutar el script y verificar las pruebas de validación, sigue estos pasos[cite: 17, 46]:

1.  Asegúrate de tener instalado **Python 3.10+**.
2.  Clona o descarga este repositorio.
3.  Abre una terminal en la carpeta del proyecto.
4.  Ejecuta el comando:
    ```bash
    python ejercicio.py
    ```

---

## 📊 Estructura de la Clase Final
[cite_start]La clase `VehiculoFinal` integra los siguientes módulos[cite: 35, 36]:
1.  **Gestión Base:** Control de sucursal y lista de unidades.
2.  **Mantenimiento:** Seguimiento de fechas de revisión técnica.
3.  **Seguridad:** Validación de pólizas de seguro activas.

---
> [cite_start]**Nota para el Evaluador:** El código incluye el bloque `if __name__ == "__main__":` para realizar pruebas automáticas de encapsulamiento y polimorfismo según los criterios exigidos[cite: 15, 46].
