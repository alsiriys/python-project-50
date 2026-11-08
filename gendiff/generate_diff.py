import os

from gendiff.parsers import parse


def get_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lstrip(".").lower()


def generate_diff(file_path1, file_path2):
    with (
        open(file_path1, encoding="utf-8") as f1,
        open(file_path2, encoding="utf-8") as f2,
    ):
        data1 = parse(f1.read(), get_format(file_path1))
        data2 = parse(f2.read(), get_format(file_path2))

    all_keys = sorted(list(data1.keys() | data2.keys()))

    result_lines = []

    def to_str(value):
        if isinstance(value, bool):
            return str(value).lower()
        return str(value)

    for key in all_keys:
        if key in data1 and key not in data2:
            result_lines.append(f"  - {key}: {to_str(data1[key])}")

        elif key not in data1 and key in data2:
            result_lines.append(f"  + {key}: {to_str(data2[key])}")

        elif data1[key] == data2[key]:
            result_lines.append(f"    {key}: {to_str(data1[key])}")

        else:
            result_lines.extend(
                (
                    f"  - {key}: {to_str(data1[key])}",
                    f"  + {key}: {to_str(data2[key])}",
                )
            )

    return "{\n" + "\n".join(result_lines) + "\n}"
