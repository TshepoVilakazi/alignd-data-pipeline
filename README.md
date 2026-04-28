# 🚀 Alignd Data Engineering Project

> End-to-end **data pipeline** built with Python, PostgreSQL, dbt, and Docker

---

## 🧭 Overview

This project demonstrates a **production-style data pipeline** that:

* Ingests raw health data
* Transforms and cleans it using Python
* Loads it into PostgreSQL
* Builds analytical models using dbt
* Validates data quality with tests
* Runs fully inside Docker

---

## 🏗️ Architecture

```text
Raw Data
   ↓
Python ETL Pipeline
   ↓
PostgreSQL (staging)
   ↓
dbt Models
   ↓
PostgreSQL (warehouse)
   ↓
dbt Tests
```

---

## 📁 Project Structure

```text
Alignd_Data_Pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   └── config.py
│
├── models/
│   ├── dim_patients.sql
│   ├── stg_policy_client_map.sql
│   ├── fct_patient_claims_summary.sql
│   └── schema.yml
│
├── docker-compose.yml
├── Dockerfile
├── run_pipeline.sh
└── README.md
```

---

## 🗄️ Data Model (Star Schema)

### 🟦 Dimension: `dim_patients`

| Column     | Description       |
| ---------- | ----------------- |
| patient_id | Unique identifier |
| name       | Patient name      |
| income     | Income value      |
| province   | Location          |

---

### 🟧 Fact: `fct_patient_claims_summary`

| Column               | Description          |
| -------------------- | -------------------- |
| patient_id           | Foreign key          |
| total_lapses         | Number of lapses     |
| total_premium_amount | Total premium amount |
| first_lapse_date     | First recorded lapse |
| last_lapse_date      | Most recent lapse    |

---

## ⚠️ Assumption

The dataset does not provide a direct relationship between `policy_id` and `client_id`.

To enable analysis, a mapping model was created:

```text
policy_id → patient_id
```

---

## 🧪 Data Quality (dbt)

Tests implemented:

* ✅ `not_null`
* ✅ `unique`

Ensures clean, reliable data for analytics.

---

## 🐳 Docker Orchestration

The entire pipeline runs inside Docker:

```text
PostgreSQL Container
        ↓
Python ETL
        ↓
dbt run
        ↓
dbt test
```

---

## ▶️ How to Run

```bash
docker compose up --build
```

---

## 🔄 Re-run Pipeline

```bash
docker compose run pipeline bash run_pipeline.sh
```

---

## 🧹 Full Reset

```bash
docker compose down -v --remove-orphans
docker compose up --build
```

---

## 📊 Viewing the Data

### 🖥️ Terminal

```bash
docker exec -it alignd_postgres psql -U postgres -d alignd_db
```

Then:

```sql
\dt staging.*
\dt warehouse.*

SELECT * FROM warehouse.dim_patients;
```

---

### 🧰 GUI (pgAdmin / DBeaver)

Use these connection details:

* Host: localhost
* Port: 5432
* Database: alignd_db
* Username: postgres
* Password: <your_password>

Navigate to:

```text
Schemas → staging / warehouse → Tables
```

---

## 🔐 Environment Variables

Create a `.env` file (not committed):

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<your_password>
POSTGRES_DB=alignd_db

DB_USER=postgres
DB_PASSWORD=<your_password>
DB_HOST=postgres
DB_PORT=5432
DB_NAME=alignd_db
```

---

## ✨ Key Features

* 🔁 Fully rerunnable (idempotent pipeline)
* 🧱 Clean staging → warehouse architecture
* 📦 Containerized with Docker
* 🧪 Built-in data quality checks
* ⚡ Production-style design

---

## 🧠 Technologies

* Python
* pandas
* PostgreSQL
* dbt
* Docker

---

## 👨‍💻 Author

**Tshepo Vilakazi**

---
