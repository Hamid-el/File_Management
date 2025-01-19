"""from time import sleep
from shutil import move
from os.path import exists, join, splitext
from os import scandir, rename
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import logging



audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg",
                    ".svgz", ".ai", ".eps", ".ico"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

source_dir = "C:/Users/hamid/Downloads"
dest_dir_sfx = "C:/Users/hamid/Desktop/Music/SFX"
dest_dir_music = "C:/Users/hamid/Desktop/music"
dest_dir_video = "C:/Users/hamid/Desktop/videos"
dest_dir_image = "C:/Users/hamid/Desktop/images"
dest_dir_documents = "C:/Users/hamid/Desktop/documents"



def make_unique(destination, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{destination}/{name}"):
        name = f"{filename} ({str(counter)}){extension}"
        counter += 1

    return name

def move_file(destination, entry, name):
    if not exists(destination):
        logging.error(f"Destination directory does not exist: {destination}")
        return
    if exists(f"{destination}/{name}"):
        unique_name = make_unique(destination, name)
        old_name = join(destination, name)
        new_name = join(destination, unique_name)
        rename(old_name, new_name)

    move(entry, destination)

#def file_matches_extension(name, extensions):
 #   return any(name.lower().endswith(ext) for ext in extensions)

#-------------------------------------------------
class MoverHandler(FileSystemEventHandler):

    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:

                 name = entry.name
                 self.check_audio_files(entry, name)
                 self.check_video_files(entry, name)
                 self.check_image_files(entry, name)
                 self.check_document_files(entry, name)

    def check_video_files(self, entry, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_audio_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:
                    dest = dest_dir_sfx
                else:
                    dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")




# ! NO NEED TO CHANGE BELOW CODE
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()"""

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import time
import os
import logging

# Main download folder
source_dir = "C:\\Users\\hamid\\Downloads"

# Add new folder if needed
destination_dir_sfx = os.path.join(source_dir, "Downloads-sfx")
destination_dir_txt = os.path.join(source_dir, "Downloads-txt")
destination_dir_music = os.path.join(source_dir, "Downloads-music")
destination_dir_video = os.path.join(source_dir, "Downloads-video")
destination_dir_image = os.path.join(source_dir, "Downloads-image")
destination_dir_pdf = os.path.join(source_dir, "Downloads-pdf")
destination_dir_office = os.path.join(source_dir, "Downloads-office")
destination_dir_3d_printer = os.path.join(source_dir, "Downloads-3d-printer")
destination_dir_arch_comp = os.path.join(source_dir, "Downloads-archive-compression")

# Extensions
image_extensions = (".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd",
                    ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt",
                    ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico")

video_extensions = (".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mkv", ".mp4", ".mp4v", ".m4v", ".avi",
                    ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd")

office_extensions = (".doc", ".docx", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".accdb")

audio_extensions = (".m4a", ".flac", "mp3", ".wav", ".wma", ".aac")

printer3d_extensions = (".step", ".stl")

basic_document_extensions = (".txt", ".log", ".json", ".md")

pdf_extensions = (".pdf", ".pdfk")

arch_comp_extensions = (".7z", ".apk", ".ark", ".arc", ".arj", ".a", ".ar", ".cab", ".car", ".cpio", ".dmg", ".ear",
                        ".gca", ".genozip", ".pak", ".partimg", ".paq6", ".paq7", ".paq8", ".rar", ".shk", ".sit",
                        ".sitx", ".sqx", ".gz", ".tgz", ".bz2", ".tbz2", ".tlz", ".txz", ".shar", ".lbr",
                        ".iso", ".mar", ".sbx", ".tar", ".f", ".lz", ".lz4", ".lzma", ".lzo", ".rz", ".sfark", ".sz",
                        ".q", ".xz", ".z", ".zst", ".war", ".wim", ".uca", ".uha", ".xar", ".xp3", ".yz1",
                        ".zip", ".zipx", ".zoo", ".zpaq", ".zz")


def make_unique(destination, name):
    filename, extension = os.path.splitext(name)
    counter = 1
    while os.path.exists(os.path.join(destination, name)):
        name = f"{filename} ({counter}){extension}"
        counter += 1
    return name


def move(destination, entry, name):
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)

        if not os.path.exists(os.path.join(destination, name)):
            shutil.move(entry.path, os.path.join(destination, name))

        else:
            unique_name = make_unique(destination, name)
            shutil.move(entry.path, os.path.join(destination, unique_name))
    except Exception as e:
        logging.error(f'move() -> destination {destination}; entry {entry}; name {name}')
        logging.error(f'Exception throwed: {e}')


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        path_split = event.src_path.split('\\')
        path_split = path_split[:-1]
        path_join = '\\'.join(path_split)

        with os.scandir(path_join) as entries:
            for entry in entries:
              if entry.is_file():
                name = entry.name

                if name.lower().endswith(tuple(audio_extensions)):
                    print(f'Moving sound {name}')
                    if entry.stat().st_size < 25000000 or "SFX" in name: #max 25 MB
                        move(destination_dir_sfx, entry, name) # sound effect
                    else:
                        move(destination_dir_music, entry, name) #music

                elif name.lower().endswith(tuple(video_extensions)):
                    print(f'Moving video {name}')
                    move(destination_dir_video, entry, name)

                elif name.lower().endswith(tuple(image_extensions)):
                    print(f'Moving image {name}')
                    move(destination_dir_image, entry, name)

                elif name.lower().endswith(tuple(printer3d_extensions)):
                    print(f'Moving 3d printer {name}')
                    move(destination_dir_3d_printer, entry, name)

                elif name.lower().endswith(tuple(pdf_extensions)):
                    print(f'Moving pdf {name}')
                    move(destination_dir_pdf, entry, name)

                elif name.lower().endswith(tuple(basic_document_extensions)):
                    print(f'Moving basic text file {name}')
                    move(destination_dir_txt, entry, name)

                elif name.lower().endswith(tuple(office_extensions)):
                    print(f'Moving office doc {name}')
                    move(destination_dir_office, entry, name)

                elif name.lower().endswith(tuple(arch_comp_extensions)):
                    print(f'Moving zip {name}')
                    move(destination_dir_arch_comp, entry, name)

                else:
                    print(f'File {name} not recognized.')


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='C:\\download-folder.log',
                        encoding='utf-8')
    except PermissionError:
        print('Permission denied to file')
    folder_to_track = source_dir
    observer = Observer()
    event_handler = Handler()
    observer.schedule(event_handler, folder_to_track, recursive=False)
    observer.start()
    print('Observer started')
    try:
        while True:
            time.sleep(60) # wait 1min until file is downloaded
    except KeyboardInterrupt:
        observer.stop()
    observer.join()