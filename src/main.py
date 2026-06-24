import os
import shutil
import sys
from gencontent import generate_page, generate_pages_recursive


dir_path_content = "./content"
template_path = "./template.html"
dir_path_static = "./static"
dir_path_public = "./docs"

def copy_directory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copying {src_path} to {dst_path}")
        else:
            copy_directory(src_path, dst_path)


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'
    copy_directory("static", "docs")
    print("Generating pages...")

    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

    
if __name__ == "__main__":
    main()
