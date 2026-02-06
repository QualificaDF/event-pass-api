from flask_restful import Resource
from flask import request
from repositories.event_repository import *
from services.event_service import register_participant
from utils.jwt_utils import auth_required

class EventListResourceV1(Resource):
    @auth_required
    def get(self):
        return get_events(), 200

    @auth_required
    def post(self):
        d = request.json
        create_event(d["nome"], d["data"], d["capacidade"], d["local"])
        return {"msg": "Evento criado"}, 201

class EventResourceV1(Resource):
    @auth_required
    def get(self, evento_id):
        e = get_event(evento_id)
        return (e, 200) if e else ({"erro": "Não encontrado"}, 404)

    @auth_required
    def delete(self, evento_id):
        delete_event(evento_id)
        return {"msg": "Evento removido"}, 200

class InscricaoResourceV1(Resource):
    def post(self, evento_id):
        d = request.json
        ok, msg = register_participant(d["nome"], d["email"], evento_id)
        return {"msg": msg}, 201 if ok else 400
