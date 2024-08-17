from app import db
class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text,nullable=False)

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
             "description":self.description
        }