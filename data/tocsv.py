import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()

readRDS = robjects.r['readRDS']
df = readRDS('cumulative_2006_2017.Rds')
df = pandas2ri.ri2py(df)
df.to_csv("cumulative_2006_2017.csv", index=None)
