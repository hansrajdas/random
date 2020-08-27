import csv

NUMBER_OF_YEARS = 10
START_IDX = 1
END_IDX = START_IDX + NUMBER_OF_YEARS

def update_value(row):
    inc_count = 0
    dec_count = 0
    i = START_IDX
    while i < END_IDX:
        if row[i] < row[i + 1]:
            inc_count += 1
        elif row[i] > row[i + 1]:
            dec_count += 1
        i += 1
    if inc_count > dec_count:
        row[-1] = 'Increasing'
    elif inc_count < dec_count:
        row[-1] = 'Decreasing'
    else:
        row[-1] = 'NoPattern'

def format_row(row):
    is_first_value = True
    res = []
    for v in row:
        if is_first_value:
            res.append('"' + v + '"')
            is_first_value = False
        else:
            res.append(v)
    return ','.join(res)

def update_collaboration_pattern():
    output_file = open('out.csv', 'w')
    is_header = True
    with open('author_50.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if is_header:
                is_header = False
                output_file.write(','.join(row))
                continue
            if row[-1] == 'Non':
                update_value(row)
            output_file.write('\n%s' % format_row(row))
    output_file.close()


update_collaboration_pattern()
