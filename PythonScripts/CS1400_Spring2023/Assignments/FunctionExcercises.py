def avg(n1, n2):
    """Return average of two numbers
    Return a message is a non-number is passed"""
    try:
      return(n1 + n2) / 2
    except TypeError:
      return("Please use two numbers as parameters")


def odds_or_evens(my_bool, nums):
    """Returns all of the odd or
    even numbers from a list"""
    return_list = []
    for num in nums:
        if my_bool:
            if num % 2 == 0:
                return_list.append(num)
        else:
            if num % 2 != 0:
                return_list.append(num)

    return return_list