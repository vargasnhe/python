-- utilizando la base de datos colegio
-- crear la tabla de los padres de los alumnos
create table padres(
id int primary key auto_increment,
nombre varchar (200) not null,
ape_paterno varchar(50) not null,
ape_materno varchar(50) not null,
telefono varchar(10) not null
);

create table alumnos_padres(
id int primary key auto_increment,
padre_id int,
alumno_id int,
-- haciendo las releferecnias hacia las tablas respectivas
FOREIGN KEY(padre_id) REFERENCES padres(id), 
FOREIGN KEY(alumno_id) REFERENCES alumnos(id)

);
INSERT INTO padres VALUES (DEFAULT, 'Juan', 'Rodriguez', 'Cano', '925364155'),
                          (DEFAULT, 'Angel', 'Sanchez', 'Baldarrago', '936205489'),
                          (DEFAULT, 'Jimmy', 'Jara', 'Pomareda', '914253689'),
                          (DEFAULT, 'Juan', 'Barrientos', 'Romero', '936259568'),
                          (DEFAULT, 'Nohemi', 'Ayala', 'Romero', '929655748'),
                          (DEFAULT, 'Christian', 'Martinez', 'Martinez', '976859245');
INSERT INTO alumnos_padres VALUES   (DEFAULT, 1,3),
                                    (DEFAULT, 1,2),
                                    (DEFAULT, 2,1),
                                    (DEFAULT, 3,2),
                                    (DEFAULT, 5,6),
                                    (DEFAULT, 3,6),
                                    (DEFAULT, 4,6),
                                    (DEFAULT, 4,4),
                                    (DEFAULT, 6,5),
                                    (DEFAULT, 6,4);
-- 1 listar padres y sus alumnos_padres  inner join intersecion 
select * from padres  
inner join alumnos_padres on padres.id=alumnos_padres.padre_id; 
-- 2 listar alumnos y sus alumnos padres  22.4
-- ect * from alumnos  
 --   join alumnos_padres on alumnos_padres on alumnos.id=alumnos_padres.alumno_id;
SELECT * FROM alumnos  inner JOIN alumnos_padres ON alumnos.id =alumnos_padres.alumno_id;

SELECT * 
FROM alumnos 
    INNER JOIN alumnos_padres ON alumnos.id = alumnos_padres.alumno_id
    INNER JOIN padres ON alumnos_padres.padre_id = padres.id;
    -- agregar cursos
-- inner join cursos on alumnos.curso_id = cursos.id   https://dev.mysql.com/doc/refman/8.0/en/join.html https://www.w3schools.com/sql/sql_join_inner.asp
    
-- 1 de la clausula anterior solamente mostrar los resultado cuyo ape_paterno del padre sea rodriguez o jara 
select *
FROM alumnos 
    INNER JOIN alumnos_padres ON alumnos.id = alumnos_padres.alumno_id
    INNER JOIN padres ON alumnos_padres.padre_id = padres.id
where padres.ape_paterno in ("Rodriguez", "Jara");

