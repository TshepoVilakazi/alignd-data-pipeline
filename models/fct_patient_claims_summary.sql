select
    m.patient_id,
    count(*) as total_lapses,
    sum(l.premium_amount) as total_premium_amount,
    min(l.lapse_date) as first_lapse_date,
    max(l.lapse_date) as last_lapse_date
from staging.stg_health_lapses l
join {{ ref('stg_policy_client_map') }} m
    on l.policy_id = m.policy_id
group by m.patient_id