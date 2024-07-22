from .imports import pd

def load_and_preprocess(file_path):
    data = pd.read_csv(file_path)
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%d-%m-%Y %H:%M')
    data = data.dropna(subset=['CustomerID'])
    return data
