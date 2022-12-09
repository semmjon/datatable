import os
import re

source_dir = "dist"
target_dir = "dist"
# print(os.getcwd())
os.makedirs(target_dir, exist_ok=True)
artifacts_file = os.listdir(source_dir)
user = os.environ["USER"]
pattern = f"(a0[+](sdist|build)[.][0-9].*[.]{user})"

for file in artifacts_file:
    os.rename(os.path.join(source_dir, file), os.path.join(target_dir, re.sub(pattern, "", file.replace("linux", "manylinux"))))
