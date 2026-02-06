from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token

class LoginResourceV1(Resource):
    def post(self):
        d = request.json
        if d["email"] == "admin@eventpass.com" and d["senha"] == "123456":
            token = create_access_token(identity=d["email"])
            return {"access_token": token}
        return {"erro": "Credenciais inválidas"}, 401
