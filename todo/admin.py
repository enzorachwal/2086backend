from django.contrib import admin
from .models import Duvida,Comorbidade,Paciente,Medico,Consulta,Exame,Contato

admin.site.register(Comorbidade)
admin.site.register(Duvida)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)
admin.site.register(Exame)
admin.site.register(Contato)


# Register your models here.
