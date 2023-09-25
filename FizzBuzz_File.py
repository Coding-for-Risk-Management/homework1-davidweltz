

def FizzBuzz(start, finish):
    v=[]
    for i in range(start, finish+1):
        if i % 15== 0:
            v.append('fizzbuzz')
        elif i % 5 == 0:
              v.append('buzz')
        elif i % 3== 0:
              v.append('fizz')
        else:
            v.append(i)

    #v = ['buzz', 41, 'fizz', 43, 44, 'fizzbuzz']
    return(v)
