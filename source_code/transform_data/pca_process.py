from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA
from sklearn.decomposition import SparsePCA
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import NMF
from sklearn.decomposition import FactorAnalysis
from sklearn.decomposition import IncrementalPCA

class transformation_data(object):

    def apply_pca_linear(
        self, 
        dataset=None, 
        n_components=None, 
        svd_solver="auto",
        tol=0.0,
        iterated_power="auto",
        random_state=None):
        
        pca_instance = PCA(
            n_components=n_components,
            svd_solver=svd_solver,
            tol=tol,
            iterated_power=iterated_power,
            random_state=random_state)

        pca_instance.fit(dataset)
        transform_data = pca_instance.transform(dataset)

        return transform_data, pca_instance
    
    def apply_kernel_pca(
        self, 
        dataset=None,
        n_components=None, 
        kernel="poly", 
        gamma=None, 
        degree=3,
        coef0=1,
        alpha=1.0,
        eigen_solver="auto",
        tol=0,
        iterated_power="auto",
        random_state=None,
        max_iter=None, 
        n_jobs=-1):

        kernel_pca_instance = KernelPCA(
            n_components=n_components,
            kernel=kernel, 
            gamma=gamma, 
            degree=degree,
            coef0=coef0,
            alpha=alpha,
            eigen_solver=eigen_solver,
            tol=tol,
            iterated_power=iterated_power,
            random_state=random_state,
            max_iter=max_iter,
            n_jobs=n_jobs)
        
        kernel_pca_instance.fit(dataset)
        tranform_data = kernel_pca_instance.transform(dataset)

        return tranform_data, kernel_pca_instance
    
    
