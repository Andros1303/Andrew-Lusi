def count_positives_sum_negatives(arr):
    pos = []
    neg = []
    rslt = []
     if arr:
        for x in arr:
            if x>0:
                pos.append(x)
            else:
                neg.append(x)
        if pos.count(0) == len(pos):
            ps = 0
        else:
            ps = len(pos)
                  rslt.append(ps)
        rslt.append(sum(neg))
         return rslt
# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of 
# negative numbers.
# If the input array is empty or null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].