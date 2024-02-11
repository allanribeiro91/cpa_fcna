from apps.formularios.models import RegistroFormularios, FormAvaliacaoDisciplinas

def run():
    # Apagar todos os registros
    FormAvaliacaoDisciplinas.objects.all().delete()
    RegistroFormularios.objects.all().delete()


#python manage.py runscript apps.formularios.scripts.apagar_dados