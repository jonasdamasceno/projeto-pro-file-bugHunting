import pytest
from pro_filer.actions.main_actions import show_disk_usage
from pro_filer.cli_helpers import _get_printable_file_path


@pytest.fixture
def file_context(tmp_path):
    tmp_path_file1 = tmp_path / "file1.txt"
    tmp_path_file1.write_text("File content")
    tmp_path_file2 = tmp_path / "file2.txt"
    tmp_path_file2.write_text("Another file content")
    return {"all_files": [str(tmp_path_file1), str(tmp_path_file2)]}


def test_show_disk_usage_with_files(capsys, file_context):
    get_test1 = f"'{_get_printable_file_path(file_context['all_files'][0])}':"
    get_test2 = f"'{_get_printable_file_path(file_context['all_files'][1])}':"
    show_disk_usage(file_context)
    console_output = capsys.readouterr()
    assert console_output.out == (
        f"{get_test2.ljust(70)} 20 (62%)\n" +
        f"{get_test1.ljust(70)} 12 (37%)\n" +
        f"Total size: {32}\n"
    )


def test_show_disk_usage_no_files(capsys):
    empty_file_context = {"all_files": []}
    show_disk_usage(empty_file_context)
    console_output = capsys.readouterr()
    assert console_output.out == "Total size: 0\n"
