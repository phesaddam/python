i=float(raw_input("enter no "))
if i%3==0 and i%5==0:
      print("fiz and buzz")
elif i%5==0:
    print("buzz")
elif i%3==0:
    print("fiz")
else:
    print(i,"it does not satisfy any condition")
i+=1