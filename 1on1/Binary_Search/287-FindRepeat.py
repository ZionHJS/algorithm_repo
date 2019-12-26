left, right = 0, len(nums) - 1
   while left < right:
        mid = (left + right) // 2
        if sum(n <= mid for n in nums) > mid:
            right = mid
        else:
            left = mid + 1
    return left


# if not nums:
            # return -1
        # tmp_num = nums[0]
        # for i in range (len(nums)):
            # tmp_num = nums[i]
            # for j in range(i+1, len(nums)):
                # if nums[j] == tmp_num:
                    # return tmp_num
                # else:
                    # pass
        # return -1

        if not nums:
            return -1
        
        left, right = 1, len(nums)-1
        
        count = 0
        
        while left+1 < right:
            mid = left + (right-left)//2
            for i in range(len(nums)):
                if nums[i] < mid:
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    left = mid 
                else:
                    right = mid
        
        count = 0 
        for j in range(0, len(nums)):
            if nums[j] == nums[right]:
                count += 1

        if count > 1:
            return nums[right]
        else:
            return nums[left]
