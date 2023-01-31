

import re
import sys


sys.stdout = open("compile_commands.json", "w+")

with open("makeout", 'r+') as fp:
    text = fp.read()
compile_commands = re.findall("(gcc.+)\n", text)
compile_commands = [cmd for cmd in compile_commands if '.c' in cmd]

print("[")

for (idx, line) in enumerate(compile_commands):
    if line.find(">") != -1:
        line = line[:line.find(">")]
    command = line
    seqs = command.split()
    for seq in seqs:
        if seq.endswith(".c"):
            file = seq
            break

    if re.search(r"-o .+?\.lo", command):
        continue
    print("\t{")
    print('\t\t"directory": "/root/gcc/openmp",')
    print('\t\t"command": "' + command + '",')
    print('\t\t"file": "' + seq + '"')
    print("\t},")

print("]")

