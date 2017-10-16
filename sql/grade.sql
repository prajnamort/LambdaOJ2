create schema for_ta;

--helper functions to calculate punish cutoff
create or replace function diff_days(i interval) returns integer
as
$$ select ceil(extract(epoch from i) / 3600 / 24)::integer $$
language sql;

create or replace function get_punish(d integer) returns integer
as
$$ select case when d <= 0 then 0
   	       when d between 0 and 10 then d
	       else 10
	  end;
$$
language sql;

--user score info for each submit
create or replace view for_ta.user_scores as
select
  a.uid,
  a.pid,
  a.sc,
  (a.sc * (100 - 10 * a.cutoff) / 100.0)::float as effect_sc,
  a.sid,
  a.cutoff,
  a.create_time
from
  (select
    main_submit.user_id as uid,
    main_submit.problem_id as pid,
    case when main_submit.score is null then 0
         else main_submit.score
    end as sc,
    get_punish(diff_days(main_submit.create_time - main_problem.deadline)) as cutoff,
    main_submit.id as sid,
    main_submit.create_time as create_time
  from main_submit join main_problem on main_submit.problem_id = main_problem.id)a;

--user max_scores
create or replace view for_ta.user_max_effect_scores as
select
  uid,
  pid,
  max(effect_sc) as effect_sc
from
  for_ta.user_scores
group by
  uid, pid;

--user_best_submits
create or replace view for_ta.user_best_submits as
select
  a.uid,
  a.pid,
  max(sid) as sid
from
  for_ta.user_max_effect_scores as a join for_ta.user_scores as b
on a.uid = b.uid and a.effect_sc = b.effect_sc and a.pid = b.pid
group by
  a.uid, a.pid;

--user grade
create or replace view for_ta.user_grade as
select
  b.uid,
  b.pid,
  b.sid,
  b.sc,
  b.effect_sc,
  b.cutoff
from
  for_ta.user_best_submits as a join for_ta.user_scores as b
on a.sid = b.sid;

--report with pid
create or replace view for_ta.user_grade_report_pid as
select
  b.student_id,
  a.uid,
  a.pid,
  a.sc,
  a.effect_sc,
  a.cutoff
from
  for_ta.user_grade as a join main_user as b
on a.uid = b.id;

--report with number
create or replace view for_ta.user_grade_report_number as
select
  a.student_id,
  b.number as problem_number,
  a.sc as raw_score,
  a.effect_sc as effect_score,
  a.cutoff as punish_cutoff
from
  for_ta.user_grade_report_pid as a join main_problem as b
on a.pid = b.id;
