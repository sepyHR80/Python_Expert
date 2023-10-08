
def WaterV(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    

    while left < right :

        witdth = right - left

        h = min(height[left], height[right])

        max_area = max (witdth*h,max_area)

        if height[left] < height[right]:
            left += 1
        else :
            right -=1
        
    
    return max_area


print(WaterV([1,8,6,2,5,4,8,3,7]))