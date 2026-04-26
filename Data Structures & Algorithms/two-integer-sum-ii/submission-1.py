class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while i <= len(numbers)-1 :
            print("first pointer: ", i, numbers[i])
            j = i + 1
            find = target - numbers[i]
            print("this is the target num: ", find)
            while j <= len(numbers)-1:
                print("current number we are looking at: ", j, numbers[j])
                if numbers[j] == find:
                    print("we found the target: ", i, numbers[i], " :" ,j, numbers[j])
                    return [i+1, j+1]
                j += 1
            i += 1

        