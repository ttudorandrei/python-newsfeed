from flask import Blueprint, request, jsonify, session
import sys

from app.models import User
from app.db import get_db

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/users", methods=["POST"])
def signup():
    data = request.get_json()
    db = get_db()

    try:
        # attempt creating a new user
        newUser = User(
            username=data["username"],
            email=data["email"],
            password=data["password"]
        )
        db.add(newUser)
        db.commit()
    except:
        # insert failed, log and send error to front end
        print(sys.exc_info()[0])
        # rollback last commit
        db.rollback()
        return jsonify(message="Signup failed"), 500

    # clear any previous sessions, add user_id (to the session) to use for querying the db and a boolean property (to the session) to conditionally render elements
    session.clear()
    session["user_id"] = newUser.id
    session["loggedIn"] = True

    return jsonify(id=newUser.id)
