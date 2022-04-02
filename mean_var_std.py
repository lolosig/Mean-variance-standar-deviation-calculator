import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("list must contain nine numbers")
  
  numlist = np.array(list)
  
  print(numlist)
  
  mean_rows = [numlist[[0,1,2]].mean(), numlist[[3,4,5]].mean(), 
  numlist[[6,7,8]].mean()]
  mean_columns = [numlist[[0,3,6]].mean(), 
  numlist[[1,4,7]].mean(), numlist[[2,6,8]].mean()] 
  
  
  var_rows = [numlist[[0,1,2]].var(), numlist[[3,4,5]].var(), 
  numlist[[6,7,8]].var()]
  var_columns = [numlist[[0,3,6]].var(), numlist[[1,4,7]].var(), 
  numlist[[2,6,8]].var()]
  
  std_rows = [numlist[[0,1,2]].std(), numlist[[3,4,5]].std(), 
  numlist[[6,7,8]].std()]
  std_columns = [numlist[[0,3,6]].std(), numlist[[1,4,7]].std(), 
  numlist[[2,6,8]].std()]

  max_rows = [numlist[[0,1,2]].max(), numlist[[3,4,5]].max(), 
  numlist[[6,7,8]].max()]
  max_columns = [numlist[[0,3,6]].max(), numlist[[1,4,7]].max(), 
  numlist[[2,6,8]].max()]

  min_rows = [numlist[[0,1,2]].min(), numlist[[3,4,5]].min(), 
  numlist[[6,7,8]].min()]
  min_columns = [numlist[[0,3,6]].min(), numlist[[1,4,7]].min(), 
  numlist[[2,6,8]].min()]

  sum_rows = [numlist[[0,1,2]].sum(), numlist[[3,4,5]].sum(), 
  numlist[[6,7,8]].sum()]
  sum_columns = [numlist[[0,3,6]].sum(), numlist[[1,4,7]].sum(), 
  numlist[[2,6,8]].sum()]


  return {
  'mean': [mean_columns, mean_rows, numlist.mean()],               
  'variance': [var_columns, var_rows,numlist.var()],            
  'standard deviation': [std_columns, std_rows, numlist.std()],
  'max': [max_columns, max_rows, numlist.max()],                   
  'min': [min_columns, min_rows, numlist.min()],
  'sum': [sum_columns, sum_rows, numlist.sum()]
  }