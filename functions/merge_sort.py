def mergeSort(l):
    length = len(l)
    if length <= 1: return l
    l1 = l[:length//2]
    l2 = l[length//2:]
    return merge(mergeSort(l1), mergeSort(l2))

def merge(l1, l2):
    if l1 == []: return l2
    if l2 == []: return l1
    if l1[0] <= l2[0]:
        return l1[:1] + merge(l1[1:], l2)
    return l2[:1] + merge(l1, l2[1:])
