
final_output = []
def to_string(input):
    final_output.append(''.join(input))

def permute(input, l, r):
    if l == r:
        to_string(input)

    else:
        for i in range(l, r+1):
            input[l], input[i] = input[i], input[l]
            permute(input, l+1, r)
            input[l], input[i] = input[i], input[l]

permute(list('aba'),0, 2)
print final_output
print set(final_output)
