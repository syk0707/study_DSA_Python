#N integers are given. At this time, write a program to find the minimum and maximum values.
def get_max_min():
    length = input()
    numbers = list(map(int, input().split()))

    min = numbers[0]
    max = numbers[0]

    for number in numbers:
        if(min > number):
            min = number
        elif(max < number):
            max = number
    print(min, max)

#When nine different natural numbers are given, write a program to find the maximum value of these and find out what number the maximum number is.
def get_max():
    numArray = []
    for i in range(9):
        numInput = input()
        numInput = int(numInput)
        numArray.append(numInput)
    max = numArray[0]
    maxIdx = 1
    idx = 0
    for number in numArray:
        idx = idx + 1
        if(max < number):
            max = number
            maxIdx = idx
    print(max)
    print(maxIdx)

# Write a program that asks how many times each number from 0 to 9 was written in the result of calculating A × B × C given three natural numbers A, B, and C.
def get_number():
    numArray = []
    for i in range(3):
        numInput = input()
        numInput = int(numInput)
        numArray.append(numInput)

    totalNum = 1

    for number in numArray:
        totalNum = totalNum * number

    a = {}
    for j in range(10):
        a[j] = 0

    for k in str(totalNum):
        k = int(k)
        a[k] = a[k] + 1
        
    for value in a.values():
        print(value)

#After receiving 10 inputs, divide them by 42 to find the remainder. Then write a program that prints out how many different values there are.
def get_reminder():
    numArray = []
    for i in range(10):
        numInput = input()
        numInput = int(numInput)
        numArray.append(numInput % 42)

    a = {}

    for k in numArray:
        if a.get(k) is None:
            a[k] = 1

    print(len(a))

#He decided to manipulate the score and take it home. For now, he chose the highest among his scores. This value is called M. All scores were then corrected to a score/M*100. When calculating his grades in a new way above, write a program to get a new average.
def get_average():
    i = int(input())
    numArray = input().split()

    maxScore = 0
    totalScore = 0

    for k in numArray:
        k = int(k)
        if(maxScore < k):
            maxScore = k

    for k in numArray:
        k = int(k)
        totalScore = totalScore + (k / maxScore) * 100
        
    print(totalScore / i)

#There are results from OX quizzes such as "OOOXXO". O is the correct answer, and X is the wrong answer. If a question is answered, the score of the question is the number of consecutive Os to the question. For example, question 3 has a score of 3. At this time, write a program to get points.
def get_ox_score():
    i = int(input())
    oxArray = {}
    for a in range(i):
        oxArray[a] = input()
        
    for oxValue in oxArray.values():
        correctNum = 0
        totalScore = 0
        for oxStr in oxValue:
            if(oxStr == "O"):
                correctNum = correctNum + 1
                totalScore = totalScore + correctNum
            else:
                correctNum = 0
        print(totalScore)

if __name__ == "__main__":
    #get_max_min()
    #get_max()
    #get_number()
    #get_reminder()
    #get_average()
    get_ox_score()