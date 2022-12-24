formula = input()
formula_int = formula.split('-')

for i in range(len(formula_int)):
    x = formula_int[i].split('+')
    x = map(int, x)
    formula_int[i] = sum(x)

result = formula_int[0]
for i in range(1,len(formula_int)):
    result -= formula_int[i]

print(result)
