

def find_largest_consecutive(nums):
    if nums == []: return 0
    nums = list(set(nums))
    nums.sort()
    count = 1
    lrg = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            count +=1
            lrg  =  max(count,lrg)
        else:
            count = 1
    return lrg

if __name__ == "__main__":
    print (find_largest_consecutive([100,1,200,2,300,3]))
