> # Base de Datos - Unidad 1

---

> ## Temas

- [Qué es una base de datos](#que-es-una-base-de-datos)

- [Qué es un sistema de base de datos](#que-es-un-sistema-de-base-de-datos)

- [Ventajas de una base de datos](#ventajas-de-una-base-de-datos)

- [Sistemas gestores de bases de datos (SGDB o DBMS)](#sistema-gestor-de-base de-datos-(dmbs-o-sgbd))
  
  - [Lenguaje de Definición de Datos (LDD)](#lld)
  
  - [Lenguaje de Manipulación de Datos (LMD)](#lmd)

- [Introducción a las Restricciones de Integridad](#restricciones-de-integridad)

- [Procesamiento distribuido y la arquitectura cliente-servidor](#procesamiento-distribuido-y-laarquitectura-cliente-servidor)

- [Usuarios de BD](#usuarios)

- [El Administrador de Base de Datos (DBA)](#administrador-de-base-de-datos-(dba))

- [La independencia de los datos](#independencia-de-datos)
  
  - [Independencia Física](#administrador-de-base-de-datos-(dba))
  
  - [Independencia Lógica](#administrador-de-base-de-datos-(dba))

- [Arquitectura de los tres esquemas](#arquitectura-de-los-tres-esquemas)
  
  - [El nivel externo](#arquitectura-de-los-tres-esquemas)
  
  - [El nivel conceptual](#arquitectura-de-los-tres-esquemas)
  
  - [El nivel Interno](#arquitectura-de-los-tres-esquemas)

---

> ## Que es una Base de datos

Una colección de datos `persistentes` que pueden
`compartirse` e `interrelacionarse`, los cuales son recolectados y
explotados por los sistemas de información.

- **Persistente:** Significa que los datos estan en un almacenamiento estable, tal como disco magnetico/solido, etc

- **Compartir:** Significa que una misma DB puede tener varios usos y usuarios, proporciona una memoria comun, la cual es compartida por varias funciones ejecutadas por multiples usuarios

- **Interrelacion:** Significa que los datos almacenados como unidades separadas se pueden conectar para mostrar informacion mas completa

---

> ## Que es un sistema de Base de datos

Es un sistema computarizado, almacenado en un equipo informatico, cuyo proposito general es mantener la informacion y hacer que este disponible cuando se solicite.

**Componentes Principales**

- **Data:** los datos son la base de datos propiamente dicha

- **Hardware:** se refiere a los dispositivos de almacenamiento donde recide la DB

- **Software:** Esta compuesto por un conjunto de programas que se conoce como Sistema Gestor de Base de Datos (`SGBD` o `DMBS`: Data Base Managment System). Este sistema maneja todas las solicitudes formuladas por los usuarios.

- **Users:** Existen tres clases de usuarios: 
  
  - **El programador** de apps, crea programas que utilizan la base de datos
  
  - **El usuario final**, quien accede a la DB por medio de un lenguaje de consulta o de programas de aplicacion
  
  - **El administrador de la DB** (`DBA: Data Base Administrator`), quien se encarga del control general del sistema de base de datos

---

> ## Ventajas de una base de datos

- **Globalización de la información:** permite a los diferentes usuarios considerar la información como un recurso corporativo que carece de dueños específicos

- E**liminacion de informacion redundante**, duplicada

- **Eliminacion de Inconsistencia de la informacion:** solo de produce cuando existe redundancia de datos

- Permite **compartir informacion:** varios sistemas o usuarios pueden utilizar una misma entidad

- Permite mantener la **integridad de la informacion:** solo se almacena la informacion correcta

- **Independencia de datos:** significa que los datos y los programas que los usan están separados. Esto es útil porque permite cambiar cómo se almacenan o se organizan los datos sin afectar los programas que los utilizan.
  
  - **Independencia física**: Puedes cambiar la forma en que los datos se guardan en el hardware (por ejemplo, cambiar de disco duro o modificar la estructura de almacenamiento) sin afectar cómo los programas acceden a ellos.
  
  - **Independencia lógica**: Puedes modificar la estructura de los datos (como agregar una nueva columna en una tabla) sin que los programas que usan la base de datos dejen de funcionar.

---

> ## Sistema Gestor de Base de Datos (DMBS o SGDB)

Es un conjunto de componentes de software que permiten a los usuarios la creacion, el uso y el mantenimiento de DB, permitiendo a estos realizar la adquisicion, dispercion, mantenimiento, consultas y formateo de datos

**Caracteristicas**

- **Definición de la base de datos:** Lenguaje y herramientas gráficas para definir entidades, relaciones, restricciones de integridad y autorización de privilegios

- **Acceso no procedural:** Lenguaje y herramientas gráficas para acceder a los datos sin necesidad de código complicado

- **Desarrollo de aplicaciones:** Herramienta gráfica para desarrollar menús, formularios de captura de datos y reportes; los requerimientos de datos para los formularios y reportes se especifican utilizando un acceso no procedural

- **Interfase del lenguaje procedural:** Lenguaje que combina el acceso no procedural con las capacidades totales de un lenguaje de programación

- **Procesamiento de transacciones:** Mecanismos de control para prevenir la interferencia de usuarios simultáneos y recuperar datos perdidos en caso de una falla

- **Ajuste de la base de datos:** Herramientas para monitorear y mejorar el desempeño de la base de datos\

**Un DBMS proporciona 5 funcionalidades**

1. Conceder a multiples usuarios acceso simultaneo a una unica DB

2. Establecer y mantener normas de seguridad y derechos de acceso de los usuarios

3. Hacer respaldos de los datos de forma habitual y recuperarlos rapidamente en caso de que se produzca una falla 

4. Establecer reglas y normas de DB para protejer la integridad de los datos

5. Proporcionar definiciones y descripciones de 'diccionario' de los datos disponibles

Los DBMS proporcionan un `Lenguaje de Definición de Datos (LDD)`para especificar el esquema de la base de datos, un Lenguaje de `Manipulación de Datos (LMD)` para expresar las modificaciones de la base de datos y un `Lenguaje de Consulta para realizar las consultas` . En la práctica, estos no son lenguajes diferentes; simplemente **forman parte de un único lenguaje de bases de datos, como** `SQL`

> ## LLD

Lenguage de definicion de datos (LLD) `Es un lenguaje de programacion para definir estructuras de datos`

Los esquemas de bases de datos se especifican mediante un conjunto de definiciones expresadas mediante LLD

Un lenguaje de LLD es proporcionado por el  DBMS que permite a los usuarios realizar las tareas de **definicion de las estructuras que almacenaran los datos, asi como los procedimientos o funcionalidades que permitan consultarlos**

La definición de la estructura de la base de datos incluye tanto la creación inicial de los diferentes objetos que formarán la base de datos, como el mantenimiento de esa estructura

> ## LMD

Lenguaje de manipulacion de datos (LMD)

Se utiliza para la gestion de datos dentro de los objetos del esquema de la DB, permite al usuario llevar a cabo tareas de consultas o modificacion de datos, estas incluyen:

- La recuperacion de la iinformacion almacenada en la DB 

- La insercion de informacion nueva en la DB 

- El borrado de la informacion de la DB

- La modificacion de la informacion almacenada en la DB

(**El LMD  mas utilizado es SQL**)

 La parte implicada a la recuperacion de datos se denomina `Lenguaje de consultas`, es habitual usar las expresiones lenguaje de consultas y LMD como sinonimos

---

> ## Restricciones de integridad

El LDD también se usa para especificar más propiedades de los datos.
Los valores de los datos almacenados en la base de datos deben satisfacer ciertas restricciones de consistencia. El LDD proporciona elementos para especificar tales restricciones.

**Las restricciones de integridad garantizan la consistencia de los datos. cuando usuarios autorizadosrealizan modificaciones en la base de datos.**

- **Integridad Referencial:** La integridad referencial garantiza que la relación entre dos tablas permanezca sincronizada durante las operaciones de actualización y eliminación. Todas las bases de datos relacionales poseen esta propiedad gracias a que el DBMS vela por su cumplimiento.

- **Restricciones de dominio:** Se debe asociar un dominio de valores posibles a cada atributo Esto actúa como restricción de los valores que puede adoptar. Estas restricciones son la forma más elemental de restricción de integridad.

- **Restricciones sobre una sola relacion:** Entre estas restricciones de integridad permitidas se encuentran: 
  
  - **not null:** el valor nulo (null) es miembro de todos los dominios y, en consecuencia, de manera predeterminada es un valor legal para todos los atributos de SQL.
  
  - **unique:** La especificación unique ( A1, A2, …, Am), indica que los atributos A1, A2, …, Am forman una clave candidata; es decir, ningún par de tuplas de la relación puede ser igual en todos los atributos indicados.
  
  - **check():** la cláusula check(P) especifica un predicado P que deben satisfacer todas las tuplas de la relación. Ej: check (semestre in (´Otoño´, ´Invierno´))

---

> ## Procesamiento distribuido y la arquitectura cliente-servidor

Con el crecimiento de Internet y las redes, el **procesamiento distribuido** se ha vuelto esencial en los sistemas de bases de datos (DBMS). Este permite que computadoras ubicadas en distintos lugares trabajen juntas para acceder a los datos.

Las **empresas** y **organizaciones** usan cada vez más bases de datos remotas disponibles en Internet. Los DBMS aprovechan la red y la capacidad local para ofrecer un acceso eficiente.

Muchos DBMS utilizan una **arquitectura cliente-servidor**, donde:

- El **cliente** envía solicitudes,

- y el **servidor** las procesa.

Esta arquitectura permite distribuir mejor el software y los datos, mejorando el rendimiento y la disponibilidad.

> ## Arquitectura cliente-servidor

El DBMS proporciona el software que se puede ejecutar en el cliente y en el servidor

- El software del cliente sea responsable de aceptar comandos de l usuario, desplegar los resultados y realizar algun procesamiento de datos 

- El software del servidor valida las peticionesx de los clientes, localiza bases de datos remotas, las actualiza, y envia datos al cliente en in formato que el pueda entender 

---

> ## Usuarios

Hay tipos diferentes de usuarios en los sistemas de DB, se clasifican segun su forma de interactuar con el sistema:

| Tipo de Usuario                   | Descripción                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Usuarios normales**             | - No técnicos.<br>- Usan programas ya creados.<br>- Interactúan con formularios o leen informes.        |
| **Programadores de aplicaciones** | - Profesionales informáticos.<br>- Escriben programas que acceden a la base de datos.                   |
| **Usuarios sofisticados**         | - No escriben programas.<br>- Realizan consultas directamente en SQL o con herramientas de análisis.    |
| **Usuarios especializados**       | - Usuarios avanzados.<br>- Desarrollan aplicaciones complejas como sistemas expertos o multimedia.      |
| **DBA (Administradores de BD)**   | - Administran el sistema de bases de datos.<br>- Se encargan de seguridad, rendimiento y mantenimiento. |

---

> ## Administrador de Base de Datos (DBA)

Persona responsable del control central del sistema de base de datos. Sus funciones principales son:

- **Definir el esquema** de la base de datos y los métodos de acceso (usando LDD).
- **Modificar** el esquema y la organización física para adaptarse a cambios o mejorar el rendimiento.
- **Gestionar autorizaciones** de acceso a los datos para distintos usuarios.
- **Mantenimiento rutinario**, incluyendo:
  - Copias de seguridad periódicas.
  - Gestión y ampliación del espacio en disco.
  - Monitoreo del rendimiento del sistema y de los trabajos en ejecución.

---

> ## Independencia de Datos

- En los primeros DBMS, las bases de datos estaban muy ligadas a los programas que las usaban.
- Esto generaba **problemas de mantenimiento** en el software.
- Para resolverlo, surgió el concepto de **independencia de datos**.
- Significa que la base de datos tiene una **identidad separada** de las aplicaciones (programas, formularios, reportes).
- Esta separación permite que se puedan hacer **cambios en la definición física o lógica** de la base de datos **sin afectar las aplicaciones** que la usan.

| Tipo de Independencia    | Descripción                                                                                                                                                                                               |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Independencia Física** | Permite **modificar el esquema físico** sin necesidad de reescribir los programas de aplicación. <br> *Ejemplo:* Reorganizar ficheros físicos para mejorar el rendimiento en consultas o actualizaciones. |
| **Independencia Lógica** | Permite **modificar el esquema conceptual** sin afectar los programas de aplicación. <br> *Ejemplo:* Agregar un nuevo campo (como CUIT en clientes) sin alterar los programas que usan la base de datos.  |

---

> ## Arquitectura de los Tres Esquemas

El modelo de **tres esquemas** permite separar los datos en distintos niveles para lograr **independencia de datos**:  

| Nivel                | Descripción                                                                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nivel Externo**    | Es la vista del usuario. Cada grupo de usuarios tiene una vista específica de la base de datos según sus necesidades (formularios, reportes). |
| **Nivel Conceptual** | Define la estructura lógica de la base de datos, incluyendo entidades y relaciones. Representa el significado de los datos.                   |
| **Nivel Interno**    | Define la estructura de almacenamiento físico de los datos en archivos y dispositivos como discos duros. Permite optimizar el rendimiento.    |

Este enfoque permite modificar la **estructura interna** o **conceptual** sin afectar la forma en que los usuarios ven los datos.  