print("Welcome to the tip calculator")
total = float(input('what was the total bill?: '))
P_propine = int(input('what percentage tip would you like to give?: 10, 12 or 15: '))
N_personas = int(input('How many people to split the bill?: '))

P_Pagar_Prop = float(total * (P_propine/100))
T_Pagar = float(total + P_Pagar_Prop)
# print(P_Pagar_Prop)
# print(T_Pagar)

Result = (T_Pagar/N_personas)
New_Result = round(Result, 2)
print(f'Each person should pay: {New_Result}')
