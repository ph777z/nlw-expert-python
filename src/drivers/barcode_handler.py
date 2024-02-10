from pathlib import Path

from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeWriter:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        tags_path = Path('tags')

        if not tags_path.exists():
            tags_path.mkdir()

        path_from_tag = str(Path(tags_path, f'{tag}'))
        tag.save(path_from_tag)

        return path_from_tag
