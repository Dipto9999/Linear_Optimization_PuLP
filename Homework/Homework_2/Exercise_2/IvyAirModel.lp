\* Ivy_Air_Problem *\
Maximize
Total_Revenue_of_Ivy_Air: 280 Ithaca_Boston_B + 140 Ithaca_Boston_M
 + 360 Ithaca_Boston_Y + 220 Ithaca_Newark_B + 100 Ithaca_Newark_M
 + 300 Ithaca_Newark_Y + 130 Newark_Boston_B + 80 Newark_Boston_M
 + 160 Newark_Boston_Y
Subject To
Ithaca_Boston_B_Potential_Customers: Ithaca_Boston_B <= 10
Ithaca_Boston_M_Potential_Customers: Ithaca_Boston_M <= 18
Ithaca_Boston_Y_Potential_Customers: Ithaca_Boston_Y <= 3
Ithaca_Newark_B_Potential_Customers: Ithaca_Newark_B <= 8
Ithaca_Newark_M_Potential_Customers: Ithaca_Newark_M <= 22
Ithaca_Newark_Y_Potential_Customers: Ithaca_Newark_Y <= 4
Newark_Boston_B_Potential_Customers: Newark_Boston_B <= 13
Newark_Boston_M_Potential_Customers: Newark_Boston_M <= 20
Newark_Boston_Y_Potential_Customers: Newark_Boston_Y <= 8
Seating_Limit_1: Ithaca_Boston_B + Ithaca_Boston_M + Ithaca_Boston_Y
 + Ithaca_Newark_B + Ithaca_Newark_M + Ithaca_Newark_Y <= 30
Seating_Limit_2: Ithaca_Boston_B + Ithaca_Boston_M + Ithaca_Boston_Y
 + Newark_Boston_B + Newark_Boston_M + Newark_Boston_Y <= 30
Bounds
0 <= Ithaca_Boston_B
0 <= Ithaca_Boston_M
0 <= Ithaca_Boston_Y
0 <= Ithaca_Newark_B
0 <= Ithaca_Newark_M
0 <= Ithaca_Newark_Y
0 <= Newark_Boston_B
0 <= Newark_Boston_M
0 <= Newark_Boston_Y
Generals
Ithaca_Boston_B
Ithaca_Boston_M
Ithaca_Boston_Y
Ithaca_Newark_B
Ithaca_Newark_M
Ithaca_Newark_Y
Newark_Boston_B
Newark_Boston_M
Newark_Boston_Y
End
