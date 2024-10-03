import numpy as np
   
data = np.array([[2.5, 2.4],
                 [0.5, 0.7],
                 [2.2, 2.9],
                 [1.9, 2.2],
                 [3.1, 3.0]])

num_components = 1
X_meaned = data - np.mean(data, axis=0)

covariance_matrix = np.cov(X_meaned, rowvar=False)

eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

sorted_indices = np.argsort(eigenvalues)[::-1]  
sorted_eigenvalues = eigenvalues[sorted_indices]
principal_comp = eigenvectors[:, sorted_indices]

selected_eigenvectors = principal_comp[:, :num_components]

X_reduced = X_meaned.dot(selected_eigenvectors)

print("Reduced Data:\n", X_reduced)
print("\nEigenvalues:\n", sorted_eigenvalues)
print("\nPrincipal Components (Eigenvectors):\n", principal_comp)

