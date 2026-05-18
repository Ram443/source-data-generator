import pandas as pd
import numpy as np
from faker import Faker

class DataGenerator:
    def __init__(self):
        self.faker=Faker()
        self.customer_count=0

    def generate_customers(self,n=0):
        CData=[]
        for i in range(n):
            self.customer_count += 1
            cust_id = f"C{self.customer_count}:06d"
            CData.append({
                "customer_id":cust_id,
                "name":self.faker.name(),
                "dob":self.faker.date_of_birth(minimum_age=18,maximum_age=88),
                "gender":np.random.choice(["M","F","O"]),
                "kyc_status":np.random.choice(["Verified", "Pending", "Rejected"], p=[0.8, 0.15, 0.05]),
                "segment": np.random.choice(["Retail", "Priority", "Wealth"]),
                "email":self.faker.email(),
                "phone":self.faker.phone_number(),
                "address":self.faker.address().replace("\n", ", "),
                "created_date":self.faker.date_between(start_date="-10y", end_date="today"),
                "updated_at":self.faker.date_time_this_year()
                })
        return pd.DataFrame(CData)
        
    #
    #Generate Accounts
    #
    def generate_accounts(self,custmer_df,avg_acct_per_cust=2):
        AData=[]
        for row in custmer_df.itertuples(index=False):
            customer_id=row.customer_id
            create_date=row.created_date
    
    
            num_acct_gen=np.random.randint(1,avg_acct_per_cust+1)
    
            for i in range(num_acct_gen):
                    account_id = f"ACC{self.faker.random_number(digits=10)}"
    
                    account_type = np.random.choice(
                        ["Savings", "Checking", "Credit", "Loan", "Investment"],
                        p=[0.35, 0.35, 0.10, 0.10, 0.10]
                    )
    
                    status = np.random.choice(
                        ["Active", "Dormant", "Closed"],
                        p=[0.85, 0.10, 0.05]
                    )
    
                    balance = round(np.random.uniform(100, 50000), 2)
    
                    open_date = self.faker.date_between(start_date=create_date, end_date="today")
    
                    AData.append({
                        "account_id": account_id,
                        "customer_id": customer_id,
                        "account_type": account_type,
                        "status": status,
                        "balance": balance,
                        "open_date": open_date,
                        "updated_at": self.faker.date_time_this_year() 
                    })
        return pd.DataFrame(AData)