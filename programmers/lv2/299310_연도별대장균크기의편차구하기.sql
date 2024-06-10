-- https://school.programmers.co.kr/learn/courses/30/lessons/299310

select year(t.differentiation_date) as year, (select max(size_of_colony) - t.size_of_colony
               from ecoli_data
               where year(differentiation_date) = year(t.differentiation_date)) as year_dev, t.id
from ecoli_data t
order by year, year_dev


-- with 구문 사용하기
with max_size as
(select year(differentiation_date) year, max(size_of_colony) max_size
    from ecoli_data
    group by 1)


select by m.year, (max_size - e.size_of_colony) year_dev, id
from ecoli_data e
left join max_size m
on year(e.differentiation_date) = m.year
order by 1, 2


--
with max_size as (
    select year(differentiation_date) year, max(size_of_colony) max_size
    from ecoli_data
    group by 1
)

select year(e.differentiation_date) as year, m.max_size - e.size_of_colony as year_dev, id
from ecoli_data e
left join max_size m
on m.year = year(e.differentiation_date)
order by 1, 2