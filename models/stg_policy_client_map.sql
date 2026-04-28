-- Because the source data did not include a direct policy_id → client_id relationship, a deterministic mapping model was created to support patient-level aggregation. In a production environment, this relationship would normally come from a policy/master data table.

with policies as (
    select distinct
        policy_id,
        row_number() over (order by policy_id) as rn
    from staging.stg_health_lapses
    where policy_id is not null
),

clients as (
    select
        client_id as patient_id,
        row_number() over (order by client_id) as rn
    from staging.stg_clients
    where client_id is not null
)

select
    p.policy_id,
    c.patient_id
from policies p
join clients c
    on ((p.rn - 1) % (select count(*) from clients)) + 1 = c.rn