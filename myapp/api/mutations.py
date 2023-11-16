from datetime import date

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.model import Disciplina


@convert_kwargs_to_snake_case
def create_disciplina_resolver(obj, info, nome, datainclusao):
    try:
        today = date.today()
        disciplina = Disciplina(
            nome=nome, datainclusao=datainclusao
        )
        db.session.add(disciplina)
        db.session.commit()
        payload = {
            "success": True,
            "discplina": disciplina.to_dict()
        }
    except ValueError:  
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload

@convert_kwargs_to_snake_case
def update_disciplina_resolver(obj, info, id, nome, datainclusao):
    try:
        disciplina = Disciplina.query.get(id)
        if disciplina:
            disciplina.nome = nome
            disciplina.datainclusao = datainclusao
        db.session.add(disciplina)
        db.session.commit()
        payload = {
            "success": True,
            "disciplina": disciplina.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }

    return payload

@convert_kwargs_to_snake_case
def delete_disciplina_resolver(obj, info, id):
    try:
        disciplina = Disciplina.query.get(id)
        db.session.delete(disciplina)
        db.session.commit()
        payload = {"success": True, "post": disciplina.to_dict()}

    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }

    return payload