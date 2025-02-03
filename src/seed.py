from models import db, Planet
from app import app

# Create several planets 
with app.app_context():
    p1 = Planet(name="Earth")
    p2 = Planet(name="Mars")

    db.session.add(p1)
    db.session.add(p2)

    db.session.commit()