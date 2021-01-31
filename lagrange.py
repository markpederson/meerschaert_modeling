# Lagrange example

import sympy as sp
x, y, z, l1, l2 = sp.symbols('x y z l1 l2')

f = x + 2*y + 3*z

g1 = x**2 + y**2 + z**2
c1 = 3

g2 = x
c2 = 1

df_dx = sp.diff(f, 'x')
df_dy = sp.diff(f, 'y')
df_dz = sp.diff(f, 'z')

dg1_dx = sp.diff(g1, 'x')
dg1_dy = sp.diff(g1, 'y')
dg1_dz = sp.diff(g1, 'z')

dg2_dx = sp.diff(g2, 'x')
dg2_dy = sp.diff(g2, 'y')
dg2_dz = sp.diff(g2, 'z')

sols = sp.solve_poly_system([
      df_dx - l1*dg1_dx + l2*dg2_dx,
      df_dy - l1*dg1_dy + l2*dg2_dy,
      df_dz - l1*dg1_dz + l2*dg2_dz,
      g1 - c1,
      g2 - c2
    ], x, y, z, l1, l2)

for i in range(0, len(sols)):
  print(i, sols[i][0:3], f.evalf(subs={x:sols[i][0], y:sols[i][1], z:sols[i][3]}))