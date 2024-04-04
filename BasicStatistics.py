nums = [0,0,0,0,0.1,0.1,0.1,0.1,0.2,0.2,0.2,0.3,0.3,0.3,0.4,0.5,0.5,0.6,0.8,0.9,1.0,1.2,1.4,1.5,1.7,2.0,3.2,3.5,4.1,4.3,4.8,5.0,5.6,5.9,6.0,6.4,7.7,8.2,8.6,9.3,9.7,9.9,11.0,11.5,12.2,12.7,14.0,16.6,17.8]
nums.sort()

length = len(nums)
if (length % 2 == 0):
    median = (nums[(length)//2] + nums[(length)//2-1]) / 2
else:
    median = nums[(length-1)//2]

print(median)

mean = sum(nums)/length
print(mean)
print(nums)
