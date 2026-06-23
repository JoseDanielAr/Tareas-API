from datetime import datetime, timezone
from database import db

class Task(db.Model):
    __tablename__ = "tasks"

    id         = db.Column(db.Integer, primary_key=True)
    titulo     = db.Column(db.String(200), nullable=False)
    completada = db.Column(db.Boolean, default=False, nullable=False)
    creada_en  = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            "id":         self.id,
            "titulo":     self.titulo,
            "completada": self.completada,
            "creada_en":  self.creada_en.isoformat(),
        }