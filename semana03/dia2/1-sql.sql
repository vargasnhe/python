-- esto es un comentario

-- sql lenguaje estructurado de consultas
-- dos lenguajes:
-- ddl data definition languaje es lenguaje de definicion de datos
-- create
CREATE database pruebas; 

show databases; 


use pruebas;

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
-- delete 


-- update tabla set columna "nuevo valor" where condicional

update alumnos set nombre = "marimar" where id = 29 ;
update alumnos set num_documento = 5454545, nombre ="rodrigo" where id =  30;

delete from alumnos where id >30 and id < 45;

INSERT INTO alumnos (nombre, sex, num_documento, fec_nacimiento) VALUES
                    ('Maria Alejandra', 'binario', '49596785', '1995-06-19');


-- 1 mostrar todos los alumnos que tengan todos alumnos q tengan ce
-- 2 mostrar alumnos sexo masculino o femenino
-- 3 mostros alumnos que nacieron antes del 1990 -01-01
select nombre, tipo_de_documento = "ce"  from alumnos; 
select nombre, sex = "masculino" or "femenino"  from alumnos; 
select nombre, fec_nacimiento < "1990-01-01"  from alumnos; 

select * from alumnos where tipo_de_documento = "ce";
select * from alumnos where sex in ("masculino", "femenino") ; 
select * from alumnos where fec_nacimiento < "1990-01-01";

select nombre from alumnos where nombre like "%a%";
select nombre from alumnos where nombre like "%a";

-- con la propiedad binary le indicamos que haga la comparación a nivel de binarios inclue la ñ y las tildes 

select nombre from alumnos where binary nombre like "%A%"; -- busca ese caracter
select nombre from alumnos where nombre like "%d%u%"; -- ddduuu du duuuu dd  uu 
select nombre from alumnos where nombre like "_o%"; -- segunda letra o
select nombre from alumnos where nombre like "E__%";

-- 4 mostrar alumnos cuyo nombre tenga letra n
  select nombre from alumnos where nombre like "%n%";    
-- 5 segundo digito del documento sea 8
select *from alumnos where num_documento like "_8%"; 
-- 6 sexo contenga la letra i seguido de una letra cualquiera y luego la letra 
select nombre from alumnos where sex like "%i_o%"; 

                 
			

		

    
    
    


