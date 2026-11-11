def to_str(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        indent = " " * (depth * 4)
        lines = []
        for k, v in value.items():
            formatted_value = to_str(v, depth + 1)
            lines.append(f"{indent}    {k}: {formatted_value}")
        return "{\n" + "\n".join(lines) + f"\n{indent}}}"
    return str(value)


def format_stylish(tree, depth=1):
    indent = " " * (depth * 4 - 2)
    lines = []

    for node in tree:
        t, k = node["type"], node["key"]

        if t == "nested":
            nested_format = format_stylish(node["children"], depth + 1)
            lines.append(f"{indent}  {k}: {nested_format}")
        elif t == "added":
            lines.append(f"{indent}+ {k}: {to_str(node['value'], depth)}")
        elif t == "deleted":
            lines.append(f"{indent}- {k}: {to_str(node['value'], depth)}")
        elif t == "unchanged":
            lines.append(f"{indent}  {k}: {to_str(node['value'], depth)}")
        elif t == "changed":
            lines.extend(
                (
                    f"{indent}- {k}: {to_str(node['old_value'], depth)}",
                    f"{indent}+ {k}: {to_str(node['new_value'], depth)}",
                )
            )

    closing_indent = " " * ((depth - 1) * 4)
    return "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"
