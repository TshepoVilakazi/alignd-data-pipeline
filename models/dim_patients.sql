select distinct
    client_id as patient_id,
    name,
    income,
    province
from staging.stg_clients
where client_id is not null