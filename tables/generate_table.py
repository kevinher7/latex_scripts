import argparse
import csv

from ..utils.files import ensure_file_extension


def format_table(headers: str, table_data: str, columns: int, caption: str, table_label: str):
    return f"""
    \\begin{{table}}[H]
        \\centering
        \\caption{{{caption}}}
        \\label{{tab:{table_label}}}
        \\begin{{tabular}}{{{'|'.join(['c'] * columns)}}}
            \\toprule
{headers}
            \\midrule
{table_data}
            \\bottomrule
        \\end{{tabular}}
    \\end{{table}}
    """


def parse_csv_data(filename, caption=None, label=None):
    filename = ensure_file_extension(filename, ".csv")

    if not caption:
        caption = f"I'm a caption for {filename}"
    if not label:
        label = filename.split(".")[0]

    with open(filename, newline="", encoding="utf-8") as file:
        reader = list(csv.reader(file))
        headers = reader.pop(0)
        number_of_columns = len(headers)
        headers = "\t\t" + " & ".join(headers) + "\\\\"

        table_rows = ""
        for row in reader:
            table_rows = table_rows + "\t\t" + " & ".join(row) + "\\\\\n"

    table_rows = table_rows.rstrip()

    latex_table = format_table(
        headers, table_rows, number_of_columns, caption, label)

    return latex_table


def create_tex_file(tex_string, filename="output.tex"):
    filename = ensure_file_extension(filename, ".tex")

    try:
        with open(filename, "w", encoding="utf-8") as tex_file:
            tex_file.write(tex_string)
        print(f"Successfully created LaTeX file: {filename}")
    except Exception as e:
        print(f"Error creating LaTeX file: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a LaTeX table from a csv file")
    parser.add_argument("input_file", type=str,
                        help="Name of input file (raw csv data)")
    parser.add_argument("-c", "--caption", type=str,
                        help="Caption of LaTeX Table", default=None)
    parser.add_argument("-l", "--label", type=str,
                        help="Label for LaTeX Table", default=None)
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Suppress output file creation.",
                        default=False)

    args = parser.parse_args()

    if args.input_file is None:
        raise ValueError("Input file not provided.")

    latex_table = parse_csv_data(args.input_file, args.caption, args.label)

    if not args.quiet:
        create_tex_file(latex_table, args.input_file)

    return latex_table


if __name__ == "__main__":
    print(main())
