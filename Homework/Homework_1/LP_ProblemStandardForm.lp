\* LP_Problem_1.0_Standard_Form *\
Maximize
OBJ: - x_1 - 3 x_2_neg + 3 x_2_pos + x_3
Subject To
_C1: x_1 - x_2_neg + x_2_pos + x_3 <= 3
_C2: - x_1 + x_2_neg - x_2_pos - x_3 <= -3
_C3: - x_1 - x_2_neg + x_2_pos <= 1
_C4: x_1 >= 0
_C5: x_2_pos >= 0
_C6: x_2_neg >= 0
_C7: x_3 >= 0
End
