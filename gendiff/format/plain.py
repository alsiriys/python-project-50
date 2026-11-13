def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(tree, path=""):
    lines = []

    for node in tree:
        key = node["key"]
        node_type = node["type"]
        current_path = f"{path}.{key}" if path else key

        if node_type == "nested":
            lines.append(format_plain(node["children"], current_path))
        elif node_type == "added":
            val = format_value(node["value"])
            lines.append(
                f"Property '{current_path}' was added with value: {val}"
            )
        elif node_type == "deleted":
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == "changed":
            old_val = format_value(node["old_value"])
            new_val = format_value(node["new_value"])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_val} to {new_val}"
            )

    return "\n".join(lines)
