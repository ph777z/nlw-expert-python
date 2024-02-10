from typing import Dict

from src.drivers import BarcodeWriter


class CreateTagController:
    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_tag(product_code)

        return self.__format_response(path_from_tag)

    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarcodeWriter()

        return barcode_handler.create_barcode(product_code)

    def __format_response(self, path_from_tag: str) -> Dict:
        return {
            'data': {
                'type': 'Tag Image',
                'count': 1,
                'path': f'{path_from_tag}.png'
            }
        }
