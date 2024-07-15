# 1. Export all data about users in HD subscription */
query_1 = """
    SELECT *
    FROM user u
    JOIN subscription s ON u.subscription_type = s.subscription_id
    WHERE s.subscription_type = 'HD';
"""

# 2. Export all data about the actors and their associated movies
query_2 = """
    SELECT actor.*, movie.*
    FROM actor
    JOIN movieactor ON actor.actor_id = movieactor.actor_id
    JOIN movie ON movie.movie_id = movieactor.movie_id;
"""

# 3. Export all data to group actors from a specific city, showing also the average age (per city). 
query_3 = """
    SELECT 
    city,
    COUNT(actor_id) AS number_of_actors,
    AVG(YEAR(CURDATE()) - YEAR(dob)) AS average_age
    FROM 
        actor
    GROUP BY 
        city;
"""

# 4. Export all data to show the favourite comedy movies for a specific user.
query_4 = """
    SELECT favouritemovie.user_id, movie.*
    FROM favouritemovie
    JOIN movie ON movie.movie_id = favouritemovie.movie_id
    WHERE favouritemovie.user_id = 1 and movie.genre = 'Comedy';
"""

# 5. Export all data to count how many subscriptions are in the database per country.
query_5 = """
    SELECT Country, COUNT(subscription_type) AS SubscriptionCount
    FROM user
    GROUP BY Country
"""

# 6. Export all data to find the movies that start with the keyword 'The'.
query_6 = """
    SELECT *
    FROM movie
    WHERE title like 'The%';
"""

# 7. Export data to find the number of subscriptions per movie category
query_7 = """
    SELECT 
    m.genre, 
    COUNT(DISTINCT u.user_id) AS subscription_count
    FROM 
        movie m
    JOIN 
        watchhistory wh ON m.movie_id = wh.movie_id
    JOIN 
        user u ON wh.user_id = u.user_id
    GROUP BY 
        m.genre;
"""

# 8.  Export data to find the username and the city of the youngest customer in the UHD subscription category
query_8 = """
    SELECT 
        u.username, 
        u.city,
        u.age
    FROM 
        user u
    JOIN 
        subscription s ON u.subscription_type = s.subscription_id
    WHERE 
        s.subscription_type = 'UHD'
    ORDER BY 
        u.age ASC
    LIMIT 1;
"""

# 9. Export data to find users between 22 - 30 years old (including 22 and 30 )
query_9 = """
    SELECT 
        * 
    FROM 
        user 
    WHERE 
        age BETWEEN 22 AND 30;
"""

# 10. Export data to find the average age of users with low score reviews (less than 3)
# Group your data for users under 20, 21-40, and 41 and over
query_10 = """
    SELECT
    CASE 
        WHEN u.age < 20 THEN 'Under 20'
        WHEN u.age BETWEEN 21 AND 40 THEN '21-40'
        ELSE '41 and over'
    END AS age_group,
    AVG(u.age) AS average_age
    FROM
        user u
    JOIN
        review r ON u.user_id = r.user_id
    WHERE
        r.score < 3
    GROUP BY
        age_group;
"""