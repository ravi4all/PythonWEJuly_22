# lambda x,y : x + y

temp = [34.4,40.3,35.6,33.5,29.6,36.7,33.6]
f = list(map(temp, lambda c : 9/5 * c + 32))

kms = [23,5,6,7,3,2,672]
ms = list(map(kms, lambda km : km * 1000))
