import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000
categories = ['Clothing', 'Electronics', 'Beauty', 'Home', 'Books']

data = {
    'Product_ID': [f'P{i}' for i in range(n)],
    'Category': np.random.choice(categories, n),
    'Price': np.random.uniform(100, 5000, n),
    'Num_Orders': np.random.randint(50, 1000, n),
    'Past_Returns': np.random.randint(0, 150, n)
}

random_add = np.random.randint(0, 50, n)
total_returns = np.array(data['Past_Returns']) + random_add
data['Return_Count'] = np.minimum(total_returns, data['Num_Orders'])

df = pd.DataFrame(data)
df['Return_Percentage'] = df['Return_Count'] / df['Num_Orders'] * 100
df.to_csv('product_data.csv', index=False)
print("✅ Dataset saved as 'product_data.csv'")
