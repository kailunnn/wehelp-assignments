# 第一題
def calculate(min, max):
    sum = 0
    for n in range(min,max+1):
        sum+=n
    print(sum)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

# 第二題
def avg(data):
    count = data["count"]
    salarys = 0
    for salary in data["employees"]:
        salarys  += salary["salary"]
    avgSalary = salarys / count
    print(avgSalary)      

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
}) # 呼叫 avg 函式

# 第三題
def maxProduct(nums):
    # 找出所有乘積結果
    list = []
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            list.append(nums[i]*nums[j])
    # print(list)
    # 找出最大值
    maxNum = None
    for num in list:
        if(maxNum == None or num > maxNum):
            maxNum = num
    print(maxNum)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1,-2,0]) # 得到 2

# 第四題
def twoSum(nums, target):
    result = []
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i] + nums[j] == target):
                result.append(i)
                result.append(j)
                return(result)

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# 第五題
def maxZeros(nums):
    count = 0
    maxCount = 0
    for num in nums:
        if(num == 0):
            count += 1
            maxCount = max(count,maxCount)
        else:
            count = 0
    print(maxCount)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3