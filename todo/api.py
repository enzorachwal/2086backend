
from todo.models import Duvida,Comorbidade,Paciente,Medico,Consulta,Exame  
from rest_framework import routers, serializers, viewsets, mixins 

# Serializers define the API representation.
class DuvidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duvida
        fields = ['pergunta', 'resposta']

# ViewSets define the view behavior.
class DuvidaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Duvida.objects.all()
    serializer_class = DuvidaSerializer

# Serializers define the API representation.
class ComorbidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comorbidade
        fields = ['descricao']

# ViewSets define the view behavior.
class ComorbidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comorbidade.objects.all()
    serializer_class = ComorbidadeSerializer 

 # Serializers define the API representation.
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nome',"sangue", 'idade', 'cpf', 'rg','email', 'condicoesMedicas', 'comorbidades']

# ViewSets define the view behavior.
class PacienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer       
 

 # Serializers define the API representation.
class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'especialidade']

# ViewSets define the view behavior.
class MedicoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer   

 # Serializers define the API representation.
class ConsultaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    class Meta:
        model = Consulta
        fields = ['data', 'hora', 'local','medico', 'requerimentoExame', 'diagnosticoMedico']

# ViewSets define the view behavior.
class ConsultaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer  


class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exame
        fields = ['descricao', 'arquivo', 'data']

# ViewSets define the view behavior.
class ExameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer 



class CreatePacienteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = PacienteSerializer 
  queryset = Paciente.objects.all()  

class CreateMedicoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = MedicoSerializer 
  queryset = Medico.objects.all()         

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'duvidas', DuvidaViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'create-paciente', CreatePacienteViewSet)
router.register(r'create-medico', CreateMedicoViewSet)