# ADVANCE LOGIC,SETS AND REAL NUMBER SYTEM REPRESENTATION IN PYTHON
import pandas as pd
def perform_operation(operation):
    df = pd.read_csv('datas.csv')
    p, q = df['p'], df['q']
    if operation == 'and':
        df['Answer'] = p & q
    elif operation == 'or':
        df['Answer'] = p | q
    elif operation == 'not':
        df['Negp'] = ~p
        df['Negq'] = ~q
    elif operation == 'xor':
        df['XOR_P'] = p^q
    print(df)

print('AND\nOR\nNOT\n')
ins = input('Enter: ').casefold()
if ins in ['and', 'or', 'not','xor']:
    perform_operation(ins)
else:
    print("Invalid input.")