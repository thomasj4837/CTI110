# DHW1 – Query Analysis Questions

After you run `run_queries.py`, review your output and answer the questions below in complete sentences.

> **Important:** Your exact answers will be different from your classmates because each student may enter different fake user data.  
> Focus on explaining what your own query results show.

## 1) All Users (`SELECT * FROM users`)
How many total rows (users) are displayed in your output?  10 users
Does this match the number of users you intended to insert? Yes

# ANSWER: 10 users, Yes

## 2) Name + Email (`SELECT first_name, last_name, email FROM users`)
What information is shown in this query that is different from Query #1? Only Name + Email is queried instead of all user information

# ANSWER:  Only Name + Email is queried instead of all user information

## 3) Users from USA (`WHERE country = 'USA'`)
How many users from the USA appear in your results? (The answer can be 0 if none of your users have country 'USA'.) 5 users

# ANSWER: 5 users

## 4) Total User Count (`COUNT(*)`)
What value did your `total_users` query return?   10
How can this query help you check whether your data was inserted correctly? It organizes the data into a table and assigns an ID to each user.

# ANSWER: 10, It organizes the data into a table and assigns an ID to each user.

## 5) 3 Most Recent Signups (`ORDER BY signup_date DESC LIMIT 3`)
Which 3 usernames appear as the most recent in **your** output?  bulbasaur_k, misty_w, ash_k

# ANSWER: bulbasaur_k, misty_w, ash_k

---

> What should be in your zipped folder when you turn it in to Canvas -> create_signup_db.py, run_queries.py, signup_hw.db, and reflection.md
