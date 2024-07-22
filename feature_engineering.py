def aggregate_data(data):
    customer_data = data.groupby('CustomerID').agg({
        'InvoiceNo': 'nunique',
        'Quantity': 'sum',
        'UnitPrice': 'mean'
    }).reset_index()
    return customer_data

def create_features(customer_data):
    customer_data['TotalSpend'] = customer_data['Quantity'] * customer_data['UnitPrice']
    customer_data['AveragePurchaseValue'] = customer_data['TotalSpend'] / customer_data['InvoiceNo']
    return customer_data
