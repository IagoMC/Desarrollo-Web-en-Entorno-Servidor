create database PAI_BD;
use PAI_BD;
/*Iago Morales Camacho*/
create table Clientes(
id int not null primary key,
email varchar(50) not null unique,
nombre varchar(20) not null,
usuario varchar(20) not null unique,
contrasena varchar(20) not null,
telefono integer unique,
descripcion varchar(500) ,
fotoPerfil varchar(500),
token varchar(20) unique
);

create table Agencia(
id int not null primary key unique,
email varchar(50) not null unique,
nombre varchar(20) not null unique,
contrasena varchar(20) not null,
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
contrasena varchar(20) not null,
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
id varchar(10) not null  primary key unique,
idUsuario int not null ,
idFotografo int not null ,
comentario varchar(500) not null,
valoracion int not null
);

/*Prasamsa Castelao López*/
CREATE TABLE FotosFotografo(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY unique,
	idFotografo INT NOT NULL ,
	foto varchar(100) 

);

CREATE TABLE ComentarioAgencia(
	id varchar(10) NOT NULL  PRIMARY KEY unique,
	idUsuario  int  NOT NULL ,
	idAgencia  int  NOT NULL ,
	comentario VARCHAR(500) NOT NULL,
	valoracion INT NOT NULL,
	foto VARCHAR(100) 

);

CREATE TABLE FotosAgencia(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY unique,
	idAgencia INT NOT NULL ,
	foto VARCHAR(100) 

);

ALTER TABLE ComentarioFotografo ADD FOREIGN KEY(idUsuario) REFERENCES Clientes(id);
ALTER TABLE ComentarioFotografo ADD FOREIGN KEY(idFotografo) REFERENCES Fotografo(id);

ALTER TABLE ComentarioAgencia ADD FOREIGN KEY(idUsuario) REFERENCES Clientes(id);
ALTER TABLE ComentarioAgencia ADD FOREIGN KEY(idAgencia) REFERENCES Agencia(id);

ALTER TABLE FotosAgencia ADD FOREIGN KEY(idAgencia) REFERENCES Agencia(id);
ALTER TABLE FotosFotografo ADD FOREIGN KEY(idFotografo) REFERENCES Fotografo(id);



insert into Agencia values (1,"imc@gmacil.com","AgenciaIago","1234","717712246","Barcelona","Agencia de fotografía, especializada en capturar momentos especiales y convertirlos en recuerdos inolvidables.","https://twitter.com/","https://www.instagram.com/","https://www.tiktok.com/es/","E:\fotosperfil_agencia\AgenciaIago.png","ABC123");
insert into Agencia values (2,"agenci@gmacil.com","Agenci","1234","798709663","Madrid","Agencia de fotografía con un enfoque en la creatividad y la calidad. Nos esforzamos por capturar la esencia de cada momento único y convertirlo en una obra de arte.","https://twitter.com/","https://www.instagram.com/","https://www.tiktok.com/es/","E:\fotosperfil_agencia\Agenci.png","ABC129");
insert into Agencia values (3,"fm@gmacil.com","FotoMomento","1235","981234569","Barcelona","Agencia de fotografía con un enfoque en el cliente. Entendemos que cada cliente es único y por eso nos esforzamos por conocer sus necesidades y deseos para crear experiencias de fotografía personalizadas e inolvidables. Ofrecemos una amplia gama de servicios de fotografía, incluyendo bodas, eventos, retratos y más, y nos aseguramos de utilizar solo equipos de alta calidad y técnicas innovadoras.","https://twitter.com/","https://www.instagram.com/","https://www.tiktok.com/es/","E:\fotosperfil_agencia\FotoMomento.png","ABC125");
insert into Agencia values (4,"agemaria@gmacil.com","AgenciaMaria","1238","981089273","A Coruña","Agencia de fotografía que se enfoca en capturar los momentos más significativos de la vida y transformarlos en historias visuales únicas. Ofrecemos una amplia gama de servicios de fotografía, incluyendo bodas, eventos, retratos y más, y nos esforzamos por ofrecer una experiencia de fotografía personalizada y memorable para cada uno de nuestros clientes.","https://twitter.com/","https://www.instagram.com/","https://www.tiktok.com/es/","E:\fotosperfil_agencia\AgenciaMaria.png","ABC127");
insert into Agencia values (5,"capturado@gmacil.com","Capturado","1223","981123476","Madrid","Agencia de fotografía dedicada a capturar momentos únicos y convertirlos en historias visuales que durarán para siempre. Ofrecemos una amplia variedad de servicios de fotografía, incluyendo bodas, eventos, retratos y más, y nos enfocamos en brindar una experiencia personalizada y profesional para cada uno de nuestros clientes.","https://twitter.com/","https://www.instagram.com/","https://www.tiktok.com/es/","E:\fotosperfil_agencia\Capturado.png","ABC987");

insert into Clientes values (6,"aronn@gmail.com","Aaron","Aaron03","12345","654987456","Buen chaval","E:\fotosperfil_cliente\Aaron.png","ab2123");
insert into Clientes values (7,"pepee@gmail.com","Pepe","Pepe86","12346","651236543","BuSco un fotografo progfesional para una sesion de fotos para una boda","E:\fotosperfil_cliente\Pepe.png","abb129");
insert into Clientes values (8,"zanaz@gmail.com","Ana","zANAZ","14545","654909056","Solo quiero ver fotos bonitas, como tu bb","E:\fotosperfil_cliente\ana.png","acb123");
insert into Clientes values (9,"maria@gmail.com","Maria","Maria_00","22345","654568456","Busco una agencia para un bautizo","E:\fotosperfil_cliente\maria.png","ab1123");
insert into Clientes values (10,"maxi@gmail.com","Maxi","Maaxiix","12985","698494356","Holaa, busco un fotografo para realizar una sesion de fotos pensado para mis redes sociales ","E:\fotosperfil_cliente\maxi.png","ccc123");






INSERT INTO Fotografo (id ,email ,nombre ,apellido ,contrasena ,telefono ,ciudad ,descripcion ,tiktok ,twitter ,instagram ,fotoPerfil ,token) values (26, "pepeee@gmail.com", "Pepe", "Pérez", "1234", "609120384", "A Coruña", "Soy fotografo profesional", "https://www.tiktok.com/es/","https://twitter.com/","https://www.instagram.com/", "E:\fotosagencia\f6.png","pol654" );
INSERT INTO Fotografo (id ,email ,nombre ,apellido ,contrasena ,telefono ,ciudad ,descripcion ,tiktok ,twitter ,instagram ,fotoPerfil ,token) values (27, "mari@gmail.com", "María", "Costa", "1234", "609118999", "A Coruña", "Soy fotografa inesperta y querría mejorar pero tengo experiencia en este mundo", "https://www.tiktok.com/es/","https://twitter.com/","https://www.instagram.com/", "E:\fotosagencia\f7.png","CCB143" );
INSERT INTO Fotografo (id ,email ,nombre ,apellido ,contrasena ,telefono ,ciudad ,descripcion ,tiktok ,twitter ,instagram ,fotoPerfil ,token) values (28, "josito@gmail.com", "Jose", "Miguel", "1234", "672728384", "A Coruña", "Tengo ganas de aprender y evolucionar junto a tí", "https://www.tiktok.com/es/","https://twitter.com/","https://www.instagram.com/", "E:\fotosagencia\f9.png","AC2223" );
INSERT INTO Fotografo (id ,email ,nombre ,apellido ,contrasena ,telefono ,ciudad ,descripcion ,tiktok ,twitter ,instagram ,fotoPerfil ,token) values (29, "meto@gmail.com", "Mateo", "Rodríguez", "1234", "600128555", "A Coruña", "Soy fotografo experimentado que garantiza un servicio impecable", "https://www.tiktok.com/es/","https://twitter.com/","https://www.instagram.com/", "E:\fotosagencia\f8.png","ACBD21" );
INSERT INTO Fotografo (id ,email ,nombre ,apellido ,contrasena ,telefono ,ciudad ,descripcion ,tiktok ,twitter ,instagram ,fotoPerfil ,token) values (30, "pnuria123@gmail.com", "Nuria", "Ferraz", "1234", "609148384", "A Coruña", "Soy fotografa profesional con ganas de mostrar mi talento al mundo", "https://www.tiktok.com/es/","https://twitter.com/","https://www.instagram.com/", "E:\fotosagencia\f10.png","ACB926" );

INSERT INTO ComentarioFotografo(id, idUsuario, idFotografo, comentario, valoracion) values (31, 6, 26, "Un servicio excelente", 4);
INSERT INTO ComentarioFotografo(id, idUsuario, idFotografo, comentario, valoracion) values (32, 7, 30, "Un servicio pesimo, no lo recomiendo", 1);
INSERT INTO ComentarioFotografo(id, idUsuario, idFotografo, comentario, valoracion) values (33, 9, 27, "La verdad es que es una persona que se preocupa por hacer las cosas bien, lo recomiendo", 5);
INSERT INTO ComentarioFotografo(id, idUsuario, idFotografo, comentario, valoracion) values (34, 9, 28, "Un servicio impecable, pese a la falta de recursos repètiría seguro", 4);
INSERT INTO ComentarioFotografo(id, idUsuario, idFotografo, comentario, valoracion) values (35, 8, 29, "Le contacte y no me respondio", 1);


insert into ComentarioAgencia values ("11","6","1","Bueno",5,"E:\fotosagencia\f1.png");
insert into ComentarioAgencia values (12,7,2,"Mal servicio",1,"E:\fotosagencia\f2.png");
insert into ComentarioAgencia values (13,8,2,"Muy malo",0,"E:\fotosagencia\f3.png");
insert into ComentarioAgencia values (14,9,3,"Muy bueno",5,"E:\fotosagencia\f4.png");
insert into ComentarioAgencia values (15,9,4,"Bueno",3,"E:\fotosagencia\f5.png");


INSERT INTO FotosFotografo (id, idFotografo, foto)VALUES 
  (21, 30, 'E:\fotosfotografo\f1.png'),
  (22, 26, 'E:\fotosfotografo\f2.png'),
  (23, 27, 'E:\fotosfotografo\f3.png'),
  (24, 28, 'E:\fotosfotografo\f4.png'),
  (25, 29, 'E:\fotosfotografo\f5.png');

INSERT INTO FotosAgencia (id, idAgencia, foto)VALUES 
  (16, 1, "E:\fotosagencia\f1.png"),
  (17, 2, 'E:\fotosagencia\f2.png'),
  (18, 3, 'E:\fotosagencia\f3.png'),
  (19, 4, 'E:\fotosagencia\f4.png'),
  (20, 5, 'E:\fotosagencia\f5.png');

