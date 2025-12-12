"""
Freeze Flask application to static HTML for GitHub Pages deployment.
This script generates static HTML files from the Flask templates.
Note: This creates a static snapshot - dynamic features won't work.
"""
from flask_frozen import Freezer
from app import app, db, User, Attendance, StudentCourse
import os

# Configure for freezing
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

freezer = Freezer(app)

@freezer.register_generator
def error_handlers():
    """Generate error pages if needed."""
    yield '/login', {}

if __name__ == '__main__':
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
        
        # Create dummy data if needed
        if not User.query.first():
            from werkzeug.security import generate_password_hash
            
            # Create a test user
            admin = User(
                index_number='admin',
                password=generate_password_hash('admin123'),
                role='admin',
                name='System Administrator'
            )
            db.session.add(admin)
            db.session.commit()
    
    # Freeze the application
    print("Freezing Flask application to static files...")
    freezer.freeze()
    print(f"Static files generated in '{app.config['FREEZER_DESTINATION']}' directory")
