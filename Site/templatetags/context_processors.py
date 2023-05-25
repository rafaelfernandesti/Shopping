from Site.models import Departamento

def departamentos(request):
    return {'departamentos': Departamento.objects.all()}
