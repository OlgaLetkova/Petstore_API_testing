import csv


def read_lines_from_csv(using_file, limit=999):
    result = []
    with open(using_file) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            result.append(row)
            if len(result) == limit:
                break
    return result
