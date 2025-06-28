# AWS notes backup
This is a simple Python script to help me upload text files from a local directory to an AWS S3 bucket.

## What It Does

This script scans the directory it's in, finds all the .txt files, and uploads them to a specific folder within my S3 bucket. It uses the boto3 library, which is the official AWS SDK for Python.
You'll see a message for each file being uploaded and a final summary when it's done.
