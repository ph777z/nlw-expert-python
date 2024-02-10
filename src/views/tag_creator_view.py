from src.controllers import CreateTagController
from .http_types import HttpRequest, HttpResponse


class TagCreatorView:
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = CreateTagController()

        body = http_request.body
        product_code = body['product_code']

        formatted_response = tag_creator_controller.create(product_code)

        return HttpResponse(status_code=200, body=formatted_response)
