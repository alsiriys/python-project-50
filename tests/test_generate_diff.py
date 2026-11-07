from gendiff import generate_diff


def read_fixture(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def test_generate_diff_json():
    file1 = 'tests/files_for_testing/file1.json'
    file2 = 'tests/files_for_testing/file2.json'
    expected_path = 'tests/files_for_testing/expected_text.txt'

    expected = read_fixture(expected_path)

    assert generate_diff(file1, file2) == expected
