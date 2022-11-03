create database alumnos;
use alumnos; 
-- DROP TABLE alumnos;
-- DROP TABLE cursos;

CREATE TABLE cursos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    color TEXT,
    dificultad ENUM('FACIL','MEDIO','DIFICIL')
);

CREATE TABLE alumnos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    ape_paterno VARCHAR(50) NOT NULL,
    ape_materno VARCHAR(50) NOT NULL,
    correo VARCHAR(250) UNIQUE NOT NULL,
    num_emergencia VARCHAR(10),
    -- Creo una columna referenciando segun el nombre de la tabla_nombre columna
    curso_id INT,
    -- Ahora relacionamos esa columna con la tabla alumnos
    FOREIGN KEY(curso_id) REFERENCES cursos(id)
);
INSERT INTO cursos VALUES   (DEFAULT, 'MATEMATICA', 'AMARILLO', 'MEDIO'),
                            (DEFAULT, 'CTS', 'NARANJA', 'DIFICIL'),
                            (DEFAULT, 'ARTE', 'MORADO', 'FACIL'),
                            (DEFAULT, 'EDUCACION FISICA', 'VERDE', 'MEDIO'),
                            (DEFAULT, 'INGLES', 'CELESTE', 'FACIL'),
                            (DEFAULT, 'COMUNICACION', 'ROJO', 'DIFICIL');

INSERT INTO alumnos VALUES  (DEFAULT, 'Eduardo', 'de Rivero', 'Manrique', 'ederiveroman@gmail.com','974207075',1),
                            (DEFAULT, 'Carla', 'Monterrosa', 'Macedo', 'cmonterrosa@gmail.com','974207074',3),
                            (DEFAULT, 'Juan', 'Perez', 'Rodriguez', 'jperez@gmail.com','974207076',5),
                            (DEFAULT, 'Rodrigo', 'Buenaventura', 'Rodrigues', 'rbuenaventura@gmail.com','974159075',2),
                            (DEFAULT, 'Sofia', 'Baldarrago', 'Vera', 'sbaldarrago@gmail.com','972503648',6);
select * from alumnos; 
select * from cursos;

-- 1 selec todos los cursos facil o dificil
select * from cursos where dificultad in ("FACIL", "DIFICIL")  ; 
-- 2 selecc cursos q sean amarillo o celeste y q sean dificultad media 
select * from cursos where color in ("AMARILLO", "CELESTE")  and dificultad = "MEDIO" ;

select * from alumnos
inner join cursos on alumnos.curso_id = cursos.id 
where correo like "%gmail%"; 

INSERT INTO alumnos VALUES (DEFAULT, 'Jhonatan', 'Maicelo', 'Roman', 'jmaicelo@gmail.com', '925361048', NULL);

-- left join
select * from alumnos
left join cursos on alumnos.curso_id = cursos.id ;
-- right join
select * from alumnos
right join cursos on alumnos.curso_id = cursos.id ;
