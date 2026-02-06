from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from api.v1.auth_controller import LoginResourceV1
from api.v1.event_controller import EventListResourceV1, EventResourceV1, InscricaoResourceV1
from api.v1.report_controller import RelatorioEventoResourceV1

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "eventpass-secret"

api = Api(app)
JWTManager(app)

api.add_resource(LoginResourceV1, "/api/v1/login")
api.add_resource(EventListResourceV1, "/api/v1/eventos")
api.add_resource(EventResourceV1, "/api/v1/eventos/<int:evento_id>")
api.add_resource(InscricaoResourceV1, "/api/v1/eventos/<int:evento_id>/inscrever")
api.add_resource(RelatorioEventoResourceV1, "/api/v1/eventos/<int:evento_id>/relatorio")

if __name__ == "__main__":
    app.run(debug=True)
