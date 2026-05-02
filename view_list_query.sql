select distinct
    package_id,
    object_name
from "_SYS_REPO"."ACTIVE_OBJECT"
where (package_id like 'ILMN.%P2D%' or package_id like 'ILMN.%P2P%')
  and object_name like '%_QV'
