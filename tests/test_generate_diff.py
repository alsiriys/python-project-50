import pytest

from gendiff import generate_diff
from gendiff.parsers import parse


def read_fixture(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()


def test_generate_diff_json():
    file1 = "tests/files_for_testing/file1.json"
    file2 = "tests/files_for_testing/file2.json"
    expected_path = "tests/files_for_testing/expected_text.txt"
    expected = read_fixture(expected_path)
    assert generate_diff(file1, file2) == expected


def test_generate_diff_yaml():
    file1 = "tests/files_for_testing/file1.yaml"
    file2 = "tests/files_for_testing/file2.yaml"
    expected_path = "tests/files_for_testing/expected_text.txt"
    expected = read_fixture(expected_path)
    assert generate_diff(file1, file2) == expected


def test_generate_diff_nested_json():
    file1 = "tests/files_for_testing/new_file1.json"
    file2 = "tests/files_for_testing/new_file2.json"
    expected_path = "tests/files_for_testing/new_file_expected_text.txt"
    expected = read_fixture(expected_path)
    assert generate_diff(file1, file2) == expected


def test_generate_diff_nested_yaml():
    file1 = "tests/files_for_testing/new_file1.yml"
    file2 = "tests/files_for_testing/new_file2.yaml"
    expected_path = "tests/files_for_testing/new_file_expected_text.txt"
    expected = read_fixture(expected_path)
    assert generate_diff(file1, file2) == expected


def test_unknown_file_format():
    with pytest.raises(ValueError):
        parse("Data", "txt")


def test_difference_unknown_format():
    file1 = "tests/files_for_testing/new_file1.json"
    file2 = "tests/files_for_testing/new_file2.json"
    with pytest.raises(ValueError):
        generate_diff(file1, file2, format_name="unknown_format")
