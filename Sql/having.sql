#HAVING CLAUSE:-

use college;
select * from info;

select aut_id,auth_name,sum(rating) from info 
group by auth_name
 having sum(rating)>3;#	IN HERE WHERE IS NOT SUPORTED USING GROUP BY
 
# WITH ROLLUP
select ifnull(auth_name,"TOTAL") as auth_name,sum(rating) from info 
group by auth_name
with rollup;


