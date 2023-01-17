create database PAI_BD;
use PAI_BD;
/*Iago Morales Camacho*/
create table Clientes(
id int not null primary key,
email varchar(50) not null unique,
nombre varchar(20) not null,
usuario varchar(20) not null unique,
contraseña varchar(20) not null,
telefono integer unique,
descripcion varchar(500) ,
fotoPerfil varchar(500),
token varchar(20) unique
);

create table Agencia(
id int not null primary key unique,
email varchar(50) not null unique,
nombre varchar(20) not null unique,
contraseña varchar(20) not null,
telefono integer  not null unique,
ciudad varchar(30) not null ,
descripcion varchar(500) ,
twitter varchar(500),
instagram  varchar(500),
tiktok varchar(500),
fotoPerfil varchar(100),
token varchar(20) unique
);


/*Aarón Saavedra Lagares */
create table Fotografo(
id int not null auto_increment primary key unique,
email varchar(50) not null unique,
nombre varchar(20) not null,
apellido varchar(50) null,
contraseña varchar(20) not null,
telefono int not null unique,
ciudad varchar(30) not null,
descripcion varchar(500) ,
tiktok varchar(500) ,
twitter varchar(500) ,
instagram varchar(500) ,
fotoPerfil varchar(100) ,
token varchar(20) unique
);

create table ComentarioFotografo(
id varchar(10) not null  primary key ,
idUsuario int not null unique,
idFotografo int not null unique,
comentario varchar(500) not null,
valoracion int not null
);

/*Prasamsa Castelao López*/
CREATE TABLE FotosFotografo(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY unique,
	idFotografo INT NOT NULL unique,
	foto varchar(100) 

);

CREATE TABLE ComentarioAgencia(
	id varchar(10) NOT NULL  PRIMARY KEY unique,
	idUsuario  int  NOT NULL unique,
	idAgencia  int  NOT NULL unique,
	comentario VARCHAR(500) NOT NULL,
	valoracion INT NOT NULL,
	foto VARCHAR(100) 

);

CREATE TABLE FotosAgencia(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY unique,
	idAgencia INT NOT NULL unique,
	foto VARCHAR(100) 

);

ALTER TABLE ComentarioFotografo ADD FOREIGN KEY(idUsuario) REFERENCES Clientes(id);
ALTER TABLE ComentarioFotografo ADD FOREIGN KEY(idFotografo) REFERENCES Fotografo(id);

ALTER TABLE ComentarioAgencia ADD FOREIGN KEY(idUsuario) REFERENCES Clientes(id);
ALTER TABLE ComentarioAgencia ADD FOREIGN KEY(idAgencia) REFERENCES Agencia(id);

ALTER TABLE FotosAgencia ADD FOREIGN KEY(idAgencia) REFERENCES Agencia(id);
ALTER TABLE FotosFotografo ADD FOREIGN KEY(idFotografo) REFERENCES Fotografo(id);
