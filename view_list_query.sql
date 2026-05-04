with q1 as (
select 
     distinct
    package_id,
    object_name
from "_SYS_REPO"."ACTIVE_OBJECT"
where object_suffix  = 'calculationview' and
 (package_id not like '%DEV%' and  package_id not like '%ILMN-LIVEVIEWS%')
  --and object_name  like '%_QV'
)

select * from q1 
where package_id||object_name not in ( select packagename||viewname from "NGUMATIMA1"."LINEAGE" )
and ( package_id like '%P2P%' or package_id like '%P2D%' )



