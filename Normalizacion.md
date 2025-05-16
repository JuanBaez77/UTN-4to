> # Unidad 4 - Normalizacion

---

> ## Indice

- [Normalización.](#normalizacion)
- Formas normales.
- Primera, segunda y tercera formas normales (1FN-2FN-3FN).
- Beneficios de la Normalización.
- Las 12 reglas de Codd

---

> ## Normalizacion

La normalizacion es una tecnica que busca dar eficiencia y fiabilidad a una BD relacional, su objetivo es:

- Llevar informacion a una estructura dende prime el aprovechamiento del espacio

- Eficiencia y rapidez en el manejo de la informacion

Permite detectar y eliminar diversos problemas de dise;o logico forzando a la division de una tabla en dos o mas.

 **Dependencia Funcional**: Se dice que existe depenedencia entre dos atributos de una tabla si para cada valor del primer atributo existe un solo valor del segundo

---

> ## Formas normales

Creador de la teoria de Normalizacion: `Edgar F. Codd`

En general las primeras tres formas normales son suficientes para cubrir las necesidades de la mayoria de las BD

## Primera forma normal (1FN)

Es una forma normal inherente al esquema relacional, se dice que una tabla se encuentra en 1FN si los dominios de todos los atributos son atomicos

![](C:\Users\Administrador\AppData\Roaming\marktext\images\2025-05-15-15-33-18-image.png)

## Segunda forma normal (2FN)

Si esta en 1FN y cada atributo que no sea clave, depende de forma funcional completa respecto de la clave principal

La clave principal debe hacer dependientes al resto de atributos, si hay atributos que dependen solo de una parte de la clave, entonces sea parte de la clave y esos atributos  formarian otra tabla 

No cumple la 2FN:

<img src="file:///C:/Users/Administrador/AppData/Roaming/marktext/images/2025-05-15-15-38-00-image.png" title="" alt="" width="591">

Si cumple la 2FN:

<img src="file:///C:/Users/Administrador/AppData/Roaming/marktext/images/2025-05-15-15-38-10-image.png" title="" alt="" width="583">

## Tercera forma normal (3FN)

Si esta en 2FN y ademas ningun atributo que no sea clave depende funcional mente de forma transitiva de la clave primaria

![](C:\Users\Administrador\AppData\Roaming\marktext\images\2025-05-15-16-37-40-image.png)
