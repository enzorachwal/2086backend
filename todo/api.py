from rest_framework import routers, serializers, viewsets, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.permissions import IsAuthenticated



#from django.contrib.auth import authenticate, user_logged_in
from django.contrib.auth import authenticate, login, logout
from todo.models import Duvida,Comorbidade,Paciente,Medico,Consulta,Exame,Contato  


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

 # Serializers define the API representation.
class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

# ViewSets define the view behavior.
class ContatoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer 

class CreatePacienteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = PacienteSerializer 
  queryset = Paciente.objects.all()  

class CreateMedicoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = MedicoSerializer 
  queryset = Medico.objects.all() 

class CreateContatoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = ContatoSerializer 
  queryset = Contato.objects.all()           


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'password',
        ]

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance

class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = UserRegistrationSerializer  


class LoginViewSet(ViewSet):
  @staticmethod
  def create(request: Request) -> Response:
      user = authenticate(
          username=request.data.get('username'),
          password=request.data.get('password'))

      if user is not None:
        login(request, user)
        return JsonResponse({"id": user.id, "username": user.username})
      else:
        return JsonResponse(
            {"detail": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'password',
        ]

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance

class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = UserRegistrationSerializer  


class LoginViewSet(ViewSet):
  @staticmethod
  def create(request: Request) -> Response:
      user = authenticate(
          username=request.data.get('username'),
          password=request.data.get('password'))

      if user is not None:
        login(request, user)
        return JsonResponse({"id": user.id, "username": user.username})
      else:
        return JsonResponse(
            {"detail": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

# Serializers define the API representation.
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model =Paciente
        fields = ['id', 'nome', 'email', 'telefone', 'cidade', 'user']

class UsuarioDetailsViewSet(ViewSet):
  serializer_class = UsuarioSerializer
  permission_classes = [IsAuthenticated]
  @staticmethod
  def list(request: Request) -> Response:
    usuario = Paciente.objects.filter(user = request.user)[0]
    serializer = UsuarioSerializer(usuario, many=False)
    return Response(serializer.data)


class UserDetailsSerializer(serializers.ModelSerializer):
  class Meta:
      model = get_user_model()
      fields = ('id', 'username')

class UserDetailsViewSet(ViewSet):
  serializer_class = UserDetailsSerializer
  permission_classes = [IsAuthenticated]
  @staticmethod
  def list(request: Request) -> Response:
    serializer = UserDetailsSerializer(request.user, many=False)
    return Response(serializer.data)


class LogoutViewSet(ViewSet):
  permission_classes = [IsAuthenticated]
  @staticmethod
  def list(request: Request) -> Response:
    logout(request)
    content = {'logout': 1}
    return Response(content)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'duvidas', DuvidaViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'create-paciente', CreatePacienteViewSet)
router.register(r'create-medico', CreateMedicoViewSet)
router.register(r'create-contato', CreateContatoViewSet)
router.register(r'currentuser', UserDetailsViewSet, basename="Currentuser")
router.register(r'currentusuario', UsuarioDetailsViewSet, basename="Currentusuario")

router.register(r'login', LoginViewSet, basename="Login")
router.register(r'logout', LogoutViewSet, basename="Logout")
router.register(r'user-registration', UserRegistrationViewSet, basename="User")
