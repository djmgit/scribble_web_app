from flask import Blueprint, jsonify

router = Blueprint('home_page', __name__)


@router.route('/', methods=['GET'])
def homePage():
    return 'testing'
