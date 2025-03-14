# Exercise 6 — Tasks

6.1. Find the domestic and international sales for each movie

```sql
SELECT title, domestic_sales, international_sales
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
```

6.2. Show the sales numbers for each movie that did better internationally rather than domestically

```sql
SELECT movies.title, boxoffice.domestic_sales, boxoffice.international_sales
FROM movies
INNER JOIN boxoffice ON movies.id = boxoffice.movie_id
WHERE boxoffice.international_sales > boxoffice.domestic_sales;
```

6.3. List all the movies by their ratings in descending order

```sql
SELECT movies.title, boxoffice.rating
FROM movies
INNER JOIN boxoffice ON movies.id = boxoffice.movie_id
ORDER BY boxoffice.rating desc;
```

![alt text](image.png)

## Exercise 7 — Tasks

Find the list of all buildings that have employees ```sql
SELECT DISTINCT building FROM employees;

````
Find the list of all buildings and their capacity
```sql
SELECT building_name,capacity
FROM buildings;
````

List all buildings and the distinct employee roles in each building (including empty buildings)

```sql

```
