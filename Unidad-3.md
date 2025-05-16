> # Unidad - 3: Modelos de DB

---

> ## Indice

- Modelos de Base de Datos
  - Relacionales (SQL) VS No Relacionales (NOSQL)
- Modelos Relacionales
  - Modelo Jerárquico
  - Modelo de Red
  - Modelo Relacional
- Modelo Relacional
  - Conceptos básicos
  - La estructura de las bases de datos relacionales
  - Generalidades
  - Claves
  - Esquemas de la relación y Ejemplar de la relación
  - Esquemas de BD y Diagramas de Esquemas de BD
  - Lenguajes De Consulta Relacional
  - Algebra Relacional y Cálculo Relacional
  - Definiciones del Modelo Relacional
  - Objetivos del Modelo Relacional
  - Características del Modelo Relacional

---

> ## Modelos de Base de Datos

Mientras las bases de datos SQL tienen como prioridad la integridad de los datos, las NoSQL priorizan el rápido acceso a ellos, aún a costa de sacrificar la integridad de los datos.

### ⚔️ **SQL vs NoSQL – Diferencias clave**

| Característica              | **SQL** (Relacional)                      | **NoSQL** (No Relacional)                               |
| --------------------------- | ----------------------------------------- | ------------------------------------------------------- |
| 📊 **Modelo de datos**      | Basado en **tablas** (filas y columnas)   | Basado en **documentos, grafos, clave-valor, etc.**     |
| 🛠️ **Esquema**             | **Fijo y estructurado**                   | **Flexible o dinámico**                                 |
| 🔍 **Consultas**            | Usa el lenguaje **SQL** (estándar)        | Cada DB tiene su propio lenguaje (ej. MongoDB usa JSON) |
| ⚙️ **Transacciones (ACID)** | **Sí**, soporte completo                  | Parcial o eventual (depende del motor)                  |
| 📈 **Escalabilidad**        | Escala **verticalmente** (mejor hardware) | Escala **horizontalmente** (más máquinas)               |
| 🧠 **Relaciones complejas** | Muy eficientes y naturales                | Menos eficientes o requieren diseño especial            |
| 🗄️ **Ejemplos**            | MySQL, PostgreSQL, SQL Server, Oracle     | MongoDB, Cassandra, Redis, CouchDB                      |

---

> ## Modelos Relacionales

`Modelo Jerarquico`: La forma de esquematizar la información se realiza a través de representaciones jerárquicas o relaciones de padre/hijo, de manera similar a la estructura de un árbol. Así, el modelo jerárquico puede representar dos tipos de relaciones entre los datos: `relaciones de uno a uno` y `relaciones de uno a muchos`

<img src="file:///C:/Users/Administrador/AppData/Roaming/marktext/images/2025-05-13-11-47-29-image.png" title="" alt="" width="591">

La representación de información donde se requieran relaciones de muchos a muchos tiene a complicarse, de tal forma que si un hijo llega a tener dos o más padres, la información de este hijo debe almacenarse en varios lugares diferentes de la base de datos.

Otra `dificultad` que presenta el modelo jerárquico de representación de datos es respecto a las bajas, en este caso, si se desea dar de baja a un padre, ello necesariamente implicará dar de baja a todos y cada uno de los hijos que dependen de este padre.

---

`Modelo de red:`Este modelo de datos facilita la representación de relaciones de muchos a muchos, permitiendo que cualquier registro en la base de datos tenga múltiples ocurrencias superiores. Esta era una de las limitaciones clave del modelo Jerarquico donde la informacion se repetia, `El modelo de red ELMINA la redundancia informativa `

<img src="file:///C:/Users/Administrador/AppData/Roaming/marktext/images/2025-05-13-11-52-41-image.png" title="" alt="" width="594">

Sin embargo, presenta desventajas, como su complejidad en el diseño y el mantenimiento, y las consultas pueden resultar más complicadas de redactar.

---

> ## Modelo relacional

`Modelo Relacional:`Una base de datos relacional consiste en un conjunto de tablas, a cada una de las cuales se le asigna un nombre único.

En el **modelo relacional**, los datos se organizan en **tablas**.

- Cada **fila** representa una **tupla**, que es una **secuencia de valores**.

- Cada **tupla** expresa una **relación** entre esos valores.

- Por eso, en matemáticas, a las tablas se las llama también **relaciones**.

En síntesis:  
**Tabla = colección de relaciones = conjunto de tuplas = filas con datos estructurados.**

<img src="file:///C:/Users/Administrador/AppData/Roaming/marktext/images/2025-05-13-11-57-49-image.png" title="" alt="" width="585">

Resumiendo, en el modelo relacional, el término relación se utiliza para referirse a
una `tabla`, siendo este último el mas usado. 

Mientras que el término `tupla` se utiliza para referirse a una fila. 

De forma similar, el término `atributo` se refiere a una columna de una tabla. El orden en que las tuplas aparecen en una tabla es irrelevante, ya que la tabla es un conjunto de tuplas

---

### 🔍 **Modelo Relacional – Dominio y Atomicidad**

- Cada **atributo** en una tabla tiene un **dominio**, que es el conjunto de valores válidos para ese atributo (tipo y formato).

- Un **dominio atómico** tiene **valores indivisibles**, es decir, no debe haber listas o conjuntos de datos dentro de un solo campo.

🔴 **Ejemplo de error**:  
Un campo de teléfono que almacena varios números juntos **no es atómico**.

✅ **Ejemplo correcto**:  
Un campo que almacena **un solo número** por fila.

💡 **Clave**:

> La **atomicidad** asegura la **integridad** y la **normalización** de los datos, facilitando su gestión y consulta.

---

### 🔐 **Modelo Relacional – Claves**

- Cada **tupla** debe ser **única**: no puede haber dos filas con exactamente los mismos valores en todos sus atributos.

#### 🔹 Superclave

- Conjunto de uno o más atributos que identifican de forma única una tupla.

- Ej: `{ID}` es una superclave.

#### 🔹 Claves candidatas

- Son **superclaves mínimas**, es decir, los conjuntos más pequeños posibles que aún identifican unívocamente una tupla.

- Ej: `{ID}` y `{nombre, nombre_dept}` son claves candidatas.

- `{ID, nombre}` **no lo es**, porque `ID` ya es suficiente.

#### 🔹 Clave primaria

- Es la **clave candidata elegida** para identificar oficialmente las tuplas.

- Debe ser **estable**: sus valores no deben cambiar (o hacerlo muy raramente).

### 🔗 **Clave Foránea (Foreign Key)**

- Una **clave foránea** es un atributo que **hace referencia** a la **clave primaria de otra entidad**.

- Sirve para **relacionar tablas** entre sí.

🔁 **Ejemplo**:  
`id_equipo` en la entidad **JUGADOR** es clave foránea porque apunta a `id_equipo` en **EQUIPO**, donde es clave primaria.

🧠 **Idea clave**:

> Las claves foráneas permiten mantener la **integridad referencial** entre entidades relacionadas.

![](C:\Users\Administrador\AppData\Roaming\marktext\images\2025-05-13-12-29-11-image.png)
