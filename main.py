a = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
b = True
L = []
first = []
second = []
third = []
fourth = []
for i in a:
   d = i.split(' ')
   c = [d[x:x+3] for x in range(0, len(d), 3)]
   L.extend(c)
first.extend(L[0])
second.extend(L[1])
third.extend(L[2])
fourth.extend(L[3])
for i,v,m,n in zip(first,second,third,fourth):
   if i == '+' and v == '-' and m == '+' and n == '-':
      t =('{:>4}'.format(int(first[0])),'+''{:>3}'.format(int(first[2])),('-'*len(first[0]) + '-'*len(first[1]) + '-'*len(' ')),'{:>4}'.format(int(first[0]) + int(first[2])))
      s =('{:>6}'.format(int(second[0])),'-''{:>5}'.format(int(second[2])),('-'*len(second[0]) + '-'*len(' ') + '-'*len(second[2])),'{:>6}'.format(int(second[0]) - int(second[2])))
      m =('{:>6}'.format(int(third[0])),'+''{:>5}'.format(int(third[2])),('-'*len(third[0]) + '-'*len(third[1]) + '-'*len(' ')),'{:>6}'.format(int(third[0]) + int(third[2])))
      n =('{:>5}'.format(int(fourth[0])),'-''{:>4}'.format(int(fourth[2])),('-'*len(fourth[0]) + '-'*len(fourth[2])),'{:>5}'.format(int(fourth[0]) - int(fourth[2])))
      for i,j,k,l in zip(t,s,m,n):
        def arithmetic_arranger(a,b):
                if len(a) > 5:
                   return "Error: Too many problems."
                elif b == False or b == None:
                   pass  
                for number in a:
                    if number == "*" or number == "/":
                        return "Error: Operator must be '+' or '-'."
                    elif (number.isalpha()) == True:
                        return "Error: Numbers must only contain digits."
                for p, f in enumerate(a):
                    num1, op, num2 = f.split()
                    if len(num1) > 4 or len(num2) > 4:
                        return "Error: Numbers cannot be more than four digits."
                    else:
                        pass                       
                return('{:8}{:10}{:10}{:10}'.format(i,j,k,l))     
        print(arithmetic_arranger(a,b))