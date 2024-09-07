from SnippyShare import db

class Snippets(db.Model):
    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Snippet({self.id}, {self.name}, {self.content})"
