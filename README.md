# Customer-Insight-Clustering
Customer segmentation using K-Means clustering to analyse distinct customer groups based on their purchasing behaviours. 
By analyzing retail transaction data, we can identify key customer segments, which enables targeted marketing strategies and enhances overall business insights.



Data Preprocessing:

Conversion of the InvoiceDate column to datetime format and handling missing values by dropping rows with missing CustomerID.


Data Aggregation:

Aggregating data at the customer level to derive purchase frequency, total quantity purchased, and average unit price.


Feature Engineering:

Calculating total spend and average purchase value per customer.


Feature Selection:

Selecting key features such as purchase frequency, total spend, and average purchase value for clustering.


Data Normalization:

Normalizing the selected features using StandardScaler to ensure all features contribute equally to the clustering process.


Optimal Cluster Determination:

Utilizing the Elbow Method to determine the optimal number of clusters by plotting the sum of squared errors (SSE) for different cluster counts.


K-Means Clustering:

Applying K-Means clustering with the optimal number of clusters to segment customers into distinct groups.


Visualization:

Visualizing the customer segments using a 3D scatter plot to illustrate the distribution of clusters based on purchase frequency, total spend, and average purchase value.
