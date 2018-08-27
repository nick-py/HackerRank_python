n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


n = int(raw_input())
marks = [[raw_input(), float(raw_input())] for i in  xrange(n)]
scores = sorted({s[1] for s in marks})
result = sorted(s[0] for s in marks if s[1] == scores[1])
print '\n'.join(result)


minv = min(n for n in scores if n!=scores[0])

result = sorted(s[0] for s in marks if s[1] == minv)

