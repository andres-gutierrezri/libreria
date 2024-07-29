-- INSERTAR LIBROS

-- SELECCIONAR BASE DE DATOS
USE libreria;
SET NAMES utf8;

-- SELECCIONAR TABLA
SELECT * FROM libreria_libro ORDER BY titulo asc;

-- REINICIAR INCREMENTO
ALTER TABLE libreria_libro AUTO_INCREMENT = 1;

-- INSERTAR VALORES
INSERT INTO libreria_libro (titulo, imagen, descripcion) VALUES ('Como Programar en C, C++ y Java', 'media/Programar-C-Java.jpg', 'Esta cuarta edición del libro de C más utilizado a nivel mundial, explica de manera clara y sencilla el lenguaje C, y presenta temas importantes de C++ y Java.');

INSERT INTO libreria_libro (titulo, imagen, descripcion) VALUES ('Física Universitaria', 'media/Fisica-Universitaria-V1.png', 'Este libro es el producto de más de medio siglo de innovaciones en la enseñanza de la física. Cuando apareció fue considerado como revolucionario entre los libros de texto basados en el cálculo, por su énfasis en los principios fundamentales de la física y en la forma de aplicarlos.');

INSERT INTO libreria_libro (titulo, imagen, descripcion) VALUES ('Ecuaciones Diferenciales con Aplicaciones de Modelado', 'media/Ecuaciones-Diferenciales.png', 'Una obra que se ha caracterizado por una exposición clara y sencilla en la enseñanza de las ecuaciones diferenciales, y por la creación de modelos y el empleo de la tecnología para solucionar problemas.');

INSERT INTO libreria_libro (titulo, imagen, descripcion) VALUES ('Cálculo con Geometría Analítica', 'media/Calculo-Geometria.jpg', 'Para escribir este libro, los editores convocaron a diversos colegas de la comunidad mexicana de investigadores de Matemática Educativa para proponer escritos que persiguieran el objetivo de introducir al lector a la complejidad de la problemática que atiende la Matemática Educativa.');

-- SELECCIONAR TABLA
SELECT * FROM libreria_libro;