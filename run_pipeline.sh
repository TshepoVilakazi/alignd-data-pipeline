#!/bin/bash
set -e

echo "Waiting for PostgreSQL to be ready..."
sleep 10

echo "Starting Docker orchestration..."

echo "Step 1: Running Python ETL pipeline..."
python -m src.pipeline

echo "Step 2: Running dbt models..."
dbt run

echo "Step 3: Running dbt tests..."
dbt test

echo "Pipeline completed successfully."