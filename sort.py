import os


VIDEO_FORMAT =[
    ".mp4",   # MPEG-4 Part 14
    ".mov",   # Apple QuickTime Movie
    ".avi",   # Audio Video Interleave
    ".mkv",   # Matroska Video
    ".flv",   # Flash Video
    ".wmv",   # Windows Media Video
    ".webm",  # WebM Video
    ".m4v",   # MPEG-4 Video
    ".3gp",   # 3GPP Multimedia File
    ".mpeg",  # MPEG Video File
    ".mpg",   # MPEG Video File
    ".mxf",   # Material Exchange Format
    ".ogv",   # Ogg Video
    ".ts",    # MPEG Transport Stream
    ".vob",   # Video Object (DVD Video)
    ".rm",    # RealMedia
    ".asf"    # Advanced Systems Format
]

AUDIO_FORMAT = [
    ".mp3",  # MPEG-1 Audio Layer III
    ".wav",  # Waveform Audio File Format
    ".flac", # Free Lossless Audio Codec
    ".aac",  # Advanced Audio Coding
    ".ogg",  # Ogg Vorbis
    ".m4a",  # MPEG-4 Audio
    ".wma",  # Windows Media Audio
    ".alac", # Apple Lossless Audio Codec
    ".aiff", # Audio Interchange File Format
    ".pcm",  # Pulse Code Modulation
    ".opus", # Opus Audio Codec
    ".amr",  # Adaptive Multi-Rate
    ".dsd",  # Direct Stream Digital
    ".ra",   # RealAudio
    ".mpc"   # Musepack
]

IMAGE_FORMAT = [
    ".jpg",   # Joint Photographic Experts Group
    ".jpeg",  # Joint Photographic Experts Group
    ".png",   # Portable Network Graphics
    ".gif",   # Graphics Interchange Format
    ".bmp",   # Bitmap Image File
    ".tiff",  # Tagged Image File Format
    ".tif",   # Tagged Image File Format (alternative extension)
    ".webp",  # WebP Image
    ".heic",  # High Efficiency Image Coding
    ".svg",   # Scalable Vector Graphics
    ".raw",   # Raw Image File
    ".ico",   # Icon File
    ".psd",   # Photoshop Document
    ".ai",    # Adobe Illustrator
    ".eps",   # Encapsulated PostScript
    ".indd",  # Adobe InDesign
]

DOCUMENTS_FORMAT = [
    ".doc",    # Microsoft Word Document
    ".docx",   # Microsoft Word Open XML Document
    ".pdf",    # Portable Document Format
    ".txt",    # Plain Text File
    ".rtf",    # Rich Text Format
    ".odt",    # OpenDocument Text Document
    ".ppt",    # Microsoft PowerPoint Presentation
    ".pptx",   # Microsoft PowerPoint Open XML Presentation
    ".xls",    # Microsoft Excel Spreadsheet
    ".xlsx",   # Microsoft Excel Open XML Spreadsheet
    ".csv",    # Comma-Separated Values
    ".md",     # Markdown File
    ".epub",   # Electronic Publication (eBook)
    ".pages",  # Apple Pages Document
    ".tex",    # LaTeX Source Document
    ".xml",    # Extensible Markup Language
    ".html",   # HyperText Markup Language
    ".ods",    # OpenDocument Spreadsheet
    ".odp",    # OpenDocument Presentation
    ".tsv",    # Tab-Separated Values
]

COMPRESSED_FORMAT = [
    ".zip",    # ZIP Archive
    ".rar",    # RAR Archive
    ".7z",     # 7-Zip Archive
    ".tar",    # Tape Archive
    ".gz",     # Gzip Compressed Archive
    ".bz2",    # Bzip2 Compressed Archive
    ".xz",     # XZ Compressed Archive
    ".iso",    # Disk Image File
    ".dmg",    # Apple Disk Image
    ".tgz",    # Gzipped Tar File
    ".tbz2",   # Bzip2 Tar File
    ".z",      # Unix Compress File
    ".lz",     # Lzip Compressed File
    ".cab",    # Cabinet File (Windows)
    ".arj",    # ARJ Compressed Archive
]

FOLDERS = {"Audios":AUDIO_FORMAT,"Videos":VIDEO_FORMAT,"Compressed Files":COMPRESSED_FORMAT,"Images":IMAGE_FORMAT,"Documents":DOCUMENTS_FORMAT}
PATH= "/home/burhan/Downloads/"


def create_folders(folder_names:dict,path:str):
    if os.path.exists(path):
        folders_paths = {}
        for folder in folder_names:
            folder_path = os.path.join(path,folder)
            folders_paths[folder_path] = folder_names[folder]
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
        return folders_paths
    else:
        raise FileNotFoundError("Path does not exists")

def listFiles(path):
    listdir = os.listdir(path)
    # print(listdir)
    files = []
    for i in listdir:
        file = os.path.splitext(i)
        if file[1] != "":
            files.append(file)
    return files

def sortFiles(files:list[tuple],folder_path:dict[str:list],path:str):
    sorted_files = []
    for i in files:
        # print(i)
        for j in folder_path:
            # print(j)
            if i[1] in folder_path[j]:
                org_file_path = os.path.join(path,i[0]+i[1])
                file_path = os.path.join(j,i[0]+i[1])
                count =1
                while os.path.exists(file_path):
                    file_path=os.path.join(j,i[0]+count+i[1])
                if os.path.exists(org_file_path):
                    os.rename(org_file_path,file_path)
                    sorted_files.append(file_path)
    return sorted_files




def main():
    folder_paths = create_folders(FOLDERS,PATH) #Create Folders
    files = listFiles(PATH)  #List only files
    sorted_files=sortFiles(files,folder_paths,PATH)
    print(sorted_files)
main()
