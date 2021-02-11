'''
#1 - Sort 10 schools around your house by distance:
Insertion sort
    - fast on small sorts
    - easy to code
    - space complexity O(1)
    - potentially already somewhat sorted

#2 - eBay sorts listings by the current Bid amount:
radix or counting sort
    - number between $1-$500 or so
    - numbers, fixed length of integers
    - always a number within a certain range

#3 - Sport scores on ESPN
Quick sort
    - data probably varied, different types
    - smaller space demand for in-memory sorting
    - most efficient, worst case not likely
    - Merge sort too much

#4 - Massive database (can't fit all into memory) needs to sort through past year's user data
Merge sort
    - doesn't fit in memory
    - sort externally
    - data so big, worried about performance

#5 - Previously sorted Udemy review data needs to update and add 2 new reviews
Insertion sort

#6 - Temperature Records for the past 50 years in Canada
radix/counting sort
    - Integer numbers between small range
    - If numbers have decimal places, quick sort for in memory sorting

#7 - Large user name database needs to be sorted. Data is very random.
Merge sort
    - If enough memory
Quick sort
    - If not that large and not so worried about worst case

#8 - You want to teach sorting for the first time
Bubble sort & selection sort
'''