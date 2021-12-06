# Implicit bias with FCMs

This repository includes the experimental process related to paper "Modeling Implicit Bias with Fuzzy Cognitive Maps" by Gonzalo Nápoles, Isel Grau, Leonardo Concepción, Lisa Koutsoviti Koumeri and João Paulo Papa.

**Files Description**

1. Reviewed manuscript -- link will soon be added
2. Fuzzy Cognitive Maps_BIAS.ipynb : Python notebook that computes the FCM models following the three scenarios described in the paper. It also includes data preprocessing. 
3. German Credit dataset : The same version of this file can also be found in UCI Machine Learning Repository.
4. Calculate Weight Matrix.ipynb : Python notebook that computes the weight matrix
5. GermanCreditBinary_formatted.txt : Preprocessed German Credit dataset using Bonchi et al, 2017, approach. We compare our FCM model to the model proposed by Bonchi et al, 2017.
  5.1 Link to Bonchi et al paper: https://link.springer.com/article/10.1007/s41060-016-0040-z#Tab1 \n
  5.2 Link to code: https://www.dropbox.com/sh/8rsh3y9zo1s0ann/AABbb-Z0SeKn5ORIAbZ1Rv0da?dl=0
6. Weight Matrix.csv : Weight/correlation matrix calculated using our approach
7. Weight Matrix Bonchi et al.csv : Weight/correlation matrix. Protected attributes are exncoded using Bonchi et al, 2017's approach.
