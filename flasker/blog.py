from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from flasker.auth import login_required
from flasker.db import get_db

bp= Blueprint("blog", __name__)

@bp.route("/")
def index():
    db = get_db()
    posts = db.execute(
        "SELECT p.id, title, body, created, author_id, username"
        "FROM posts p JOIN user u ON p.author_id = u.id"
        "ORDER By created DESC"
    ).fetchall()
    return render_template("blog/index.html", posts=posts)
