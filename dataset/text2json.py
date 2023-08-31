import json
import sys


INSTR = "### Instruction:"
INPUT = "### Input:"
OUTPUT = "### Output:"

def text2json(str1):
    ret = []
    found = str1.find(INSTR)
    while found >= 0:
        found_input = str1.find(INPUT)
        if found_input>=0:
            instruction = str1[found+len(INSTR)+1:found_input-1]
            found_output=str1.find(OUTPUT)
            if found_output >= 0:
               input = str1[found_input+len(INPUT)+1:found_output-1]
               found = str1[1:].find(INSTR)
               if found >= 0:
                   found += 1
                   output = str1[found_output+len(OUTPUT)+1:found-1]
                   str1 = str1[found:]
               else:
                   output = str1[found_output+len(OUTPUT)+1:]
               obj = {"instruction": instruction, "input":input, "output":output}
               ret.append(obj)
            else:
                break
        else:
            break
    return ret
    
def escape(jsonstr):
    return jsonstr.replace('"', '\\"').replace('\n', '\\n')

if __name__ == "__main__":
    filepath = sys.argv[1]
    dst = sys.argv[2]
    with open(filepath, 'r') as fp:
        content = fp.read()
        obj = text2json(content)
        print(f'records:{len(obj)}')
        print(obj[:1])
        with open(dst, 'w') as fp:
            fp.write(json.dumps(obj))
