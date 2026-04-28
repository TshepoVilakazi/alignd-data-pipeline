CREATE SCHEMA IF NOT EXISTS warehouse;

CREATE TABLE IF NOT EXISTS warehouse.dim_patients (
    patient_id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    income NUMERIC(12, 2),
    province VARCHAR(100)
);

CREATE INDEX IF NOT EXISTS idx_dim_patients_province
ON warehouse.dim_patients (province);