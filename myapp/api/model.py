from app import db

class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    datainclusao = db.Column(db.String)
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "datainclusao": self.datainclusao
        }


