-- esto es un comentario

-- sql lenguaje estructurado de consultas
-- dos lenguajes:
-- ddl data definition languaje es lenguaje de definicion de datos
-- create
CREATE database pruebas1; 

show databases; 


use pruebas1;

-- las tablas siempre deben ser en plural
create table alumnos(
-- ahora definimos las columnas
-- nombre_colm tipo_dato [ parametros opcionales]
	id int primary key auto_increment,
	nombre varchar(50) not null,
-- es un tipo de fato que permite guardar determinados valores
	sex enum("femenino", "masculino", "binario", "otro", "helicoptero"),
-- agregar documento(dni,ce, pasaporte)
	tipo_de_documento enum ("dni","ce","pasaporte") default "dni",
    num_documento varchar(10) not null,
    fec_nacimiento datetime 
    );
show tables ; 

-- Dml data manipulation language lenguaje de manipulación de datos
-- select [columnas] from tabla
select nombre, sex from alumnos; 
SELECT 
    *
FROM
    alumnos;

INSERT INTO alumnos (nombre, sex, num_documento, fec_nacimiento) VALUES
                    ('Eduardo', 'MASCULINO', '73500746', '1992-08-01');
INSERT INTO alumnos (nombre, sex, num_documento, fec_nacimiento) VALUES
                    ('Ronald', 'binario', '75268256', '1995-07-25'),
                    ('Karim', 'femenino', '85234716', '1991-01-15'),
                    ('Alexa', 'helicoptero', '14729583', '1995-06-08');
INSERT INTO alumnos VALUES 
                    (DEFAULT, 'Romina', 'femenino', 'ce', '456789132', '1987-05-14'),
                    (DEFAULT, 'Roberto', 'binario', 'pasaporte', '15946789', '1985-01-01'),
                    (DEFAULT, 'Jair', 'masculino', "dni", '34598746', '1995-04-09');
                    
                    
