from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_with_empty_context(capsys):
    # Arrange
    context = {
        "all_files": [],
        "all_dirs": []
    }

    # Act
    show_preview(context)

    # Assert
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"


def test_show_preview_with_basic_context(capsys):
    # Arrange
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py"
        ],
        "all_dirs": ["src", "src/utils"]
    }

    # Act
    show_preview(context)

    # Assert
    captured = capsys.readouterr()
    assert captured.out == (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )


def test_show_preview_with_additional_files_and_dirs(capsys):
    # Arrange
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
            "src/extra_file1.py",
            "src/extra_file2.py",
            "src/extra_file3.py"
        ],
        "all_dirs": ["src", "src/utils", "src/extras"]
    }

    # Act
    show_preview(context)

    # Assert
    captured = capsys.readouterr()
    assert captured.out == (
        "Found 6 files and 3 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py', "
        "'src/extra_file1.py', 'src/extra_file2.py']\n"
        "First 5 directories: ['src', 'src/utils', 'src/extras']\n"
    )
