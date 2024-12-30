import os 

Path = os.path.dirname(os.path.abspath(__file__))

file_count, dirs, root = 0, 0, ""

for root, dirnames, filenames in os.walk(Path):
    print(f"Files: {filenames}")
    file_count += len(filenames)

print(f"Dirs: {dirs}")
print(f"Root: {root}")
print(f"Len of files: {file_count}")
