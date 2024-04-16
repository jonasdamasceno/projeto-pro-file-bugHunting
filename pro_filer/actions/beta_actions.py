"""Arquivo que estudantes devem editar"""


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=lambda x: x.count("/"))
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        rename_file = file_name
        new_search_term = search_term

        if not case_sensitive:
            rename_file = file_name.lower()
            new_search_term = search_term.lower()

        if new_search_term in rename_file:
            found_files.append(path)

    return found_files
