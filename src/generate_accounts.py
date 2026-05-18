import pandas as pd
from faker import Faker
import generate_customers as gc
import numpy as np

fake=Faker()
avg_acct_per_cust=2
data=[]
def generate_accounts(custermer_df,avg_acct_per_cust=2):
    for row in custermer_df.itertuples(index=False):
        customer_id=row.customer_id
        create_date=row.created_date


        num_acct_gen=np.random.randint(1,avg_acct_per_cust+1)

        for i in range(num_acct_gen):
                account_id = f"ACC{fake.random_number(digits=10)}"

                account_type = np.random.choice(
                    ["Savings", "Checking", "Credit", "Loan", "Investment"],
                    p=[0.35, 0.35, 0.10, 0.10, 0.10]
                )

                status = np.random.choice(
                    ["Active", "Dormant", "Closed"],
                    p=[0.85, 0.10, 0.05]
                )

                balance = round(np.random.uniform(100, 50000), 2)

                open_date = fake.date_between(start_date=create_date, end_date="today")

                data.append({
                    "account_id": account_id,
                    "customer_id": customer_id,
                    "account_type": account_type,
                    "status": status,
                    "balance": balance,
                    "open_date": open_date,
                    "updated_at": fake.date_time_this_year() 
                })
    return pd.DataFrame(data)

