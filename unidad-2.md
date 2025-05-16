> # Base de Datos - Unidad 2

---

> ## Temas

- [Proceso y Ciclo de vida para la creación de una BD](#ciclo-de-vida-clasico)
- [Fases del diseño de una base de datos](#fases-de-diseño-de-una-base-de-datos)
- [Análisis de requisitos](#analisis-de-requisitos)
- [Diseño conceptual](#diseño-conceptual)
- [El Modelo Entidad-Relación](#der)
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

La primera fase de una base de datos consiste en conocer y analizar con detalle las expectativas, las necesidades y los objetivos de los futuros usuarios de la DB

Recogida de requisitos

- Identificar los principales usuarios y las principales areas en las que se usara la DB

- Analizar la documentación existenete relativa a las apps en uso

- Estudio las entradas, el flujo y las salidas

- Hacer entrevistas y encuestas a futuros usuarios

Estructuracion de los requisitos

- Se debe tener en cuenta que algunos de estos requisitos, muy
  probablemente, cambiarán durante el proceso de diseño y que
  hay que estar atentos y en contacto permanente con los
  usuarios de la base de datos para detectar posibles problemas.

Formalización de los requisitos

- El objetivo es convertir los requisitos a un formato estructurado
  mediante técnicas de especificación de requisitos como, por ej,
  diagramas de flujo de datos (DFD)

---

> ## Diseño Conceptual

La fase de diseño conceptual tiene como objetivo crear un esquema conceptual de alto nivel, en esta fase todavia no se considera el tipo de BD ni el DBMS en concreto que se utilizara

---

> ## DER

modelo conceptual de datos: una coleccion de herramientas conceptuales para la descripción de `DATOS`, `RELACIONES` de entrada, `SEMANTICA` (significado), `RESTRICCIONES` de consistencia.

Los modelos conceptuales hacen el modelo SEMANTICO de los datos

consiste en estudiar los datos que se pretenden almacenar en una base, antes de elegir el modelo que se va a usar 

![](C:\Users\Administrador\AppData\Roaming\marktext\images\2025-05-13-11-05-28-image.png)

Modelo entidad-relación

- Se trata de un modelo que sirve para crear esquemas conceptuales de bases de
  datos. Es prácticamente un estándar.
  Es un modelo de datos basado en una percepción del mundo real que consiste en
  un conjunto de objetos básicos llamados entidades y relaciones entre estos objetos,
  implementándose en forma gráfica a través del Diagrama Entidad Relación.

`Entidad:`Se trata de cualquier objeto u elemento (real o abstracto) acerca del cual se pueda almacenar información en la base de datos.

Una entidad no es una propiedad concreta sino un objeto que puede poseer múltiples propiedades (`atributos`).

`Relaciones:`Representan asociaciones entre entidades. Es el elemento del modelo que permite relacionar en sí los datos del modelo

<img src="file:///C:/Users/Administrador/AppData/Roaming/marktext/images/2025-05-13-11-14-15-image.png" title="" alt="" width="648">

`Cardinalidad:` Indica el número de relaciones en las que una entidad puede aparecer. Puede definir ciertas restricciones a las que la base de datos se deben adaptar.

<img src="file:///C:/Users/Administrador/AppData/Roaming/marktext/images/2025-05-13-11-17-50-image.png" title="" alt="" width="653">

<img src="file:///C:/Users/Administrador/AppData/Roaming/marktext/images/2025-05-13-11-18-15-image.png" title="" alt="" width="236">

`Atributos:`

<img src="file:///C:/Users/Administrador/AppData/Roaming/marktext/images/2025-05-13-11-19-28-image.png" title="" alt="" width="702">

![](C:\Users\Administrador\AppData\Roaming\marktext\images\2025-05-13-11-21-09-image.png)
