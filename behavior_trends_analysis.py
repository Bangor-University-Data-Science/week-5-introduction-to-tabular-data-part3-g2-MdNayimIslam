
import pandas as pd

def import_data(filename: str) -> pd.DataFrame:
    if filename.endswith('.csv'):
        return pd.read_csv(filename)
    elif filename.endswith('.xlsx'):
        return pd.read_excel(filename)
    else:
        raise ValueError("Please use CSV or Excel")

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['CustomerID'])
    return df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    return df.groupby('CustomerID').size().reset_index(name='purchase_count').query('purchase_count >= @min_purchases')

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    df['Quarter'] = pd.to_datetime(df['InvoiceDate']).dt.to_period('Q')
    return df.groupby('Quarter')['Revenue'].sum().reset_index().rename(columns={'Revenue': 'total_revenue'})

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    return df.groupby('StockCode')['Quantity'].sum().reset_index().nlargest(top_n, 'Quantity')

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('StockCode').agg(avg_quantity=('Quantity', 'mean'),avg_unit_price=('UnitPrice', 'mean')).reset_index().rename(columns={'StockCode': 'product'})

def answer_conceptual_questions() -> dict:
    answers = {
        'Q1': {'A', 'D'},
        'Q2': {'B'},
        'Q3': {'A', 'C'},
        'Q4': {'A', 'B'},
        'Q5': {'A'}
    }
    return answers
