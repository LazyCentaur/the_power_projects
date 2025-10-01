-- DataProject:
-- LógicaConsultasSQL

-- 1. Crea el esquema de la BBDD.
-- Lo dejo en el README.md, en un pantallazo

-- los SELECT, FROM etc, no están en mayúsculas porque DBeaver los pone en minúsculas automáticamente.

-- 2. Muestra los nombres de todas las películas con una clasificación por edades de ‘R’.
select f.title, f.rating 
from film f
where f.rating = 'R';

-- Encuentra los nombres de los actores que tengan un “actor_id” entre 30 y 40.
select concat(a.first_name, ' ', a.last_name)
from actor a
where a.actor_id between 30 and 40;

-- 4. Obtén las películas cuyo idioma coincide con el idioma original.
-- aquí en la BBDD viene todo a NULL el original_language_id
select f.film_id, f.title
from film f
join "language" l 
on f.original_language_id  = l.language_id;

-- 5. Ordena las películas por duración de forma ascendente.
select f.title, f.length 
from film f 
order by f.length asc;

-- 6. Encuentra el nombre y apellido de los actores que tengan ‘Allen’ en su apellido.
select *
from actor a
where a.last_name ILIKE 'Allen';

-- 7. Encuentra la cantidad total de películas en cada clasificación de la tabla
-- “film” y muestra la clasificación junto con el recuento.
select f.rating, count(f.rating)
from film f
group by f.rating
having f.rating is not NULL;

-- 8. Encuentra el título de todas las películas que son ‘PG-13’ o tienen una
-- duración mayor a 3 horas en la tabla film.
select f.title , f.rating , f.length 
from film f 
where f.rating = 'PG-13' or f.length > 180;

-- 9. Encuentra la variabilidad de lo que costaría reemplazar las películas.
select variance(f.replacement_cost ) as "variance_replacement_cost"
from film f;

-- 10. Encuentra la mayor y menor duración de una película de nuestra BBDD.
select min(f.length ) as "min_lenght", max(f.length ) as "max_lenght"
from film f;

-- 11. Encuentra lo que costó el antepenúltimo alquiler ordenado por día.
select date(r.rental_date) as day,
	coalesce(SUM(p.amount), 0) as cost
from rental r
left join payment p 
on p.rental_id =r.rental_id 
group by date(r.rental_date )
order by day desc
limit 1 offset 2;

-- 12. Encuentra el título de las películas en la tabla “film” que no sean ni ‘NC-17’ 
-- ni ‘G’ en cuanto a su clasificación.
select f.title , f.rating 
from film f 
where f.rating not in ('NC-17', 'G');

-- 13. Encuentra el promedio de duración de las películas para cada clasificación de la tabla film 
-- y muestra la clasificación junto con el promedio de duración.
select f.rating , round(avg(f.length ), 2) as avg_by_rating 
from film f 
group by f.rating;

-- 14. Encuentra el título de todas las películas que tengan una duración mayor a 180 minutos.
select f.title , f.length 
from film f 
where f.length > 180;

-- 15. ¿Cuánto dinero ha generado en total la empresa?
select sum(p.amount ) as total_payment
from payment p;

-- 16. Muestra los 10 clientes con mayor valor de id.
select c.customer_id , concat(c.first_name ,' ', c.last_name )
from customer c 
order by c.customer_id desc 
limit 10;

-- 17. Encuentra el nombre y apellido de los actores que aparecen en la película con título ‘Egg Igby’.
select concat(a.first_name , ' ', a.last_name ) as actor
from actor a 
where "actor_id" in (
	select fa.actor_id 
	from film_actor fa 
	where "film_id" in (
		select f.film_id 
		from film f 
		where f.title ilike 'Egg Igby'
	)
);

-- 18. Selecciona todos los nombres de las películas únicos.
select distinct(f.title)
from film f;

-- 19. Encuentra el título de las películas que son comedias y tienen una
-- duración mayor a 180 minutos en la tabla “film”.
select f.title , f.length ,  c."name" 
from film f
inner join film_category fc 
on f.film_id = fc.film_id 
inner join category c 
on fc.category_id = c.category_id 
where c."name" = 'Comedy' and f.length  > 180;

select f.title, f.length
from film f
where f.length > 180
  and exists (
    select 1
    from film_category fc
    join category c on c.category_id = fc.category_id
    where fc.film_id = f.film_id
      and c.name ilike 'Comedy'
);

-- 20. Encuentra las categorías de películas que tienen un promedio de duración 
-- superior a 110 minutos y muestra el nombre de la categoría junto con el promedio de duración.
select c.name as category_name , round(avg(f.length ), 2) as average_duration
from film f 
inner join film_category fc 
on f.film_id = fc.film_id 
inner join category c 
on fc.category_id = c.category_id
group by c."name"
having avg(f.length) > 110
order by average_duration desc;

-- 21. ¿Cuál es la media de duración del alquiler de las películas?
select avg(r.return_date - r.rental_date) as avg_rental_time
from rental r;

-- 22. Crea una columna con el nombre y apellidos de todos los actores y actrices.
select concat(a.first_name , ' ', a.last_name )
from actor a;

-- 23. Números de alquiler por día, ordenados por cantidad de alquiler de forma descendente.
select date(r.rental_date ) as day, count(*) as rentals
from rental r
group by day
order by rentals desc;

-- 24. Encuentra las películas con una duración superior al promedio.
select f.title , f.length
from film f
where f.length > (
	select avg(f2.length) 
	from film f2
);

-- 25. Averigua el número de alquileres registrados por mes.
select extract(month from r.rental_date) as month, count(*) as rentals
from rental r
group by month
order by rentals desc;

-- 26. Encuentra el promedio, la desviación estándar y varianza del total pagado.
select avg(p.amount ) as average, 
		stddev(p.amount ) as standard_deviation , 
		variance(p.amount) as variance
from payment p ;

-- 27. ¿Qué películas se alquilan por encima del precio medio?
with avg_amt as (
  select avg(p.amount) as avg_amt
  from payment p
)
select distinct f.title, p.amount 
from payment p
join rental r using (rental_id)
join inventory i using (inventory_id)
join film     f using (film_id)
cross join avg_amt
where p.amount > avg_amt.avg_amt
order by f.title;

-- 28. Muestra el id de los actores que hayan participado en más de 40 películas.
select fa.actor_id , count(fa.film_id)
from film_actor fa
group by fa.actor_id 
having count(fa.film_id) > 40;

-- 29. Obtener todas las películas y, si están disponibles en el inventario,
-- mostrar la cantidad disponible.
select f.title , count(i.inventory_id) as amount
from film f
left join inventory i
on f.film_id = i.film_id
group by f.film_id, f.title 
order by amount;

-- 30. Obtener los actores y el número de películas en las que ha actuado.
select a.actor_id , 
	concat(a.first_name ,' ', a.last_name ),
	count(fa.film_id) as film_count
from actor a
join film_actor fa 
on a.actor_id = fa.actor_id 
group by a.actor_id , a.first_name, a.last_name
order by film_count;

-- 31. Obtener todas las películas y mostrar los actores que han actuado en
-- ellas, incluso si algunas películas no tienen actores asociados.
select f.title, concat(a.first_name , ' ', a.last_name ) as actors
from film f 
full join film_actor fa
on f.film_id = fa.film_id 
left join actor a
on fa.actor_id = a.actor_id 
order by f.title;

-- 32. Obtener todos los actores y mostrar las películas en las que han
-- actuado, incluso si algunos actores no han actuado en ninguna película.
select concat(a.first_name , ' ', a.last_name ) as actors, f.title 
from actor a 
full join film_actor fa 
on a.actor_id = fa.actor_id 
full join film f 
on fa.film_id = f.film_id
order by a.first_name ;

-- 33. Obtener todas las películas que tenemos y todos los registros de alquiler.
select f.title , count(r.rental_id) as amount_of_rentals  
from film f
full join inventory i 
on f.film_id  = i.film_id 
full join rental r 
on i.inventory_id = r.inventory_id
group by f.title
order by f.title ;

-- 34. Encuentra los 5 clientes que más dinero se hayan gastado con nosotros.
select c.customer_id,
  concat(c.first_name , ' ', c.last_name) as customer,
  top5.total_spent
from customer c
join (
  select p.customer_id, sum(p.amount) as total_spent
  from payment p
  group by p.customer_id
  order by sum(p.amount) desc 
  limit 5
) top5 on top5.customer_id = c.customer_id
order by top5.total_spent desc;

with top5 as (
  select p.customer_id, sum(p.amount) as total_spent
  from payment p
  group by p.customer_id
  order by sum(p.amount) desc
  limit 5
)
select c.customer_id,
       concat(c.first_name ,' ' , c.last_name ) as customer,
       top5.total_spent
from customer c
join top5 on top5.customer_id = c.customer_id
order by top5.total_spent desc;

-- 35. Selecciona todos los actores cuyo primer nombre es ' Johnny'.
select a.actor_id , concat(a.first_name, ' ', a.last_name ) 
from actor a
where a.first_name ilike('Johnny');

-- 36. Renombra la columna “first_name” como Nombre y “last_name” como Apellido.
select a.first_name as "Nombre",  a.last_name as "Apellido" 
from actor a;

-- 37. Encuentra el ID del actor más bajo y más alto en la tabla actor.
select max(a.actor_id) as maximun, min(a.actor_id) as minimun 
from actor a;

-- 38. Cuenta cuántos actores hay en la tabla “actor”.
select count(a.actor_id)
from actor a;

-- 39. Selecciona todos los actores y ordénalos por apellido en orden ascendente.
select concat(a.first_name, ' ', a.last_name) 
from actor a
order by a.last_name, a.first_name;

-- 40. Selecciona las primeras 5 películas de la tabla “film”.
select f.film_id , f.title, f.description 
from film f
order by f.film_id 
limit 5;

-- 41. Agrupa los actores por su nombre y cuenta cuántos actores tienen el
-- mismo nombre. ¿Cuál es el nombre más repetido?
with name_counts as (
	select a.first_name, count(*) as cnt
	from actor a
	group by a.first_name 
)
select nc.first_name, nc.cnt 
from name_counts nc
order by nc.cnt desc
fetch first 1 row with ties;

-- 42. Encuentra todos los alquileres y los nombres de los clientes que los realizaron.
select r.rental_id as id_renta , concat(c.first_name , ' ', c.last_name ) as customer
from rental r
inner join customer c
on r.customer_id = c.customer_id;

-- 43. Muestra todos los clientes y sus alquileres si existen, incluyendo
-- aquellos que no tienen alquileres.
select concat(c.first_name, ' ', c.last_name ), r.rental_id 
from customer c 
left join rental r
on c.customer_id  = r.customer_id
order by c.last_name, c.first_name, r.rental_date nulls last;

-- 44. Realiza un CROSS JOIN entre las tablas film y category. ¿Aporta valor
-- esta consulta? ¿Por qué? Deja después de la consulta la contestación.
select *
from film f 
cross join film_category fc
order by fc.category_id ;
-- no aprta valor ya que una película solo puede tener 1 categoría y esto lo que hace es crear
-- filas mezclando todas las categorías con cada película, no tiene sentido.

-- 45. Encuentra los actores que han participado en películas de la categoría 'Action'.
with cte as (
    select f.film_id as film_id
    FROM film f
    inner join film_category fc 
    on f.film_id = fc.film_id 
    inner join category c2 
    on fc.category_id = c2.category_id 
    where c2.name = 'Action'
)
select distinct concat(a.first_name, ' ', a.last_name )
from cte
inner join film_actor fa 
on cte.film_id = fa.film_id
inner join actor a
on fa.actor_id = a.actor_id
order by concat(a.first_name, ' ', a.last_name );

-- 46. Encuentra todos los actores que no han participado en películas.
select *
from actor a
full join film_actor fa 
on a.actor_id = fa.actor_id 
where fa.film_id is null;

-- 47. Selecciona el nombre de los actores y la cantidad de películas en las
-- que han participado.
with cte as (
	select a.actor_id, concat(a.first_name, ' ', a.last_name ) as actor
	from actor a
)
select cte.actor ,  count(*) as films_number
from film_actor fa
join cte 
on fa.actor_id = cte.actor_id 
group by cte.actor_id, cte.actor
order by films_number;

-- 48. Crea una vista llamada “actor_num_peliculas” que muestre los nombres
-- de los actores y el número de películas en las que han participado.
create view actor_num_peliculas as
select concat(a.first_name, ' ', a.last_name) as name_actor, count(fa.film_id) as number_films
from actor a
left join film_actor fa
on a.actor_id = fa.actor_id
group by a.first_name, a.last_name;

-- 49. Calcula el número total de alquileres realizados por cada cliente.
select * 
from (
	with cte as (
		select r.customer_id, count(r.rental_id) as rentals
		from rental r
		group by r.customer_id
	)
	select concat(c.first_name, ' ', c.last_name), cte.rentals
	from cte
	right join customer c 
	on cte.customer_id = c.customer_id
	order by c.first_name, c.last_name
) as subc;

-- 50. Calcula la duración total de las películas en la categoría 'Action'.
with cte as (
	select f.film_id 
	from film f
	join film_category fc 
	on f.film_id = fc.film_id 
	join category c 
	on fc.category_id = c.category_id 
	where c."name" = 'Action'
)
select f.title as titulo, f.length as duracion_total 
from cte 
join film f
on cte.film_id = f.film_id

-- 51. Crea una tabla temporal llamada “cliente_rentas_temporal” para
-- almacenar el total de alquileres por cliente.
create temporary table cliente_rentas_temporal as
select concat(c.first_name, ' ', c.last_name ) as cliente, count(r.rental_id ) as rental_per_client
from customer c 
left join rental r 
on c.customer_id = r.customer_id
group by c.customer_id, c.first_name, c.last_name;

select * from cliente_rentas_temporal
order by rental_per_client;

-- 52. Crea una tabla temporal llamada “peliculas_alquiladas” que almacene las
-- películas que han sido alquiladas al menos 10 veces.
create temporary table peliculas_alquiladas as
select f.film_id , count(r.rental_id ) as total_rent
from rental r 
inner join inventory i 
on r.inventory_id = i.inventory_id 
inner join film f 
on i.film_id = f.film_id
group by f.film_id
having count(r.rental_id ) > 10;
  
-- 53. Encuentra el título de las películas que han sido alquiladas por el cliente con el nombre ‘Tammy Sanders’ 
-- y que aún no se han devuelto. Ordena los resultados alfabéticamente por título de película.
select f.title
from customer  c
join rental r 
on r.customer_id  = c.customer_id
join inventory i 
on i.inventory_id = r.inventory_id
join film f 
on f.film_id = i.film_id
where c.first_name ilike 'Tammy'
  and c.last_name  ilike 'sanders'
  and r.return_date is null
order by f.title;

-- 54. Encuentra los nombres de los actores que han actuado en al menos una película que pertenece 
-- a la categoría ‘Sci-Fi’. Ordena los resultados alfabéticamente por apellido.


select concat(a.first_name ,' ', a.last_name ) as actor
from actor a 
where exists (
	select 1
	from film_actor fa 
	join film f 
	on fa.film_id = f.film_id
	join film_category fc 
	on f.film_id = fc.film_id 
	join category c 
	on fc.category_id = c.category_id 
	where 
		fa.actor_id = a.actor_id 
		and c.name = 'Sci-Fi'
)
order by a.last_name , a.first_name ;

-- 55. Encuentra el nombre y apellido de los actores que han actuado en películas que se alquilaron 
-- después de que la película ‘Spartacus Cheaper’ se alquilara por primera vez. Ordena los resultados
-- alfabéticamente por apellido.
select concat(a.first_name ,' ', a.last_name )
from actor a 
where exists (
	select 1
	from film_actor fa 
	join inventory i 
	on fa.film_id = i.film_id
	join rental r
	on r.inventory_id = i.inventory_id
	where fa.actor_id = a.actor_id
	and r.rental_date > 
		(select min(r.rental_date )
		from rental r 
		inner join inventory i 
		on r.inventory_id = i.inventory_id 
		inner join film f 
		on i.film_id = f.film_id 
		where f.title ilike 'Spartacus Cheaper')
	)
order by a.last_name , a.first_name ;

-- 56. Encuentra el nombre y apellido de los actores que no han actuado en
-- ninguna película de la categoría ‘Music’.
select concat(a.first_name ,' ', a.last_name )
from actor a
where not exists (
	select 1
	from category c 
	join film f 
	on c.category_id = f.film_id
	join film_actor fa 
	on f.film_id = fa.film_id 
	where c."name" = 'Music'
	and fa.actor_id = a.actor_id 
)
order by a.last_name , a.first_name;

-- 57. Encuentra el título de todas las películas que fueron alquiladas por más de 8 días.
select distinct on (f.title) f.title, 
	r.return_date - r.rental_date as rent_days
from film f
inner join inventory i 
on f.film_id = i.film_id
inner join rental r
on r.inventory_id = i.inventory_id 
where r.return_date - r.rental_date > '8 days'
order by f.title ;

-- 58. Encuentra el título de todas las películas que son de la misma categoría que ‘Animation’
select f.title 
from film f 
where "film_id" in (
		select fc.film_id 
		from film_category fc 
		inner join category c 
		on fc.category_id = c.category_id 
		where c.name = 'Animation'
	)
order by f.title;

-- 59. Encuentra los nombres de las películas que tienen la misma duración que la película con 
-- el título ‘Dancing Fever’. Ordena los resultados alfabéticamente por título de película.
select f.title, f.length
from film f 
where "length" in (
	select f2.length 
	from film f2 
	where f2.title ilike 'Dancing Fever'
) order by f.title;

-- 60. Encuentra los nombres de los clientes que han alquilado al menos 7
-- películas distintas. Ordena los resultados alfabéticamente por apellido.
SELECT
  concat(c.first_name,' ', c.last_name) as customer,
  count(distinct i.film_id) as distinct_films
from customer c
join rental r 
on r.customer_id = c.customer_id
join inventory i 
on i.inventory_id = r.inventory_id
group by c.customer_id, c.first_name, c.last_name
having count(distinct i.film_id) >= 7
order by c.last_name, c.first_name;

-- 61. Encuentra la cantidad total de películas alquiladas por categoría y
-- muestra el nombre de la categoría junto con el recuento de alquileres.
select c.name, count(r.rental_id ) as total_rents
from category c 
left join film_category fc 
on c.category_id = fc.category_id 
left join film f 
on fc.film_id = f.film_id
left join inventory i 
on f.film_id = i.film_id
left join rental r 
on i.inventory_id = r.inventory_id
group by c.name
order by c."name" ;

-- 62. Encuentra el número de películas por categoría estrenadas en 2006.
select c.name as category, count(*) as film_count
from category c
join film_category fc 
on fc.category_id = c.category_id
join film f 
on f.film_id = fc.film_id
where f.release_year = 2006
group by c.name
order by film_count desc;

-- 63. Obtén todas las combinaciones posibles de trabajadores con las tiendas que tenemos.
select concat(s.first_name, ' ', s.last_name ) as worker, s2.store_id 
from staff s
cross join store s2 ;

-- 64. Encuentra la cantidad total de películas alquiladas por cada cliente y muestra el ID 
-- del cliente, su nombre y apellido junto con la cantidad de películas alquiladas.
select c.customer_id, concat(c.first_name, ' ',  c.last_name) as customer,
  count(r.rental_id) as total_rentals
from customer c
join rental r
  on r.customer_id = c.customer_id
group by c.customer_id, c.first_name, c.last_name
order by total_rentals DESC, c.last_name, c.first_name;
