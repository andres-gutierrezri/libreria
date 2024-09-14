-- INSERTAR LIBROS

-- SELECCIONAR BASE DE DATOS
USE libreria;
SET NAMES utf8mb4;

-- SELECCIONAR TABLA
SELECT * FROM libreria_libro ORDER BY titulo asc;

-- REINICIAR INCREMENTO
ALTER TABLE libreria_libro AUTO_INCREMENT = 1;

-- INSERTAR VALORES
INSERT INTO libreria_libro (titulo, imagen, descripcion) VALUES ('Como Programar en C, C++ y Java', 'publico/caratulas/Programar-C-Java.jpg', 'Esta cuarta edición del libro de C más utilizado a nivel mundial, explica de manera clara y sencilla el lenguaje C, y presenta temas importantes de C++ y Java.');

INSERT INTO libreria_libro (titulo, imagen, descripcion) VALUES ('Física Universitaria', 'publico/caratulas/Fisica-Universitaria-V1.png', 'Este libro es el producto de más de medio siglo de innovaciones en la enseñanza de la física. Cuando apareció fue considerado como revolucionario entre los libros de texto basados en el cálculo, por su énfasis en los principios fundamentales de la física y en la forma de aplicarlos.');

INSERT INTO libreria_libro (titulo, imagen, descripcion) VALUES ('Ecuaciones Diferenciales con Aplicaciones de Modelado', 'publico/caratulas/Ecuaciones-Diferenciales.png', 'Una obra que se ha caracterizado por una exposición clara y sencilla en la enseñanza de las ecuaciones diferenciales, y por la creación de modelos y el empleo de la tecnología para solucionar problemas.');

INSERT INTO libreria_libro (titulo, imagen, descripcion) VALUES ('Cálculo con Geometría Analítica', 'publico/caratulas/Calculo-Geometria.jpg', 'Para escribir este libro, los editores convocaron a diversos colegas de la comunidad mexicana de investigadores de Matemática Educativa para proponer escritos que persiguieran el objetivo de introducir al lector a la complejidad de la problemática que atiende la Matemática Educativa.');

INSERT INTO libreria_libro (titulo, imagen, descripcion) VALUES ('Fundamentos de Circuitos Eléctricos', 'publico/caratulas/Fundamentos-Circuitos-Electricos.png', 'Fundamentos de Circuitos eléctricos se ha convertido en la elección de los estudiantes para un curso introductorio de circuitos eléctricos. La tercera edición continúa en esta línea basándose en el éxito de las ediciones anteriores, con nuevas características para alumnos y profesores Incluye ejemplos de aplicaciones industriales prácticas.');

INSERT INTO libreria_libro (titulo, imagen, descripcion) VALUES ('Variables Complejas y Aplicaciones', 'publico/caratulas/Variables-Complejas-Aplicaciones.jpg', 'Este libro es una revisión de la sexta edición, publicada en USA en 1996. Esta edición, al igual que las anteriores, ha servido como libro de texto en cursos de introducción a la teoría y aplicaciones de las funciones de variable compleja. Esta nueva edición mantiene el contenido básico y el estilo de las que la precedieron. En esta edición, los cambios más relevantes aparecen en los nueve primeros capítulos, que constituyen el núcleo de un curso básico.');

-- SELECCIONAR TABLA
SELECT titulo, imagen FROM libreria_libro;