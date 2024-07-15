import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

def parse_args():
    parser = argparse.ArgumentParser(description="Sorting folder")
    parser.add_argument("--source", "-s", help="Source folder", required=True)
    parser.add_argument("--output", "-o", help="Output folder", default="dist")
    return parser.parse_args()

def grabs_folder(path: Path) -> None:
    for item in path.iterdir():
        if item.is_dir():
            grabs_folder(item)
        else:
            folder.append(item)

def copy_file(path: Path, output: Path) -> None:
    ext = path.suffix[1:]  # отримуємо розширення без крапки
    if ext:  # перевірка, чи є розширення
        target_dir = output / ext  # створюємо підкаталог з ім'ям розширення
        target_dir.mkdir(parents=True, exist_ok=True)  # створюємо підкаталог, якщо він не існує
        copyfile(path, target_dir / path.name)  # копіюємо файл до підкаталогу
        logging.info(f"Файл {path} скопійовано до {target_dir}")
    else:
        logging.info(f"Файл {path} не має розширення, пропущено")

if __name__ == '__main__':
    args = parse_args()
    source = Path(args.source)
    output = Path(args.output)

    folder = []

    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    grabs_folder(source)

    threads = []
    for file_path in folder:
        thread = Thread(target=copy_file, args=(file_path, output))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Обробка завершена. Вихідна директорія: {output}")
