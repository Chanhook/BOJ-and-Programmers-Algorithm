def solution(answers):
    answer = []
    
    l = len(answers)
    
    student1 = [1,2,3,4,5] * 2000  
    student2 = [2,1,2,3,2,4,2,5] * 1250
    student3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    maxcnt = 0
    for idx, student in enumerate([student1,student2,student3]):
        cnt = 0
        for stu, ans in zip(student,answers):
            if stu == ans:
                cnt +=1
        answer.append([idx+1,cnt])
        maxcnt = max(maxcnt,cnt)
    
    result = [x[0] for x in answer if x[1] >= maxcnt]
    
    return result


# def solution(answers):
#     def score(stu,answers):
#         cnt=0
#         for i in range(len(answers)):
#             if(stu[i]==answers[i]):
#                 cnt+=1
#         return cnt
        
        
        
#     l=len(answers)
#     student1=[1,2,3,4,5]*2000
#     student2=[2,1,2,3,2,4,2,5]*1250
#     student3=[3,3,1,1,2,2,4,4,5,5]*1000
    
#     stu1=student1[:l]
#     stu2=student2[:l]
#     stu3=student3[:l]
    
#     result1=score(stu1,answers)
#     result2=score(stu2,answers)
#     result3=score(stu3,answers)
    
#     if(result1>result2 and result1>result3):
#         answer = [1]
#     elif(result2>result1 and result2>result3):
#         answer=[2]   
#     elif(result3>result1 and result3>result2):
#         answer=[3]
#     elif(result1==result2 and result2>result3):
#         answer=[1,2]
#     elif(result1==result3 and result1>result2):
#         answer=[1,3]
#     elif(result2==result3 and result2>result1):
#         answer=[2,3]
#     elif(result1==result2 and result2==result3):
#         answer=[1,2,3]
    
          
#     return answer