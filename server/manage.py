from flask.cli import FlaskGroup

from backend import create_app
from backend.models import db

app = create_app()

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()