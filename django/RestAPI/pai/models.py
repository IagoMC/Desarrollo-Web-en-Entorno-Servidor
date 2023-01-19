# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agencia(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=50)
    nombre = models.CharField(unique=True, max_length=20)
    contraseña = models.CharField(max_length=20)
    telefono = models.IntegerField(unique=True)
    ciudad = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    twitter = models.CharField(max_length=500, blank=True, null=True)
    instagram = models.CharField(max_length=500, blank=True, null=True)
    tiktok = models.CharField(max_length=500, blank=True, null=True)
    fotoperfil = models.CharField(db_column='fotoPerfil', max_length=100, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Agencia'


class Clientes(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=50)
    nombre = models.CharField(max_length=20)
    usuario = models.CharField(unique=True, max_length=20)
    contraseña = models.CharField(max_length=20)
    telefono = models.IntegerField(unique=True, blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    fotoperfil = models.CharField(db_column='fotoPerfil', max_length=500, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clientes'


class Comentarioagencia(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    idusuario = models.OneToOneField(Clientes, models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    idagencia = models.OneToOneField(Agencia, models.DO_NOTHING, db_column='idAgencia')  # Field name made lowercase.
    comentario = models.CharField(max_length=500)
    valoracion = models.IntegerField()
    foto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ComentarioAgencia'


class Comentariofotografo(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    idusuario = models.OneToOneField(Clientes, models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    idfotografo = models.OneToOneField('Fotografo', models.DO_NOTHING, db_column='idFotografo')  # Field name made lowercase.
    comentario = models.CharField(max_length=500)
    valoracion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ComentarioFotografo'


class Fotografo(models.Model):
    email = models.CharField(unique=True, max_length=50)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    contraseña = models.CharField(max_length=20)
    telefono = models.IntegerField(unique=True)
    ciudad = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    tiktok = models.CharField(max_length=500, blank=True, null=True)
    twitter = models.CharField(max_length=500, blank=True, null=True)
    instagram = models.CharField(max_length=500, blank=True, null=True)
    fotoperfil = models.CharField(db_column='fotoPerfil', max_length=100, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fotografo'


class Fotosagencia(models.Model):
    idagencia = models.OneToOneField(Agencia, models.DO_NOTHING, db_column='idAgencia')  # Field name made lowercase.
    foto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FotosAgencia'


class Fotosfotografo(models.Model):
    idfotografo = models.OneToOneField(Fotografo, models.DO_NOTHING, db_column='idFotografo')  # Field name made lowercase.
    foto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FotosFotografo'
