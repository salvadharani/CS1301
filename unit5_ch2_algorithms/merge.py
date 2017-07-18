#Recall in 5.2.4 Worked Example 1, we gave you the code for
#merge_sort. You may copy that code into this problem and
#modify it. Change it such that instead of sorting from
#lowest to highest, it sorts from highest to lowest.
#
#Name your function merge_sort(). For example, if you call
#merge_sort([5, 3, 1, 2, 4]), you would get [5, 4, 3, 2, 1].
#
#Do not use Python's sort or reverse methods to complete
#this.


#Write your code below!

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        midpoint = len(lst) // 2
        left = merge_sort(lst[:midpoint])
        right = merge_sort(lst[midpoint:])
        newlist = []
        while len(left) and len(right) > 0:
            if left[0] < right[0]:
                newlist.append(right[0])
                del right[0]
            else:
                newlist.append(left[0])
                del left[0]
        newlist.extend(right)
        newlist.extend(left)
        return newlist

#The code below will test your function. If it works, this
#will print [5, 3, 1, -1, -3, -5].
print(merge_sort([1, 3, -1, -3, -5, 5]))


