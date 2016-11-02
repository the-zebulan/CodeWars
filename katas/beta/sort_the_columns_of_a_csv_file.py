def sort_csv_columns(csv_file_content):
    return '\n'.join(';'.join(sorted_row) for sorted_row in zip(*sorted(
        (zip(*(row.split(';') for row in csv_file_content.split('\n')))),
        key=lambda col: col[0].lower()
    )))
