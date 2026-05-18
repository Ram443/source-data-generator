import boto3 as boto
from datetime import datetime
import os

class S3Uploader:
    def __init__(self,bucket_nm,region_nm="us-east-1"):
        self.bucket_nm = bucket_nm
        self.region_nm=region_nm
        self.s3=boto.client("s3",region_name=self.region_nm)

    def generate_s3_path(self,domain,file_nm):
        load_dt=datetime.now().strftime("%Y-%m-%d")
        return f"bronze/{domain}/load_date={load_dt}/{file_nm}"
    
    def write_temp_csv(self,df,file_nm):
        temp_path=f"/tmp/{file_nm}"
        df.to_csv(temp_path,index=False)
        return temp_path
    
    def upload(self,local_path,s3_path):
        try:
            self.s3.upload_file(local_path,self.bucket_nm,s3_path)
            print(f"upload -> s3://{self.bucket_nm}/{s3_path}")
        except Exception as e:
            print(f"Upload failed: {e}")
            raise e