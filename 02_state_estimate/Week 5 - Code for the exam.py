import numpy as np

def sph_to_cart(epsilon, alpha, r):
    """
    Transform sensor readings to Cartesian coordinates in the sensor frames. 
    """
    p = np.zeros(3)  # Position vector 

    # Your code here
    x = r * np.cos(alpha) * np.cos(epsilon)
    y = r * np.sin(alpha) * np.cos(epsilon)
    z = r * np.sin(epsilon)
    
    p[0] = x
    p[1] = y
    p[2] = z

    return p
  
def estimate_params(P):
    
  P = np.array(P)
  
  param_est = np.zeros(3)
  
  ones_row = np.matrix(np.ones(len(P)))
  ones_column = ones_row.T
  
  x_row = (P[:,0])
  x_column = np.matrix(x_row).T
  y_row = (P[:,1])
  y_column = np.matrix(y_row).T
  z_row = (P[:,2])
  z_column = np.matrix(z_row).T
  
  A = np.hstack(((ones_column),(x_column),(y_column)))
  
  B = z_column
  
  #print(A)
  
  params = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(B)
  
  print(params)
  
  param_est[0] = params[0,0]
  param_est[1] = params[1,0]
  param_est[2] = params[2,0]
  
  return param_est