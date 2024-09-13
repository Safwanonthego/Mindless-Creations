import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def organizeFiles(folderPathInput, folderPathOutput):
    #Dictionary
    extensionDic = {
        'jpg': 'Images',
        'jpeg': 'Images',
        'png': 'Images',
        'gif': 'Images',
        'bmp': 'Images',
        'pdf': 'PDFs',
        'doc': 'Documents',
        'docx': 'Documents',
        'xls': 'Spreadsheets',
        'xlsx': 'Spreadsheets',
        'ppt': 'Presentations',
        'pptx': 'Presentations',
        'txt': 'TextFiles',
        'mp3': 'Music',
        'wav': 'Music',
        'mp4': 'Videos',
        'mov': 'Videos',
        'avi': 'Videos',
        # Add more extensions and folders as needed
    }
    for file in os.listdir(folderPathInput):
        filePathInput = os.path.join(folderPathInput, file)
        if os.path.isfile(filePathInput):
            fileExtension = file.split('.')[-1].lower()
            if fileExtension in extensionDic:
                newFolder = os.path.join(folderPathOutput, extensionDic[fileExtension])
                if not os.path.exists(newFolder):
                    os.makedirs(newFolder)
                filePathOutput = os.path.join(newFolder, file)
                shutil.move(filePathInput, filePathOutput)
                # print(f'Moved: {file} -> {newFolder}')
            else:
                print(f"No folder assigned for extention '.{fileExtension}'")


class EventHandler(FileSystemEventHandler):
    def __init__(self, folderPathInput, folderPathOutput):
        self.folderPathInput = folderPathInput
        self.folderPathOutput = folderPathOutput

    def on_modified(self, event):
        organizeFiles(self.folderPathInput, self.folderPathOutput)



if __name__ == "__main__":
    folderPathInput = input("Enter Path Input: ")
    folderPathOutput = input("Enter Path Output: ")
    
    event_handler = EventHandler(folderPathInput, folderPathOutput)
    observer = Observer()
    observer.schedule(event_handler, folderPathInput, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

