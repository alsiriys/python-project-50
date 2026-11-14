import argparse

from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.add_argument(
        "-f", "--format", default="stylish", help="set format of output"
    )
    args = parser.parse_args()

    diff = generate_diff(
        file_path1=args.first_file,
        file_path2=args.second_file,
        format_name=args.format,
    )
    print(diff)


if __name__ == "__main__":
    main()
