from ariadne import convert_kwargs_to_snake_case

from api.model import Disciplina

def listDisciplinas_resolver(obj, info):
    try:
        disciplinas = [disciplina.to_dict() for disciplina in Disciplina.query.all()]
        print(disciplinas)
        payload = {
            "success": True,
            "disciplinas": disciplinas
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload



@convert_kwargs_to_snake_case
def getDisciplina_resolver(obj, info, id):
    try:
        disciplina = Disciplina.query.get(id)
        payload = {
            "success": True,
            "disciplina": disciplina.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo item matching id {id} not found"]
        }

    return payload
