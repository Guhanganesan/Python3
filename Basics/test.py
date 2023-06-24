# Getting the Size of a File in Python Using Different Units
import os
file_path = r'D:\GithubRepositories\Python-2023\Python3\Basics\part_6.mkv'

def get_size(file_path, unit='mb'):
    file_size = os.path.getsize(file_path)
    exponents_map = {'bytes': 0, 'kb': 1, 'mb': 2, 'gb': 3}
    if unit not in exponents_map:
        raise ValueError("Must select from \
        ['bytes', 'kb', 'mb', 'gb']")
    else:
        size = file_size / 1024 ** exponents_map[unit]
        print(size)
        return round(size, 3)


print(get_size(file_path, 'mb'))
