import math

def recursive_power_set(seq):
    if seq:
        head, tail = seq[:1], seq[1:]
        for smaller in recursive_power_set(tail):
            yield smaller
            yield head + smaller
    else:
        yield []

def print_power_set(list, list_size):
    power_set_size = int(math.pow(2, list_size))
    total_power_set = []
    for counter in range(0, power_set_size):
        for j in range(0, list_size):
            if counter & (1 << j) > 0:
                #print str(list[j]),
                total_power_set[-1].append(list[j])
        #print ""
        total_power_set.append([])
    print total_power_set


def main():
    #for s in recursive_power_set([1,2,3]):
    #    print s
    print_power_set([1,2,3],3)

main()