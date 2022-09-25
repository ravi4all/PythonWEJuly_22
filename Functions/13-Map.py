def temp_convert(c):
    return 9/5 * c + 32

def km_to_m(km):
    return km * 1000

# f = temp_convert(23.34)
# print("Temp is :",f)

temp = [34.4,40.3,35.6,33.5,29.6,36.7,33.6]
# f = []
# for t in temp:
#     f.append(temp_convert(t))

# print("Temp is",f)

kms = [23,5,6,7,3,2,672]
# ms = []
# for k in kms:
#     ms.append(km_to_m(k))

# print(ms)

# def myConverter(iter, func):
#     data = []
#     for i in range(len(iter)):
#         data.append(func(iter[i]))
#     return data

# f = myConverter(temp, temp_convert)
# ms = myConverter(kms, km_to_m)

f = list(map(temp, temp_convert))
ms = list(map(kms, km_to_m))
