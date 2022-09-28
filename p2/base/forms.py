from django.forms import ModelForm
from .models import Curso, Estudiante, Prueba, Preguntas, EstudiantePreguntas, Tema

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ('curso','nombres','apellidos','nombre_completo',)    

class EstudiantePreguntasForm(ModelForm):
    class Meta:
        model = EstudiantePreguntas
        fields = '__all__'        

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args,**kwargs)
        if user:
            self.fields['preguntas'].queryset = Preguntas.objects.filter(user=user)    
  

class PruebaForm(ModelForm):
    class Meta:
        model = Prueba
        fields = ('nombre_prueba',)

class PreguntasForm(ModelForm):

    class Meta:
        model = Preguntas
        fields = ('prueba', 'tema', 'pregunta',)

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args,**kwargs)
        if user:
            self.fields['prueba'].queryset = Prueba.objects.filter(user=user)    

class UPreguntasForm(ModelForm):

    class Meta:
        model = Preguntas
        fields = ('pregunta',)

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args,**kwargs)
        if user:
            self.fields['prueba'].queryset = Prueba.objects.filter(user=user)  

class TemaForm(ModelForm):
    class Meta:
        model = Tema
        fields = '__all__'
