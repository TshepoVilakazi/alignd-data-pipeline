CREATE SCHEMA IF NOT EXISTS warehouse;

CREATE TABLE IF NOT EXISTS warehouse.stg_policy_client_map (
    policy_id BIGINT PRIMARY KEY,
    patient_id INTEGER NOT NULL,

    CONSTRAINT fk_policy_client_patient
        FOREIGN KEY (patient_id)
        REFERENCES warehouse.dim_patients(patient_id)
);

CREATE INDEX IF NOT EXISTS idx_policy_client_patient_id
ON warehouse.stg_policy_client_map (patient_id);