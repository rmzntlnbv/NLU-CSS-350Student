# Install needed library
pip install ucimlrepo

# Python code
from ucimlrepo import fetch_ucirepo 
import pandas as pd
  
# fetch dataset adult file is id = 2
adult = fetch_ucirepo(id=2) 
  
df = pd.DataFrame(adult.data.targets, columns=adult.data.features)
df.to_csv("../data/adults_student.csv")

# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 
  
# metadata 
print(adult.metadata) 
  
# variable information 
print(adult.variables) 

