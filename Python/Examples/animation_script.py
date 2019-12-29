from self_assembling import FCW_model

L = 100
rho = 0.5

l = 8

t = 10**3

model = FCW_model(L, l, rho)

model.animate(t)