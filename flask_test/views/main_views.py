from flask import Blueprint

# 'main' 은 나중에 함수명으로 URL을 찾아내는 url_for 함수에서 사용됨.
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Hello, Flask!!'
