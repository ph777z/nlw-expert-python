from flask import Blueprint, request, jsonify

from src.views import TagCreatorView
from src.views.http_types import HttpRequest


tag_routes_bp = Blueprint('tag_routes', __name__)

@tag_routes_bp.post('/create_tag')
def create_tag():
    tag_creator_view = TagCreatorView()

    http_request = HttpRequest(body=request.json) # type: ignore
    response = tag_creator_view.validate_and_create(http_request)

    return jsonify(response.body), response.status_code
