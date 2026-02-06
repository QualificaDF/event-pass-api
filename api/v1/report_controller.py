from flask_restful import Resource
from repositories.event_repository import count_participants, get_event

class RelatorioEventoResourceV1(Resource):
    def get(self, evento_id):
        e = get_event(evento_id)
        if not e:
            return {"erro": "Evento não encontrado"}, 404
        total = count_participants(evento_id)
        return {
            "evento": e["nome"],
            "participantes": total
        }
