from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flasker.auth import login_required
from flasker.db import get_db

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    db = get_db()
    posts = db.execute(
        "SELECT p.id, title, body, created, author_id, username"
        " FROM post p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()
    return render_template("blog/index.html", posts=posts)

@bp.route("/oversikt")
def oversikt():
    """Show all the posts, most recent first."""
    db = get_db()
    ting = db.execute(
        "SELECT id, navn, tilstand, created, lokasjon"
        " FROM ting"
        " ORDER BY navn"
    ).fetchall()
    print(ting)
    return render_template("blog/oversikt.html", ting=ting)

def get_post(id, check_author=True):
    """Get a post and its author by id.
    Checks that the id exists and optionally that the current user is
    the author.
    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post = (
        get_db()
        .execute(
            "SELECT p.id, title, body, created, author_id, username"
            " FROM post p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None
        print(title)

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
                (title, body, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/create.html")

@bp.route("/create_item", methods=("GET", "POST"))
@login_required
def create_item():
    try:
        print("creating")
        """Create a new item."""
        print(request.method)
        if request.method == "POST":
            navn = request.form["navn"]
            print(navn)
            tilstand = request.form["tilstand"]
            print(tilstand)
            antall = request.form["antall"]
            print(antall)
            lokasjon = request.form["hvor"]
            print(lokasjon)
            _type = request.form["type"]
            print(_type)

            print(f"""navn {navn}
                    tilstand {tilstand}
                    antall {antall}
                    lokasjon {lokasjon}
                    _type {_type}""")


            error = None

            if not navn:
                error = "navn må angis."

            if error is not None:
                flash(error)
            else:
                db = get_db()
                db.execute(
                    "INSERT INTO ting (navn, tilstand, mengde, _type, lokasjon) VALUES (?,?,?,?,?)",
                    (navn, tilstand, antall, _type, lokasjon)
                )
                db.commit()
                return redirect(url_for("blog.oversikt"))
    except Exception as e:
            print(e)
        

    return render_template("blog/create_item.html")

    """ id INTEGER PRIMARY KEY AUTOINCREMENT,
    navn TEXT UNIQUE NOT NULL,
    tilstand TEXT NOT NULL,
    mengde FLOAT NOT NULL,
    _type TEXT NOT NULL,
    lokasjon TEXT NOT NULL
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

 """


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE post SET title = ?, body = ? WHERE id = ?", (title, body, id)
            )
            db.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/update.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a post.
    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("blog.index"))