class Solution:
    def findMajority(self, arr):
        # Recursive function to find the majority element in a given segment

        def majorityRec(start, end):
            # Base case: if the segment contains only one element
            if start == end:
                return arr[start]

            # Find the middle index of the current segment
            mid = (end + start) // 2

            # Recursively find the majority element in the left and right halves
            leftMajority = majorityRec(start, mid)
            rightMajority = majorityRec(mid + 1, end)

            # If both halves agree on the majority element, return it
            if leftMajority == rightMajority:
                return leftMajority

            # Count the occurrences of the left and right majority elements in the current segment
            leftCount = arr[start:end + 1].count(leftMajority)
            rightCount = arr[start:end + 1].count(rightMajority)

            # Return the element with the higher count in the current segment
            return leftMajority if leftCount > rightCount else rightMajority

        # Function to initiate the divide and conquer algorithm
        return majorityRec(0, len(arr) - 1)


# Test the algorithm with three different inputs
sol = Solution()
print(sol.findMajority([1, 2, 2, 3, 2])) # Expect 2
print(sol.findMajority([4, 4, 4, 4, 7, 4, 4])) # Expect 4
print(sol.findMajority([9, 9, 1, 1, 9, 1, 9, 9])) # Expect 9
