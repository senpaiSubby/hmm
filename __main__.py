from quart import (
    Quart,
    render_template,
    session,
    request,
    redirect,
    url_for
    )
from os import system
from app.backend import *

system("clear")

app = Quart(__name__)

@app.route("/", methods=["GET"])
async def home():
    return await render_template("/index.html", notes=listNotes())


@app.route("/addnote", methods=["POST"])
async def nadd():
    form = await request.form
    print(form)
    if form["inputbar"]:
        addNote(form["inputbar"])

    return redirect(url_for("home"))

@app.route("/editnote", methods=["POST"])
async def nedit():
    form = await request.form
    if form["editNote"] and form["inputbar"]:
        editNote(form["editNote"], form["inputbar"])
    return redirect(url_for("home"))

@app.route("/delnote", methods=["POST"])
async def ndel():
    form = await request.form
    if form["deleteNote"]:
        delNote(form["deleteNote"])
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
