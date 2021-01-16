import pathlib
from dateutil.parser import parse
from datetime import datetime, timedelta

FILE_PATTERN = '*.zip'
ARCHIVE = 'archive'
ARCHIVE_WEEKDAY = 1

if __name__ == '__main__':
    cur_path = pathlib.Path('./files/')
    zip_file_path = cur_path.joinpath(ARCHIVE)

    paths = zip_file_path.glob(FILE_PATTERN)
    current_date = datetime.today()
    print('Delete old files!')

    for path in paths:
        name = path.stem  # возвращает имя файла без расширения
        path_date = parse(name)
        path_timedelta = current_date - path_date
        if path_timedelta > timedelta(days=30) and path_date.weekday() != ARCHIVE_WEEKDAY:
            path.unlink()
            print('File deleted')
