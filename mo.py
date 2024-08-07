# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Apoderado(models.Model):
    idapoderado = models.CharField(db_column='IdApoderado', primary_key=True, max_length=10, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento')  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=8, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    numerocelular = models.CharField(db_column='NumeroCelular', max_length=9, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Apoderado'


class Asistenciacolegio(models.Model):
    idasistencia = models.ForeignKey('Diario', models.DO_NOTHING, db_column='IdAsistencia')  # Field name made lowercase.
    idestudiante = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='IdEstudiante')  # Field name made lowercase.
    asistencia = models.IntegerField(db_column='Asistencia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AsistenciaColegio'


class Asistenciacurso(models.Model):
    idhora = models.ForeignKey('Hora', models.DO_NOTHING, db_column='IdHora')  # Field name made lowercase.
    idestudiante = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='IdEstudiante')  # Field name made lowercase.
    asistencia = models.IntegerField(db_column='Asistencia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AsistenciaCurso'


class Clase(models.Model):
    idclase = models.CharField(db_column='IdClase', primary_key=True, max_length=5, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    idcurso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    idseccion = models.ForeignKey('Seccion', models.DO_NOTHING, db_column='IdSeccion')  # Field name made lowercase.
    iddocente = models.ForeignKey('Docente', models.DO_NOTHING, db_column='IdDocente')  # Field name made lowercase.
    auxiliar = models.CharField(db_column='Auxiliar', max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clase'


class Curso(models.Model):
    idcurso = models.CharField(db_column='IdCurso', primary_key=True, max_length=5, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=40, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curso'


class Diario(models.Model):
    idasistencia = models.CharField(db_column='IdAsistencia', primary_key=True, max_length=8, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    dia = models.DateField(db_column='Dia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Diario'


class Docente(models.Model):
    iddocente = models.CharField(db_column='IdDocente', primary_key=True, max_length=10, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento')  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=8, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    numerocelular = models.CharField(db_column='NumeroCelular', max_length=9, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Docente'


class Estudiante(models.Model):
    idestudiante = models.CharField(db_column='IdEstudiante', primary_key=True, max_length=10, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento')  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=8, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    anioescolar = models.IntegerField(db_column='AnioEscolar')  # Field name made lowercase.
    imagen = models.BinaryField(db_column='Imagen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estudiante'


class Hora(models.Model):
    idhora = models.CharField(db_column='IdHora', primary_key=True, max_length=14, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    idclase = models.ForeignKey(Clase, models.DO_NOTHING, db_column='IdClase')  # Field name made lowercase.
    diahorai = models.DateTimeField(db_column='DiaHoraI')  # Field name made lowercase.
    diahoraf = models.DateTimeField(db_column='DiaHoraF')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hora'


class Lista(models.Model):
    idestudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='IdEstudiante')  # Field name made lowercase.
    idseccion = models.ForeignKey('Seccion', models.DO_NOTHING, db_column='IdSeccion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lista'


class Notas(models.Model):
    idclase = models.ForeignKey(Clase, models.DO_NOTHING, db_column='IdClase')  # Field name made lowercase.
    idestudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='IdEstudiante')  # Field name made lowercase.
    tiponota = models.CharField(db_column='TipoNota', max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nota = models.IntegerField(db_column='Nota', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notas'


class Relacion(models.Model):
    idestudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='IdEstudiante')  # Field name made lowercase.
    idapoderado = models.ForeignKey(Apoderado, models.DO_NOTHING, db_column='IdApoderado')  # Field name made lowercase.
    relacion = models.CharField(db_column='Relaci¾n', max_length=30, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Relacion'


class Seccion(models.Model):
    idseccion = models.IntegerField(db_column='IdSeccion', primary_key=True)  # Field name made lowercase.
    designacion = models.CharField(db_column='Designacion', max_length=30, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seccion'


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='IdUsuario', primary_key=True)  # Field name made lowercase.
    nomusuario = models.CharField(db_column='NomUsuario', max_length=10, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    contrasenia = models.CharField(db_column='Contrasenia', max_length=30, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    tipousuario = models.IntegerField(db_column='TipoUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Modern_Spanish_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Modern_Spanish_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    model = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Modern_Spanish_CI_AS')
    session_data = models.TextField(db_collation='Modern_Spanish_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
