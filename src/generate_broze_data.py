from DataGenerator import DataGenerator
from S3Uploader import S3Uploader
from datetime import datetime

gen=DataGenerator()
uploader=S3Uploader(bucket_nm="bank-lakehouse")
customer=gen.generate_customers(4)
accounts=gen.generate_accounts(customer,2)

cust_file_nm=f"custmers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
acct_file_nm=f"accounts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

cust_local=uploader.write_temp_csv(customer,cust_file_nm)
acct_local=uploader.write_temp_csv(accounts,acct_file_nm)

cust_s3 =uploader.generate_s3_path("customers",cust_file_nm)
acct_s3=uploader.generate_s3_path("accounts",acct_file_nm)

uploader.upload(cust_local,cust_s3)
uploader.upload(acct_local,acct_s3)