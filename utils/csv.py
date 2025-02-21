import os


def get_csv_files_in_path(path):
    csv_paths_list = []

    for file in os.listdir(path):
        if file.endswith("csv"):
            csv_paths_list.append(file)

    return csv_paths_list


def ensure_csv_extension(file_name):
    if file_name[-4:] != ".csv":
        file_name += ".csv"

    return file_name


def get_csv_path_from_filename(file_name):
    current_path = os.getcwd()

    file_name = ensure_csv_extension(file_name)
    file_path = os.path.join(current_path, file_name)

    return file_path
