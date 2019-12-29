from self_assembling import FCW_model

L = 100
rho = 0.2

l = 8

t = 10**4

foldername = 'l_%i' % l

model = FCW_model(L, l, rho)

model.simulate(t, folder=foldername)