class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        one_step_back = 1
        two_steps_back = 1

        curr = 0

        for i in range(n-1):
            curr = one_step_back + two_steps_back
            two_steps_back = one_step_back
            one_step_back = curr
        
        return curr