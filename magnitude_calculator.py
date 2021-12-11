# 05/20/2021
# Executes the conversion between the appearent and absolute
# magnitudes

# m (lower case) is the appearent 
# M (upper case) is the absolute magnitude
# d = distance in pc
import numpy as np
def app_to_abs(m, d):
    M = m-(5*np.log10(d/10))
    return M
def abs_to_app(M, d):
    m = M+(5*np.log10(d/10))
    return m

def Mpc_to_pc(d_mpc):
    return d_mpc*10**6
d = print(Mpc_to_pc(68.674))
#print(d)
print('absolute magnitude is:', '{:.2f}'.format(app_to_abs(18.179000854492188, Mpc_to_pc(85.5066))))
#print('appearent magnitude is :', '{:.2f}'.format(abs_to_app(-7.1, 276.1)))