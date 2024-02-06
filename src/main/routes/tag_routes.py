from pathlib import Path

from flask import Blueprint, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

from src.utils import dir_tags


tag_routes_bp = Blueprint('tag_routes', __name__)

@tag_routes_bp.post('/create_tag')
def create_tag():
    body = request.json
    product_code = body.get('product_code') # type: ignore
    if not product_code:
        return 'É preciso informar product_code', 400

    tag = Code128(product_code, writer=ImageWriter)
    tag_path = Path(dir_tags(), product_code)
    tag.save(tag_path) # type: ignore

    return jsonify({ 'tag_path': f'{tag_path}' })
