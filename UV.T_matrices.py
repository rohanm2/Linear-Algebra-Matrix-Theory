import numpy as np 

def calculateProducts(n, m, p): 
    U = np.random.rand(m, n) # creating U matrix with random values 
    V = np.random.rand(p, n) # creating V matrix with random values 
    
    # Method 1: U times V transpose 
    W_1 = np.matmul(U, V.T) 
    
    # Method 2: Sum of each column of U times each column of V transposed 
    W_2 = np.zeros((m, p)) 
    for i in range(0, n): # for loop handles the summation 
        W_2 += np.matmul(U[:, i].reshape(m, 1), V[:, i].T.reshape(1, p)) # handles the column products 
        
    return W_1, W_2 

W_1, W_2 = calculateProducts(10, 5, 8)   
print(np.allclose(W_1, W_2)) # Tests for equality between the products from the 2 methods 

W_3, W_4 = calculateProducts(4, 6, 2)   
print(np.allclose(W_3, W_4))

W_5, W_6 = calculateProducts(100, 9, 5)   
print(np.allclose(W_5, W_6))

W_7, W_8 = calculateProducts(2, 30, 1)   
print(np.allclose(W_7, W_8)) 

print(W_1) # printing the matrices to show they're equal 
print(W_2) 