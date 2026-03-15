# 💰 Gestor de Finanzas Personales (Python + MySQL)

Este es un sistema de escritorio robusto desarrollado en **Python** para el control detallado de finanzas personales. A diferencia de sistemas básicos, este proyecto integra una base de datos **MySQL** para el manejo profesional de grandes volúmenes de datos y persistencia segura.

## 🚀 Funcionalidades Principales
- **Registro Detallado:** Permite ingresar descripción, monto, fecha, tipo (Ingreso/Egreso) y **categoría**.
- **Balance Automático:** Calcula el saldo real en tiempo real restando gastos de ingresos.
- **Historial Formateado:** Visualización de movimientos en una tabla organizada directamente en la consola.
- **Gestión de Datos:** Capacidad para eliminar registros específicos mediante ID.
- **Arquitectura Modular:** Código organizado en capas (Configuración, Consultas y Lógica) para facilitar el mantenimiento.

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.x
- **Base de Datos:** MySQL 8.0
- **Conector:** `mysql-connector-python`
- **IDE:** Visual Studio Code en Windows 11

## 📋 Requisitos Previos
1. Tener instalado **MySQL Server** y **MySQL Workbench**.
2. Instalar el conector de Python mediante la terminal:
   ```bash
   pip install mysql-connector-python


⚙️ Configuración del Entorno
Base de Datos: Ejecuta el siguiente script en tu cliente SQL (como MySQL Workbench) para crear la estructura necesaria:

CREATE DATABASE gestor_finanzas;
USE gestor_finanzas;

CREATE TABLE transacciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    descripcion VARCHAR(255),
    categoria VARCHAR(50) DEFAULT 'General',
    tipo ENUM('Ingreso', 'Egreso'),
    monto DECIMAL(10, 2)
);


📁 Estructura del Proyecto
main.py: Interfaz de usuario, manejo del menú interactivo y validación de entradas.

consultas.py: Lógica de comunicación con el servidor MySQL (operaciones CRUD).

db_config.py: Parámetros de conexión y función para obtener el objeto de conexión.

👤 Autor
Inosencio Perez

GitHub: Inosencio-Perez

Este proyecto es parte de mi portfolio de desarrollo backend, enfocado en la integración de bases de datos relacionales y diseño de software modular.