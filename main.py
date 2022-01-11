import os


def human_read_format(size):
    e = 1
    while size > 1023:
        size = size / 1024
        e += 1
    if e == 1:
        return str(round(size)) + "Б"
    elif e == 2:
        return str(round(size)) + "КБ"
    elif e == 3:
        return str(round(size)) + "МБ"
    elif e == 4:
        return str(round(size)) + "ГБ"


def get_files_sizes():
    r = []
    for i in os.listdir('.'):
        if os.path.isfile(i):
            r.append(str(i) + ' ' + human_read_format(os.path.getsize(i)))
    return '\n'.join(r)
