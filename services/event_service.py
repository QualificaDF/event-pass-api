from repositories.event_repository import *
from utils.validators import email_valido

def register_participant(nome, email, evento_id):
    if not email_valido(email):
        return False, "Email inválido"

    cap = get_event_capacity(evento_id)
    if cap is None:
        return False, "Evento não encontrado"

    if count_participants(evento_id) >= cap:
        return False, "Evento lotado"

    add_participant(nome, email, evento_id)
    return True, "Inscrição realizada com sucesso"
