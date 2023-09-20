def biggest_and_smallest(nums):
    # empty array to put biggest and smallest number into
    big_small = []
    # set to values in array, so that you don't set them to values that would be the smallest/biggest
    biggest = nums[0]
    smallest = nums[0]
    # go through each number in array, replacing biggest and smallest if needed
    for num in nums:
        if num < smallest:
            smallest = num
        elif num > biggest:
            biggest = num
    # append biggest and smallest to array after loop gone through
    big_small.append(smallest)
    big_small.append(biggest)
    # no need to return, just print since we aren't doing anything else with the array
    print(big_small)


def generate_array():
    # empty array to enter numbers into
    nums = []
    # condition to be set to true when finished entering numbers
    finished_array = False
    while finished_array == False:
        # keep adding numbers until user enters something that isn't a number
        try:
            num = int(
                input("Enter a number to add to the array, if finished, enter anything else: "))
            nums.append(num)
        except Exception:
            finished_array = True
            continue
    # return array to be inputted into the min and max function
    return nums


def main():
    nums = generate_array()
    print("Your minimum and maximum number in the array:")
    biggest_and_smallest(nums)


main()
