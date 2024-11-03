# YouTube Trending Video ETL and Analysis

This project provides an end-to-end data engineering and analytics solution for analyzing YouTube's trending video dataset. Leveraging AWS services, ETL pipelines, and data visualization, it aims to uncover insights from trending YouTube videos, including top content categories, engagement patterns, and optimal posting times.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Architecture](#project-architecture)
- [Technologies Used](#technologies-used)
- [Data Ingestion and Storage](#data-ingestion-and-storage)
- [Data Processing and Transformation](#data-processing-and-transformation)
- [Data Analysis and Visualization](#data-analysis-and-visualization)
- [Setup and Execution](#setup-and-execution)
- [Dashboard and Insights](#dashboard-and-insights)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project addresses a hypothetical client’s need for optimizing YouTube ad campaigns. By analyzing YouTube’s trending videos, we identify key factors influencing video popularity and help categorize videos for targeted advertising. Main objectives:

- Build a scalable ETL pipeline for data ingestion, transformation, and storage.
- Set up a structured data lake and processing layers on AWS.
- Generate insights on video trends, engagement, and regional preferences.

## Project Architecture

The project is implemented with a modular and scalable architecture:

1. **Data Ingestion**: Ingest raw data from YouTube's trending videos dataset on Kaggle.
2. **ETL Pipeline**: AWS Glue ETL jobs transform and load data.
3. **Data Storage**: Store processed data in AWS S3 with partitions for efficient querying.
4. **Data Lake & Cataloging**: AWS Glue for data cataloging, AWS Athena for querying.
5. **Dashboard**: Insights visualized in a custom dashboard.

![Architecture Diagram Placeholder](extras/architecture.jpeg)

## Technologies Used

- **Cloud Platform**: AWS
- **ETL**: AWS Glue, AWS Lambda
- **Data Storage**: Amazon S3
- **Data Processing**: Apache Spark (via AWS Glue)
- **Data Cataloging**: AWS Glue Catalog
- **Query Engine**: AWS Athena
- **Visualization**: Tableau / Power BI

## Data Ingestion and Storage

Data for this project is sourced from Kaggle’s YouTube Trending Video dataset, containing:
- Video metadata (title, category, views, likes, dislikes)
- Regional information (e.g., Canada, Great Britain, US)

Data is uploaded to AWS S3 and organized in a structured data lake format, partitioned by video category and region.

## Data Processing and Transformation

1. **Data Cleaning**: JSON and CSV files are preprocessed using AWS Lambda functions to handle parsing errors and format inconsistencies.
2. **Data Transformation**: Glue ETL jobs transform and partition data, converting it into columnar formats (e.g., Parquet).
3. **Data Cataloging**: AWS Glue Crawler is used to catalog data, enabling access for Athena queries.

## Data Analysis and Visualization

Data analysis includes:
- **Engagement Analysis**: Understanding video engagement (likes/comments) across categories.
- **Trend Patterns**: Analyzing the frequency of trending videos over time.
- **Geographic Insights**: Mapping video popularity by region.

The final dashboard visualizes these insights, providing the client with data-driven recommendations for ad targeting and scheduling.

## Setup and Execution

1. **AWS Setup**:
   - Set up AWS account and configure IAM roles for Glue and S3.
   - Deploy S3 buckets with permissions for raw, processed, and analytical data.
2. **ETL Pipeline**:
   - Configure Glue Crawlers and AWS Lambda functions for data preprocessing.
   - Define ETL workflows with Glue Studio.
3. **Data Cataloging and Querying**:
   - Use Athena to query data stored in S3.
   - Load query results into an analytical layer via Glue jobs.

## Dashboard and Insights

Dashboard and Insights
The Tableau dashboard allows users to dynamically explore engagement insights, with key visuals including:

Regional View Distribution: Map-based view counts by region.
Views per Category: Bar chart of views distributed across video categories.
Response Metrics by Category and Region: Insights into likes, dislikes, comments, and views with adjustable aggregation methods.

The dashboard is interactive and provides various metrics and ratios computed across region and categories. 
Find the Tableau Dashboard <a href = "https://public.tableau.com/views/YoutubeTrendingVideoAnalysis_17301475010720/YoutubeTrendingVideoAnalysis?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">here</a>
