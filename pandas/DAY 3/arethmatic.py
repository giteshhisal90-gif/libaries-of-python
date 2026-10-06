import pandas as pd 

var = pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})

var["C"] = var["A"]+var["B"]
# similarly we can prform other operations like
# Addition
# Subtraction
# multiplication
# Division

# if c is greter than or equal 10 make true

var[">=10"] = var["C"]>=10

print(var)