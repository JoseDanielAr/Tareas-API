# routes.py
from flask import Blueprint, jsonify, request
from database import db
from models import Task

tasks_bp = Blueprint("tasks", __name__)


# GET /tasks — listar todas
@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks]), 200


# GET /tasks/<id> — obtener una
@tasks_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(task.to_dict()), 200


# POST /tasks — crear
@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or not data.get("titulo", "").strip():
        return jsonify({"error": "El campo 'titulo' es obligatorio"}), 400

    task = Task(titulo=data["titulo"].strip())
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


# PUT /tasks/<id> — actualizar
@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404

    data = request.get_json()

    if "titulo" in data:
        if not data["titulo"].strip():
            return jsonify({"error": "El campo 'titulo' no puede estar vacío"}), 400
        task.titulo = data["titulo"].strip()

    if "completada" in data:
        task.completada = bool(data["completada"])

    db.session.commit()
    return jsonify(task.to_dict()), 200


# DELETE /tasks/<id> — eliminar
@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Tarea eliminada correctamente"}), 200