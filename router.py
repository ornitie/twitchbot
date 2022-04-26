from flask import Blueprint


router = Blueprint(
    "urls",
    __name__,
)


@router.route("/testing")
def index():
    return "testing external router"


@router.route("/")
def hello_world():
    return "Hello, Twitch, I'm a flask server!"


@router.route("/json")
def json_hello():
    return {"name": "ornitie", "message": "Hello, World!"}
