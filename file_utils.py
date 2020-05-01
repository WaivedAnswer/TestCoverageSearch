import os


def find_test_files(root_dir: str, search_filter: str, full_search: bool):
    assert(os.path.exists(root_dir))

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if passes_search_filter(file, search_filter) and is_test_file(file):
                output_file(file_path)
            elif full_search and is_test_file(file) and passes_file_search(file_path, search_filter):
                output_file(file_path)


def output_file(file_path):
    print(file_path)


def get_test_file_types():
    return ["cpp", "cs", "py"]


def is_test_file(filename: str):
    test_file_types = get_test_file_types()
    suffix = filename.split('.')[-1]
    if suffix not in test_file_types:
        return False
    return passes_search_filter(filename, "test")


def passes_file_search(file_path, search_filter):
    with open(file_path) as f:
        return passes_search_filter(f.read(), search_filter)


def passes_search_filter(searchable: str, search_filter: str):
    lower = searchable.lower()
    terms = search_filter.split()
    if not terms:
        return False
    for filter_term in terms:
        if lower.find(filter_term.lower()) == -1:
            return False
    return True
