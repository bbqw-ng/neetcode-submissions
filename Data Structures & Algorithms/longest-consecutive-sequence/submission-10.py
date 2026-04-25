class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #covers edge case of empty array
        if not nums:
            return 0
        #removes duplicates with set, then turn it back into list to use array accessing methods, saves us the dupe checking
        sorted_nums = sorted(set(nums))
        print(sorted_nums)
        longest = 1
        #keeps track of consecutive nums (should always be one aside from empty input)
        tracker = 1
        #this the the element before j (two pointer, j is looking 1 ahead)
        i = 0
        while i < len(sorted_nums) - 1:
            print("iteration: ", i)
            #this the second pointer(the one looking ahead)
            j = i + 1
            #checks to see if number is consec
            print("current number we are looking at ", sorted_nums[i])
            print("number that is after ", sorted_nums[j])
            if sorted_nums[i] + 1 == sorted_nums[j] or sorted_nums[i] -1 == sorted_nums[j]:
                print("accepted:", sorted_nums[i])
                print("------")
                tracker += 1
                if tracker > longest: 
                    longest = tracker
            #covers the case for the ending number
            elif sorted_nums[j] - 1 == sorted_nums[i] or sorted_nums[j] + 1 == sorted_nums[i]:
                #increments the counter for the last element in the consecutive list
                print("accepted ", sorted_nums[j])
                tracker += 1
            else:
                #if the next is not consecutive, reset the tracker 
                tracker = 1
            i += 1
        
        return longest
        
        