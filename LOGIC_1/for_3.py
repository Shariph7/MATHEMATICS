# ADVANCE LOGIC,SETS AND REAL NUMBER SYTEM REPRESENTATION IN PYTHON for three sets.
import pandas as pd
def perform_operation(operation):
    df = pd.read_csv('data.csv')
    p, q, r = df['p'], df['q'], df['r']
    if operation == 'and':
        df['Answer'] = p & q & r
    elif operation == 'or':
        df['Answer'] = p | q | r
    elif operation == 'not':
        df['Negp'] = ~p
        df['Negq'] = ~q
        df['Negr'] = ~r
    elif operation == 'xor':
        df['XOR_P'] = p^q^r
    print(df)

print('AND\nOR\nNOT\n')
ins = input('Enter: ').casefold()
if ins in ['and', 'or', 'not','xor']:
    perform_operation(ins)
else:
    print("Invalid input.")