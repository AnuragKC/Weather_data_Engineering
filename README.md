# Weather Data Engineering Pipeline

This project implements a weather data processing pipeline using AWS services and Snowflake. 
The pipeline fetches data from a weather API, processes it, and stores it in Snowflake for further analysis.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Pipeline Workflow](#pipeline-workflow)
- [Setup Instructions](#setup-instructions)
- [Showcase Purpose](#showcase-purpose)

## Overview

The pipeline integrates various AWS services (mainly lambda, s3 and dynamodb) and Snowflake to ingest, process, and store weather data. It uses:

- EventBridge for scheduling tasks.
- Lambda for data processing and integration.
- DynamoDB for intermediate data storage.
- S3 for staging processed data.
- Snowpipe in Snowflake for automated ingestion.

## Technologies Used

- AWS Lambda
- AWS DynamoDB
- AWS EventBridge
- AWS S3
- AWS SNS
- Python
- Snowflake

## Pipeline Workflow

### 1. API Integration
- Acquired an API key to access weather data.
- Developed a Python script to fetch weather data from the API.

### 2. Event Triggering
- Set up an EventBridge Schedule to trigger the Lambda function every hour.

### 3. Data Ingestion into DynamoDB
- The Lambda function fetches weather data from the API and stores it in a **DynamoDB table**.

### 4. Processing DynamoDB Streams
- Configured DynamoDB Streams to trigger a Lambda function whenever data is inserted.
- The triggered Lambda function processes the data and uploads it to an S3 bucket.

### 5. Data Loading into Snowflake
- Configured Snowpipe in Snowflake to monitor new data in the S3 bucket.
- Set up an SNS queue to notify Snowflake about new data uploads.
- Snowpipe ingests the data from the S3 bucket into a Snowflake external stage.

## Snowflake Integration
- Implemented Snowflake querying to manage the weather data pipeline.
- Utilized Snowpipe for seamless data ingestion into Snowflake tables from an S3 bucket.
- Created a database, table schema, and external stage for automated data integration.

## Setup Instructions

### 1. API Key Setup:
   - Obtain an API key from the weather API provider.
   - Add the key to your Lambda function environment variables.

### 2. AWS Resources:
   - Create an EventBridge rule for scheduling the Lambda function.
   - Set up DynamoDB and enable streams for the table.
   - Configure S3 bucket for storing processed data.

### 3. Lambda Function:
   - Write and deploy Python scripts for fetching API data and processing DynamoDB streams.

### 4. Snowflake Configuration:
   - Configure Snowpipe to monitor the S3 bucket.
   - Set up an SNS queue to notify Snowflake about new data.

### 5. Testing:
   - Trigger the EventBridge rule and verify the pipeline.
   - Check DynamoDB, S3, and Snowflake for data consistency.

## Showcase Purpose

This project is designed for personal use only.

