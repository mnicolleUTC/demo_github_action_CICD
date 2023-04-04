import pandas as pd
import numpy as np
import boto3
from cred import AWS_KEY_ID,AWS_KEY_SECRET


def test_secret():
    s3 = boto3.client('s3', aws_access_key_id=AWS_KEY_ID,\
							aws_secret_access_key=AWS_KEY_SECRET)
    with open("temp.txt","w") as f :
        f.write("test OK")
    with open("temp.txt", "rb") as f:
	    # Upload the file to S3
        s3.upload_fileobj(f, "netflix-recommandation", "last_recommandation/temp.txt")


if __name__ =="__main__":
    matrix = np.zeros(4)
    df = pd.DataFrame(matrix)
    print("Hello word")
    test_secret()
    print("Success Loading")