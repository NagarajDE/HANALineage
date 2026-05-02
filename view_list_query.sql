with q1 as (
select 
     distinct
    package_id,
    object_name
from "_SYS_REPO"."ACTIVE_OBJECT"
where object_suffix  = 'calculationview' and
 (package_id like 'ILMN.%P2D%' or package_id like 'ILMN.%P2P%')
  and object_name not like '%_QV'
)

select * from q1 where package_id||object_name not in ( select packagename||viewname from "NGUMATIMA1"."LINEAGE" )
