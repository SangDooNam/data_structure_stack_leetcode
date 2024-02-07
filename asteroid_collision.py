class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        stack = []
        for asteroid in asteroids:
            
            while stack and asteroid < 0 < stack[-1]:
                
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                if stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        
        return stack
    


sol = Solution()

asteroids = [5,10,-5]

asteroids = [8,-8]
asteroids = [10,2,-5]
print(sol.asteroidCollision(asteroids))






