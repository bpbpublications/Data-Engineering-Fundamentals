import boto3

# Create an S3 client
s3 = boto3.client("s3")

# Define the S3 bucket name
bucket_name = "customer-journey-data-bucket"

# Define a lifecycle rule for archiving and deletion
lifecycle_rule = {
    "Rules": [
        {
            "ID": "ArchiveAndDelete",
            "Status": "Enabled",
            "Transitions": [
                {
                    "Days": 365,  # Move objects to Glacier after 1 year
                    "StorageClass": "GLACIER",
                },
            ],
            "Expiration": {
                "Days": 730,  # Automatically delete objects after 2 years
            },
        }
    ]
}

# Apply the lifecycle rule to the S3 bucket
s3.put_bucket_lifecycle_configuration(
    Bucket=bucket_name, LifecycleConfiguration=lifecycle_rule
)

print(f"Lifecycle rule successfully applied to {bucket_name}.")
