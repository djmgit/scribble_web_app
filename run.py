import os
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'secret'
    app.config['admin_token'] = "Bearer 1f3e1016c00260a82f3f38c820d012330ea673c0d04a6153"
    CORS(app, resources={r"*": {"origins": "*"}})

    return app

from controllers import (
    home_page,
    signup,
    login,
    add_note,
    all_notes,
    note_by_id
)

app = create_app()

'''app.register_blueprint(generateBadges.router, url_prefix='/api')
app.register_blueprint(registerUser.router, url_prefix='/user')
app.register_blueprint(loginUser.router, url_prefix='/user')
app.register_blueprint(fileUploader.router, url_prefix='/api/upload')
app.register_blueprint(modifyUser.router, url_prefix='/user/change')
app.register_blueprint(homePage.router)
app.register_blueprint(errorHandlers.router)
app.register_blueprint(resetUser.router, url_prefix='/reset')'''

app.register_blueprint(home_page.router)
app.register_blueprint(signup.router, url_prefix='/api')
app.register_blueprint(login.router, url_prefix='/api')
app.register_blueprint(add_note.router, url_prefix='/api')
app.register_blueprint(all_notes.router, url_prefix='/api')
app.register_blueprint(note_by_id.router, url_prefix='/api')

if __name__ == '__main__':
    app.run()
