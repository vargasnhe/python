-- crear database llamada colegio
create database colegio;

-- utilizar
Use colegio; 

-- en la bd necesitamos almecenar los alumnos con la siguiente info: ID pk entero autoincrementable, nombre string hasta 100 caracteresm ape_pater string
-- apell materno strin hgasta 50 caracter, correo no se puede repetir va ser texto, num_emergencia string hasta 10 caract

create table alumnos(
	id int primary key auto_increment,
	nombre varchar(100) not null,
    ape_paterno varchar(50) not null ,
    ape_materno varchar(50) not null,
    correo  text unique ,
    num_emergencia varchar(10)

    );
    


