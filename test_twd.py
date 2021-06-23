from twd import TWD

dt = [["n","y","high","y"],
      ["y","n","high","y"],
      ["y","y","very high","y"],
      ["n","y","normal","n"],
      ["y","n","high","n"],
      ["n","y","very high","y"]]

o3wd = TWD(dt,["Headache","Muscle Pain","Temperature"])

print("U => ",o3wd.getU())
print("X={x| Flu(x)=y} =>",o3wd.getX("y"))
print("Va(Headache)",o3wd.getVa("Headache"))
print("Va(Muscle Pain)",o3wd.getVa("Muscle Pain"))
print("Va(Temperature)",o3wd.getVa("Temperature"))
print("Vd",o3wd.getVd())
print("Va",o3wd.getVa())
print("IND(A)",o3wd.getIND())
print("IND(Headache)",o3wd.getIND(["Headache"]))
print("IND(Headache,Muscle Pain)",o3wd.getIND(["Headache","Muscle Pain"]))
print("IND(Muscle Pain)",o3wd.getIND(["Muscle Pain"]))
print("IND(Temperature)",o3wd.getIND(["Temperature"]))
print("IND(Headache,Temperature)",o3wd.getIND(["Headache","Temperature"]))
print("lowerXA =>",o3wd.getLowerAX(o3wd.getX("y"),o3wd.getIND()))
print("upperXA =>",o3wd.getUpperAX(o3wd.getX("y"),o3wd.getIND()))
print("POS(X)",o3wd.getPOSX(o3wd.getX("y"),o3wd.getIND()))
print("BND(X)",o3wd.getBNDX(o3wd.getX("y"),o3wd.getIND()))
print("NEG(X)",o3wd.getNEGX(o3wd.getX("y"),o3wd.getIND()))
print("Precision of Approximation: ",o3wd.precision(o3wd.getX("y"),o3wd.getIND()))
print("Quality of Approximation: ",o3wd.quality(o3wd.getX("y"),o3wd.getIND()))
print("Roughness: ",o3wd.roughness(o3wd.getX("y"),o3wd.getIND()))
print("")
print("Rules")
print(o3wd.getRules(o3wd.getPOSX(o3wd.getX("y"),o3wd.getIND())))
print("")
print("Reduction:",o3wd.getReduct())
