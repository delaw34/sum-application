
# Python program that sums up all the items in a list of 9 items
# remove duplicates
# sums up the list
# print the result


numbers = [12, 14, 16, 18, 20,10,12, 20]
remove_dul = set(numbers)
sum_total = sum(remove_dul)
print("this is total sum of all numbers after removing all duplicates", sum_total)
