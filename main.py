import pandas as pd
import numpy as np
import boto3
import os


def test_secret():
    s3 = boto3.client('s3', aws_access_key_id=AWS_KEY_ID,\
							aws_secret_access_key=AWS_KEY_SECRET)
    with open("temp.txt","w") as f :
        f.write("test OK")
    with open("temp.txt", "rb") as f:
	    # Upload the file to S3
        s3.upload_fileobj(f, "netflix-recommandation", "last_recommandation/temp.txt")


if __name__ =="__main__":
    # Fetch secret Variable with os
    #AWS_KEY_ID = os.environ['AWS_KEY_ID']
    #AWS_KEY_SECRET = os.environ['AWS_KEY_SECRET']
    # Test lines 
    matrix = np.zeros(4)
    df = pd.DataFrame(matrix)
    # Test Boto3
    #test_secret()
    print("Success Loading")
    # Prompt message 
    print("This is commit 2")