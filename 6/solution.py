input = open('input.txt', 'r').readline()

def find_hdr(hdr_len):
    for i in range(3, len(input)):
        str = ""
        for j in range(hdr_len):
            if input[i + j] in str:
                break
            str += input[i + j]
        if len(str) == hdr_len:
            return i + len(str)          

print(f"Solution A: {find_hdr(4)}")
print(f"Solution B: {find_hdr(14)}")