import Béka0

# CRF számítása

i = 0.05
T = 40
CRF =(i*(1+i)**T)/(((1+i)**T)-1)

# A tárolás teljes ktg.

FLH1 = 500
FLH2 = 1000
FLH3 = 2000

Capex1 = 1950
Capex2 = 2500
Capex3 = 3025

td = 6
P = 600



Cft = 4.6        # €/kW-year
Cvt = 0.22       # €/MWh

Cqmt_1 = Cft + Cvt * (FLH1 / 1000) # €/kW-year
Cqmt_2 = Cft + Cvt * (FLH2 / 1000) # €/kW-year
Cqmt_3 = Cft + Cvt * (FLH3 / 1000) # €/kW-year

# tárolás teljes ktg.

Ctot_1 = (Capex1*CRF+Cqmt_1)*1000/FLH1
Ctot_2 = (Capex2*CRF+Cqmt_2)*1000/FLH2
Ctot_3 = ((Capex3*CRF+Cqmt_3)*1000/FLH3)

# Energia tárolás határai

pc_max = 80
pd_max = 80
P = 600
eta = 0.8 # roundtrip efficiency