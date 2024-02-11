from django.shortcuts import render
from apps.usuarios.models import Usuarios
from django.http import JsonResponse
from datetime import datetime

def verificar_usuario(request, cpf, data_nascimento):
    # Convertendo a string de data para um objeto date
    data_nascimento_obj = datetime.strptime(data_nascimento, '%Y-%m-%d').date()

    try:
        usuario = Usuarios.objects.get(cpf=cpf, data_nascimento=data_nascimento_obj)
        dados = {
            'verificacao': True,
            'usuario_uuid': usuario.uuid,
        }
    except Usuarios.DoesNotExist:
        # Se o usuário não for encontrado, retorna False
        dados = {
            'verificacao': False,
            'usuario_uuid': None,
        }
    # Retorna True se o usuário existir, False caso contrário
    return JsonResponse(dados, safe=False)




