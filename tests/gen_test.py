import pytest
from gendiff.generate_diff import generate_diff
from pathlib import Path


@pytest.mark.parametrize(
    "file1, file2, file_answer, form_name",
    [
        ('file1.json', 'file2.json', 'answer_stylish.txt', 'stylish'),
        ('file1.yml', 'file2.yml', 'answer_stylish.txt', 'stylish'),
        ('file1.json', 'file2.json', 'answer_plain.txt', 'plain'),
        ('file1.yml', 'file2.yml', 'answer_plain.txt', 'plain'),
        ('file1.json', 'file2.json', 'answer_json.json', 'json'),
        ('file1.yml', 'file2.yml', 'answer_json.json', 'json'),
    ]
)
def test_generate_diff(file1, file2, file_answer, form_name):
    with open(Path() / 'tests/fixtures' / file_answer) as f:
        corr_answer = f.read()
    assert generate_diff(file1, file2, form_name) == corr_answer
    