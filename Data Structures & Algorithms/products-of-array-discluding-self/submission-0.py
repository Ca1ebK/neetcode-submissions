class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate products of everything to the left
        
        left_products = [1]
        left_product = 1
        for i in range(1, len(nums)):
            left_product *= nums[i-1]
            left_products.append(left_product)
        
        # calculate products of everything to the right

        right_products = [1]
        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i+1]
            right_products.append(right_product)
        
        right_products.reverse()

        res = []
        for i in range(len(nums)):
            res.append(left_products[i] * right_products[i])
        
        return res