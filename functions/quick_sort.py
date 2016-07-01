def myqsort(l):
    if l <= []:
        return l
    head = l[0]
    tail = l[1:]
    return myqsort([item for item in tail if item < head]) + [head] + myqsort([item for item in tail if item >= head])
