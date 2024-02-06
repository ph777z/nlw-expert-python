from pathlib import Path


def dir_tags():
    tags_path = Path('tags')

    if not tags_path.exists():
        tags_path.mkdir()

    return tags_path
