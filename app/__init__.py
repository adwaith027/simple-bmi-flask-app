from flask import Flask

def create_app():
    app=Flask(__name__)
    
    from app.routes import bmi_bp
    app.register_blueprint(bmi_bp)
    
    return app