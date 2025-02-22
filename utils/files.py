def ensure_file_extension(file_name, extension):
    if file_name[-4:] != extension:
        if not "." in extension:
            extension = "." + extension

        if "." in file_name:
            raise ValueError(
                f"Invalid File Extension for {file_name}. Expected {extension}")

        if len(extension) > 5:
            raise ValueError("File extension is too long!")

        file_name += extension

    return file_name
