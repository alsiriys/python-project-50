import os

from gendiff.build_tree import build_tree
from gendiff.format.stylish import format_stylish
from gendiff.parsers import parse


def get_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lstrip(".").lower()


def generate_diff(file_path1, file_path2, format_name="stylish"):
    with (
        open(file_path1, encoding="utf-8") as f1,
        open(file_path2, encoding="utf-8") as f2,
    ):
        data1 = parse(f1.read(), get_format(file_path1))
        data2 = parse(f2.read(), get_format(file_path2))

    tree = build_tree(data1, data2)

    if format_name == "stylish":
        return format_stylish(tree)

    raise ValueError(f"Unknown format: {format_name}")
