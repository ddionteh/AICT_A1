from app.db.db import db  # ✅ FIX: Correct Import for db

class TrafficViolation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.String(50), nullable=False)
    violation_type = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Violation {self.violation_type} for {self.vehicle_id}>'
