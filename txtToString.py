def read_file(filename):
    indices = [13, 113, 145, 153, 184, 196, 211, 225, 237, 0]
    columns = []
    data = []
    with open(filename) as f:
        lines = f.readlines()
    columns = lines[0].strip().split('\t')
    for line in lines[1:]:
        row = []
        line = line.strip()
        for i in range(len(indices) - 1):
            row.append(line[indices[i-1]:indices[i]].rstrip())
        data.append(row)
    return [columns] + data

with open('scriptText.txt', 'w') as text_file:
    read_file(text_file)