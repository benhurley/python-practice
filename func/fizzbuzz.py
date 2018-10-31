# Two versions of fizz buzz solved two different ways in python

# Example also used to practice unit testing with unittest

def fizzbuzz(n):

    # make sure value being passed in is an integer
    if (not isinstance(n, int)):
        return -1

    # error check the value being passed in
    if (n < 0):
        n = 0

    #ans list
    ans = []

    for num in range(1,n+1):

        divisible_by_3 = (num % 3 == 0)
        divisible_by_5 = (num % 5 == 0)

        num_ans_str = ""

        if divisible_by_3:
            # Divides by 3
            num_ans_str += "Fizz"
        if divisible_by_5:
            # Divides by 5
            num_ans_str += "Buzz"
        if not num_ans_str:
            # Not divisible by 3 or 5
            num_ans_str = str(num)

        # Append the current answer str to the ans list
        ans.append(num_ans_str) 

    return ans


def fizzbuzzjazz(x):

    # make sure value being passed in is an integer
    if (not isinstance(x, int)):
        return -1

    # error check the value being passed in
    if (x < 0):
        x = 0

    return [("Fizz" if x % 3 == 0 else "") + ("Buzz" if x % 5 == 0 else "") + ("Jazz" if x % 7 == 0 else "") or str(x) for x in range(1,x+1)]

