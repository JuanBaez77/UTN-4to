> # Base de Datos - Unidad 2

---

> ## Temas

- [Proceso y Ciclo de vida para la creación de una BD](#ciclo-de-vida-clasico)
- [Fases del diseño de una base de datos](#fases-de-diseño-de-una-base-de-datos)
- Análisis de requisitos
- Diseño conceptual
- El Modelo Entidad-Relación
  - Entidades - Tipos de entidades
  - Relaciones
  - Cardinalidad
  - Atributos – Tipos de atributos
  - Entidades ISA

---

> ## Ciclo de vida clasico

![](C:\Users\Administrador\AppData\Roaming\marktext\images\2025-04-04-16-25-11-image.png)

1. Análisis de requisitos Recabar información sobre el uso que se piensa dar a la base de datos (requisitos del sistema). 

2. Diseño conceptual (modelo E/R)
   Creación de un esquema conceptual de la base de datos independiente del DBMS que se vaya a utilizar. Diagrama Entidad-Relación (DER) 

3. Elección del sistema gestor de bases de datos Elección del modelo de datos (tipo de DBMS) y del DBMS concreto (p.ej. Modelo Relacional: MySQL – PostgreSQL) 

4. Diseño lógico Creación del esquema lógico para el modelo de datos del DBMS elegido (p.ej. paso del DER a un Esquema Lógico Relacional). 

5. Diseño físico Implementación de la base de datos utilizando el DDL del DBMS elegido (MySQL) (lenguaje de definición de datos del DBMS). 

6. Uso y mantenimiento Gestión de los datos utilizando el DML (lenguaje de manipulación de datos del DBMS).

---

> ## Fases de diseño de una base de datos

| **Fase**                             | **Descripción**                                                                                             |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| 🌍 **Mundo Real**                    | Contiene la información tal cual la percibimos. Es el punto de partida junto con el análisis de requisitos. |
| 🔍 **Análisis de Requisitos**        | Identificación de la información que se debe almacenar y cómo se usará.                                     |
| 🎨 **Diseño Conceptual**             | Representa el modelo de datos **independiente del DBMS**. Se usa el **Modelo Entidad-Relación**.            |
| 🖥️ **Diseño Lógico**                | Transforma el modelo conceptual a un **formato más cercano al DBMS** (Ej: Relacional, de Red, Jerárquico).  |
| 🏗️ **Diseño Físico**                | Representa los datos según el **modelo concreto del DBMS** (Ej: MySQL, PostgreSQL).                         |
| ⚙️ **Implementación y Optimización** | Se cargan los datos y se ajustan los parámetros del modelo físico para mejorar el rendimiento.              |

---

> ## Analisis de requisitos


