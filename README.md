# Customer-Insight-Clustering
Customer segmentation using K-Means clustering to analyse distinct customer groups based on their purchasing behaviours. 
By analyzing retail transaction data, we can identify key customer segments, which enables targeted marketing strategies and enhances overall business insights.

## Tools and Technologies

Pandas: For data manipulation and analysis.

Matplotlib: For creating visualizations.

Scikit-learn: For data normalization and clustering algorithms.



## i) Data Preprocessing:

Conversion of the InvoiceDate column to datetime format and handling missing values by dropping rows with missing CustomerID.


## ii) Data Aggregation:

Aggregating data at the customer level to derive purchase frequency, total quantity purchased, and average unit price.


## iii) Feature Engineering:

Calculating total spend and average purchase value per customer.


## iv) Feature Selection:

Selecting key features such as purchase frequency, total spend, and average purchase value for clustering.


## v) Data Normalization:

Normalizing the selected features using StandardScaler to ensure all features contribute equally to the clustering process.


## vi) Optimal Cluster Determination:

Utilizing the Elbow Method to determine the optimal number of clusters by plotting the sum of squared errors (SSE) for different cluster counts.


## vii) K-Means Clustering:

Applying K-Means clustering with the optimal number of clusters to segment customers into distinct groups.


## ix) Visualization:

Visualizing the customer segments using a 3D scatter plot to illustrate the distribution of clusters based on purchase frequency, total spend, and average purchase value.


1: Clone the repository:
``git clone https://github.com/yourusername/Customer-Insight-Clustering.git``

2: Navigate to the project directory:
``cd Customer-Insight-Clustering``

3: Run the script
``python customer_segmentation.py``

## Conclusions:

Marketing Strategy: The distinct segmentation allows for targeted marketing strategies, focusing on high-value customers for loyalty programs and low-value customers for acquisition campaigns.

Optimal Cluster Identification: The Elbow Method plot indicates an optimal number of clusters at K=4, where the sum of squared errors (SSE) shows a pronounced inflection point, suggesting diminishing returns for adding more clusters beyond this point.

Low Variance within Clusters: The sharp decline in SSE up to 4 clusters indicates that the clusters formed within this range have low intra-cluster variance, enhancing the homogeneity within each cluster.

Dominance of Low-Frequency Purchasers: The 3D scatter plot reveals a dominant cluster with low purchase frequency and low total spend, indicating a significant portion of customers with infrequent and low-value transactions.



![image](https://github.com/user-attachments/assets/f1f7a023-af3b-47e8-8c3c-f060f2dee156)


![image](https://github.com/user-attachments/assets/d42e1aa6-409e-4f6c-a616-a5c2ff9cb893)

