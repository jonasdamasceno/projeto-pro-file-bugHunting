from pro_filer.actions.main_actions import find_duplicate_files  # NOQA

import pytest


def test_find_duplicate_files_no_duplicates(tmp_path):
    # Criação de arquivos de teste
    output_path1 = tmp_path / "valid.py"
    output_path1.write_text("extension test")
    no_extension1 = str(output_path1)

    output_path2 = tmp_path / "valid2.py"
    output_path2.write_text("extension test aaa")
    with_extension1 = str(output_path2)

    # Definição do contexto
    context = {
        "all_files": [no_extension1, with_extension1]
    }

    # Execução do teste
    result = find_duplicate_files(context)

    # Verificação do resultado
    assert result == []


def test_find_duplicate_files_with_duplicates(tmp_path):
    # Criação de arquivos de teste
    output_path1 = tmp_path / "valid.py"
    output_path1.write_text("extension test")
    no_extension1 = str(output_path1)

    output_path2 = tmp_path / "valid.py"
    output_path2.write_text("extension test 2 ")
    with_extension1 = str(output_path2)

    output_path3 = tmp_path / "valid.py"
    output_path3.write_text("extension test3 ")
    aaaaaa = str(output_path3)

    # Definição do contexto
    context = {
        "all_files": [no_extension1, with_extension1, aaaaaa]
    }

    # Execução do teste
    result = find_duplicate_files(context)

    # Verificação do resultado
    assert result == [
        (no_extension1, with_extension1),
        (no_extension1, aaaaaa),
        (with_extension1, aaaaaa),
    ]


def test_find_duplicate_files_with_invalid_file():
    # Definição do contexto com arquivos inválidos
    context = {
        "all_files": [
            "./tests/invalid.py",
            "./tests/actions/invalid.py",
        ]
    }

    # Verificação do lançamento de exceção
    with pytest.raises(ValueError):
        find_duplicate_files(context)
