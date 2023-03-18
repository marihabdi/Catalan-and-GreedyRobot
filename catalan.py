#Mariama Abdi
#CSS 310
#Instructor Dimpsey



answer = 0

#function for computing nth catalan
def catalan(n): 

    if n > 0 :
        answer = 0; 
        for i in range(n):
        #catalan formula
            answer += catalan(i) * catalan(n - 1 - i)
        return answer;

    #if n is zero answer is one
    elif n == 0:
        return 1

value = int(input())
print(catalan(value))
