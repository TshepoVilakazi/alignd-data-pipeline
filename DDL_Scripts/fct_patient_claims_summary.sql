CREATE SCHEMA IF NOT EXISTS warehouse;

CREATE TABLE IF NOT EXISTS warehouse.fct_patient_claims_summary (
    patient_id INTEGER PRIMARY KEY,
    total_lapses INTEGER NOT NULL,
    total_premium_amount NUMERIC(12, 2) NOT NULL,
    first_lapse_date DATE,
    last_lapse_date DATE,

    CONSTRAINT fk_claims_summary_patient
        FOREIGN KEY (patient_id)
        REFERENCES warehouse.dim_patients(patient_id)
);

CREATE INDEX IF NOT EXISTS idx_fct_claims_summary_patient_id
ON warehouse.fct_patient_claims_summary (patient_id);