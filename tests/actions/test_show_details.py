import pytest
from datetime import date
from pro_filer.actions.main_actions import show_details


@pytest.fixture
def non_existent_file_context():
    return {"base_path": "/home/trybe/???"}


def test_show_details_file_exists(capsys, tmp_path):
    file_path = tmp_path / "pro-filer-preview.gif"
    file_path.write_text("File content")
    file = {"base_path": str(file_path)}

    show_details(file)

    captured = capsys.readouterr()
    assert captured.out == (
        "File name: pro-filer-preview.gif\n"
        f"File size in bytes: {file_path.stat().st_size}\n"
        "File type: file\n"
        "File extension: .gif\n"
        f"Last modified date: {date.today()}\n"
    )


def test_show_details_file_not_exists(capsys, non_existent_file_context):
    show_details(non_existent_file_context)

    captured = capsys.readouterr()
    assert captured.out == (
        "File '???' does not exist\n"
    )


def test_show_details_file_without_extension(capsys, tmp_path):
    dir_path = tmp_path / "images"
    dir_path.write_text("File content")
    file = {"base_path": str(dir_path)}

    show_details(file)

    captured = capsys.readouterr()
    assert captured.out == (
        "File name: images\n"
        f"File size in bytes: {dir_path.stat().st_size}\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        f"Last modified date: {date.today()}\n"
    )
