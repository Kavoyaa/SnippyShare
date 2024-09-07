from flask import render_template, flash
from SnippyShare import app, db
from SnippyShare.forms import ContentForm
from SnippyShare.models import Snippets
import uuid

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ContentForm()
    if form.validate_on_submit():   
        id = str(uuid.uuid4())
        s = Snippets(id=id, name=form.title.data, content=form.content.data)
        db.session.add(s)
        db.session.commit()

        snippet = Snippets.query.filter_by(name=form.title.data, content=form.content.data).all()[-1]

        return render_template("success.html", title="Success", id=snippet.id)
    else:
        return render_template("index.html", form=form)

@app.route("/snippets/<n>")
def snippets(n):
    snippet =  Snippets.query.filter_by(id=n).first()
    content = snippet.content
    return render_template("snippets.html", title=snippet.name, content=content, id=n)

@app.route("/raw/<n>")
def raw(n):
    snippet =  Snippets.query.filter_by(id=n).first()
    content = snippet.content.replace("<", "&lt;").replace(">", "&gt;")
    return f"<pre>{content}</pre>"

