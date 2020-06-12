t = [1, 2, 3, 4, 5]
sub_array = [[]]
for i in range(len(t)):
    for j in range(i, len(t)+1):
        if len(t[i:j]) != 0:
            sub_array.append(t[i:j])

print "Sub array of {} is {}".format(t, sub_array)