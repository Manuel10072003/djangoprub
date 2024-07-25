from rest_framework import serializers
#from .models import Curso
#from .models import Estudiante

class EstudianteSerializer(serializers.Serializer):
    nombres = serializers.CharField(max_length=60)
    apellidos = serializers.CharField(max_length=60)
    fecha_nacimiento = serializers.DateField()
    dni = serializers.CharField(max_length=8)
    anio = serializers.IntegerField()
    foto = serializers.ImageField()
    apoderado = serializers.CharField()
    seccion = serializers.IntegerField()
    relacion = serializers.CharField(max_length=40)

class ModificarEstudianteS(serializers.Serializer):
    nombres = serializers.CharField(max_length=60)
    apellidos = serializers.CharField(max_length=60)
    fecha_nacimiento = serializers.DateField()
    dni = serializers.CharField(max_length=8)
    anio = serializers.IntegerField()
    foto = serializers.ImageField()

class CursoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)

class SeccionSerializer(serializers.Serializer):
    designacion = serializers.CharField(max_length=30)

class DocenteSerializer(serializers.Serializer):
    Nombres = serializers.CharField(max_length=60)
    Apellidos = serializers.CharField(max_length=60)
    FechaNacimiento = serializers.DateField()
    DNI = serializers.CharField(max_length=8)
    NumeroCelular = serializers.CharField(max_length=9)
    Contrasenia = serializers.CharField(max_length=30)

class NotaSerializer(serializers.Serializer):
    idclase = serializers.CharField(max_length=5)
    idestudiante = serializers.CharField(max_length=10)
    tiponota = serializers.CharField(max_length=10)
    nota = serializers.IntegerField()

class ApoderadoSerializer(serializers.Serializer):
    nombres = serializers.CharField(max_length=60)
    apellidos = serializers.CharField(max_length=60)
    fechanacimiento = serializers.DateField()
    dni = serializers.CharField(max_length=8)
    numerocelular = serializers.CharField(max_length=9)

class ClaseSerializer(serializers.Serializer):
    idclase = serializers.CharField(max_length=5)
    idcurso = serializers.CharField(max_length=5)
    idseccion = serializers.IntegerField()
    iddocente = serializers.CharField(max_length=10)

class HoraSerializer(serializers.Serializer):
    idhora = serializers.CharField(max_length=14)
    idclase = serializers.CharField(max_length=5)
    diahorai = serializers.DateTimeField()
    diahoraf = serializers.DateTimeField()
