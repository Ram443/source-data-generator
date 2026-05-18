from faker import Faker
import  numpy as np
import pandas as pd
fake=Faker()

def generate_customers(n=1):
    data=[]
    for i in range(n):
        data.append({
            "customer_id":f"C{i+1:09d}",
            "name":fake.name(),
            "dob":fake.date_of_birth(minimum_age=18,maximum_age=88),
            "gender":np.random.choice(["M","F","O"]),
            "kyc_status":np.random.choice(["Verified", "Pending", "Rejected"], p=[0.8, 0.15, 0.05]),
            "segment": np.random.choice(["Retail", "Priority", "Wealth"]),
            "email":fake.email(),
            "phone":fake.phone_number(),
            "address":fake.address().replace("\n", ", "),
            "created_date":fake.date_between(start_date="-10y", end_date="today"),
            "updated_at":fake.date_time_this_year()
            })
    return pd.DataFrame(data)
    

