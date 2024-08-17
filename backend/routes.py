from app import app,db
from flask import request,jsonify

from models import Note 

#Get all Notes

@app.route("/api/notes",methods=["GET"])

def get_notes():
    notes = Note.query.all()
    result = [note.to_json() for note in notes]
    return jsonify(result)

#create a note
@app.route("/api/notes",methods=["POST"])
def create_note():
    try:
        data = request.json 

        required_fields = ["name","description"]
        for field in required_fields:
            return jsonify({"error":f'Missing required field : {field}'}),400

        name = data.get("name")
        description=data.get("description")
        new_note = Note(name=name,description=description)
        db.session.add(new_note)
        db.session.commit()
        return jsonify({"msg":"Notes created successfully"}),201
    except Exception  as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500

#delete note
@app.route("/api/notes/<int:id>",methods=["DELETE"])
def deletenote(id):
    try:
        note = Note.query.get(id)
        if note is None:
            return jsonify({"error":"Notes not found"}),404
        db.session.delete(note)
        db.session.commit()
        return jsonify({"msg":"Notes deleted successfully"}),200
    except Exception as e :
        db.session.rollback()
        return jsonify({"error":str(e)}),500

#update notes

@app.route("/api/notes/<int:id>",methods=["PATCH"])
def update_note(id):
    try:
        note = Note.query.get(id)
        if note is None:
            return jsonify({"error":"Notes not found"}),404
        data = request.json
        note.name = data.get("name",note.name)
        note.description = data.get("description",note.description)
        db.session.commit()
        return jsonify({note.to_json()}),200
    except Exception  as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500
