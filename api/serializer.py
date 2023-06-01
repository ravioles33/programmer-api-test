from rest_framework import serializers
from .models import Programmer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Programmer
        #fields=('fullname','nickname') #Indicando los campos individualmente
        fields = '__all__' #todos los campos
