from .http_types import HttpRequest, HttpResponse


class TagCreatorView:
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body['product_code']
        print(product_code)

        return HttpResponse(status_code=200, body='asdfasd')
