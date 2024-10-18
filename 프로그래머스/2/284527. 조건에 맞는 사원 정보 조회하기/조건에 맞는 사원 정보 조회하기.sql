select sum(g.score) as SCORE, g.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from hr_employees e
    inner join hr_grade g on e.emp_no = g.emp_no
group by year, emp_no
having g.year = '2022'
order by score desc
limit 1
