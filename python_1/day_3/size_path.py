import os


def path_join(path_to_dir, files):
    return os.path.join(path_to_dir, files)


def get_size(path_to_dir):
    list_files = os.listdir(path_to_dir)
    count = 0
    for files in list_files:
        local_path = path_join(path_to_dir, files)
        file_size = os.path.getsize(local_path)
        count = count + file_size
        print("Найдены:",path_to_dir, files, count)
        if os.path.isdir(local_path):
            count += get_size(local_path)
    return count


def main():
    work_path = os.sys.argv[1]
    get_size(work_path)


if __name__ == '__main__':
    main()
