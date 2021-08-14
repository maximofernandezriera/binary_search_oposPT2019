def binary_search(list, item):
  # low and high keep track of which part of the list you'll search in.
  low = 0
  high = len(list) - 1

  # While you haven't narrowed it down to one element ...
  while low <= high:
    # ... check the middle element
    mid = (low + high) // 2
    guess = list[mid]
    # Found the item.
    if guess == item:
      return mid
    # The guess was too high.
    if guess > item:
      high = mid - 1
    # The guess was too low.
    else:
      low = mid + 1

  # Item doesn't exist
  return None

# Below line read inputs from user using map() function  
my_list = list(map(int,input("\nEnter 50 numbers : ").strip().split()))[:50]

#146 161ºº 193 217 266 276 460 487 585 756 842 889 954 985 1061 1114 1169 1256 1509 1533 1680 1829 1917 1995 2013 2085 2134 2182 2249 2261 2306 2499 2543 2723 2731 3196 3253 3271 3351 3514 3557 3629 3755 3884 3935 4163 4236 4296 4298 4420 4661 4764 4901 4912 4943 5043 5224 5247 5444 5485 5569 

print (binary_search(my_list, 756)) # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print (binary_search(my_list, 3)) # => None