import os
import re

source_dir = "dist"
target_dir = "dist"
# print(os.getcwd())
os.makedirs(target_dir, exist_ok=True)
artifacts_file = os.listdir(source_dir)
print(artifacts_file)
user = os.environ.get("USER", "")

for file in artifacts_file:
    source = os.path.join(source_dir, file)
    # target = os.path.join(target_dir, re.sub(f"^(.+)\\..+(-.+-.+-.+|.tar.gz)", "\\1\\2",
    #                                          re.sub(f"a0[+](sdist|build)[.][0-9]+", "",
    #                                                 file.replace("linux", "manylinux"))))
    target = os.path.join(target_dir, file.replace("linux", "manylinux"))
    print(f"Move {source} to {target}")
    os.rename(source, target)
