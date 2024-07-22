def plot_elbow(sse):
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 11), sse, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('SSE')
    plt.title('Elbow Method')
    plt.show()

def plot_clusters(customer_data):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(customer_data['InvoiceNo'],
                         customer_data['TotalSpend'],
                         customer_data['AveragePurchaseValue'],
                         c=customer_data['Cluster'],
                         cmap='viridis')
    ax.set_xlabel('Purchase Frequency')
    ax.set_ylabel('Total Spend')
    ax.set_zlabel('Average Purchase Value')
    ax.set_title('Customer Segments')
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    plt.show()
