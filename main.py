import os

from System.Lib import nul, Console
from System.Dumpsc import process_sc, decompress_data
from System.Decode import decode_sc, cut_sprites
from pathlib import Path

def get_files():
    all_files = os.listdir("./")
    if (len(all_files) < 3):
        Console.error('Files not found')
        return

    files = []
    for file in all_files:
        match file.endswith():
            case ".ktx":
                Console.info("Find file, which ends with .ktx")
                ktx_file()
            case ".zktx":
                Console.info("Find file, which ends with .zktx")
            case 
    if (len(files) < 1):
        Console.warn('No valid files found !!!')
        return
    
    return files
def ktx_file():
    try:
        get_do = input("What to do with the ktx file?")
        Console.info("1. Convert ktx to zktx")
        Console.info("2. Convert ktx to png")
    except:
        Console.warn("Int count!")
        exit()
    
def extract_images():
    # Getting files
    files = get_files()
    if files is None: return

    for file in files:
        if file.endswith('_tex.sc'):
            sc_file = file[:-7] + ".sc"
            sc_file_name = sc_file[:-3]
            
            # Creating Sub directory for specified file
            sc_output_dir = f"{sc_file_name}"

            with open(f"{file}", "rb") as f:
                print('')
                Console.info(f"Processing {file}")
                # extracting texture
                images = process_sc(f"{sc_file_name}_tex", f.read(), f"{sc_output_dir}", True)

            if sc_file not in files:
                Console.warn(f"{sc_file} not found! Will skip cutting images")
                continue
            
            Console.info(f"Processing {sc_file}")
            with open(f"{sc_file}", "rb") as f:
                data = decompress_data(f.read(), sc_file_name)                
                sprite_globals, sprite_data,sheet_data = decode_sc(data, sc_file_name)
                cut_sprites(sprite_globals, sprite_data, sheet_data, images, f"{sc_output_dir}")

            Console.success(f"Successfully extracted textures for {sc_file_name}")


if __name__ == '__main__':
    # Verifying and creating necessary directories
    
    # main task
    extract_images()
