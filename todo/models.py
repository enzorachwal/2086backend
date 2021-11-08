from django.db import models

# Create your models here.
class TodoItem(models.Model):
  content = models.TextField()

class Duvida(models.Model):
  pergunta = models.TextField("Pergunta")
  resposta = models.TextField("Resposta")
  def __str__(self):
      return str(self.pergunta)
  class Meta:
      verbose_name = "Dúvida frequente"
      verbose_name_plural = "Dúvidas frequentes" 

class Comorbidade(models.Model):
  descricao = models.CharField("Descrição",max_length=100)
  def __str__(self):
      return str(self.descricao)
  class Meta:
      verbose_name = "Comorbidade"
      verbose_name_plural = "Comorbidades"

class Paciente(models.Model):
  nome = models.CharField("Nome",max_length=100)
  sangue = models.CharField("Tipo Sanguíneo",max_length=3, null=True)
  cpf = models.CharField("CPF",max_length=20)
  idade = models.IntegerField("Idade")
  rg = models.CharField("RG",max_length=20)
  email = models.CharField("Email",max_length=20, null=True) 
  condicoesMedicas = models.TextField("Condições Médicas")
  comorbidades = models.ManyToManyField("Comorbidade", verbose_name="Comorbidades", blank=True)
    
  def __str__(self):
      return str(self.nome)
  class Meta:
      verbose_name = "Paciente"
      verbose_name_plural = "Pacientes"  

class Consulta(models.Model):
  data = models.DateField("Data")
  hora = models.TimeField('Hora', null=True)
  local = models.CharField("Local",max_length=100)
  medico = models.ForeignKey('Medico', on_delete=models.PROTECT, verbose_name="Médico", null= True)
  diagnosticoMedico = models.TextField("Diagnóstico do Médico")
  requerimentoExame =  models.FileField(upload_to='static/requerimentos', null=True, max_length=255 )
    
  def __str__(self):
      return str(self.data)
  class Meta:
      verbose_name = "Consulta"
      verbose_name_plural = "Consultas"   

class Medico(models.Model):
  crm = models.CharField("CRM",max_length=20)
  nome = models.CharField("Nome",max_length=100)
  especialidade = models.TextField("Especialidade do Profissional")
   
  def __str__(self):
      return str(self.nome)
  class Meta:
      verbose_name = "Médico"
      verbose_name_plural = "Médicos"      

class Exame(models.Model):
  descricao = models.CharField("Descrição",max_length=100)
  arquivo = models.FileField(upload_to='static/exames', null=True, max_length=255 )
  data = models.DateField("Data")
   
  def __str__(self):
      return str(self.descricao)
  class Meta:
      verbose_name = "Exame"
      verbose_name_plural = "Exames"    

class Hospital(models.Model):
  nome = models.CharField("Nome", max_length=255)
  endereco = models.CharField("Endereço", max_length=255)

  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Hospital"
      verbose_name_plural = "Hospitais"      