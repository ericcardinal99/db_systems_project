# CMPE 180B Project: Spam Detection for Social Media Platform
Fake accounts on social media platforms seem to be everywhere: offering free stuff in comments on posts, random messages to users, or attempting to impersonate an actual account. Most people on social media, if not all, have experienced these frustrating encounters. However, these accounts are often exposed as fake by their automated and repetitive behavior. 
Understanding the behaviors of spam accounts is the first step, and as social media users we have identified trends we often see. Through our project, we then hoped to demonstrate how such fake accounts could be identified quickly and removed before anyone is harmed.

The following steps shows the social media platfor database that we developed and how to set it up:

### Table Creation and Data Population
1. Start by sourcing the CreateTables.sql file to generate all the tables: SOURCE C:\Users\PATH_TO_FOLDER\CreateTables.sql
2. Set up indices for the table from the TableIndices.sql file: SOURCE C:\Users\PATH_TO_FOLDER\TableIndices.sql
2. Insert user data from the InsertUsers.sql file: SOURCE C:\Users\PATH_TO_FOLDER\InsertUsers.sql
3. Set up connection triggers to update user follower and following values: SOURCE C:\Users\PATH_TO_FOLDER\ConnectionTriggers.sql
4. Insert connection data from InsertConnections.sql file: SOURCE C:\Users\PATH_TO_FOLDER\InsertConnections.sql
5. Insert spam connection data from SpamConnections.sql file: SOURCE C:\Users\PATH_TO_FOLDER\SpamConnections.sql
6. Insert post data from InsertPosts.sql file: SOURCE C:\Users\PATH_TO_FOLDER\InsertPosts.sql
7. Insert spam post data from SpamPosts.sql file: SOURCE C:\Users\PATH_TO_FOLDER\SpamPosts.sql
8. Insert message data from InsertMessages.sql file: SOURCE C:\Users\PATH_TO_FOLDER\InsertMessages.sql
9. Insert spam message data form SpamMessages.sql file: SOURCE C:\Users\PATH_TO_FOLDER\SpamMessages.sql
10. Insert comment data from InsertComments.sql file: SOURCE C:\Users\PATH_TO_FOLDER\InsertComments.sql
11. Insert spam comment data form SpamComments.sql file: SOURCE C:\Users\PATH_TO_FOLDER\SpamComments.sql
12. Insert report data from InsertReports.sql file: SOURCE C:\Users\PATH_TO_FOLDER\InsertReports.sql
13. Insert tagged_users data from InsertTags.sql file: SOURCE C:\Users\PATH_TO_FOLDER\InsertTags.sql

### Dependencies
***User Table:***
- Primary Key: user_id
- Dependent on:
  - post(user_id)
  - comment(user_id)
  - message(from_user_id, to_user_id)
  - report(source_id, user_id)
  - connections(follower_id, followed_id)
  - tagged_users(user_id)

***Post Table:***
- Primary Key: post_id
- Dependent on:
  - user(user_id)
  - comment(post_id)
  - tagged_users(post_id)

***Comment Table:***
- Primary Key: comment_id
- Dependent on:
  - post(post_id)
  - user(user_id)

***Message Table:***
- Primary Key: message_id
- Dependent on:
  - user(from_user_id)
  - user(to_user_id)

***Report Table:***
- Primary Key: report_id
- Dependent on:
  - user(source_id)
  - user(user_id)

***Connections Table:***
- Composite Primary Key: (follower_id, followed_id)
- Dependent on:
  - user(follower_id)
  - user(followed_id)

***Tagged Users Table:***
- Composite Primary Key: (post_id, user_id)
- Dependent on:
  - post(post_id)
  - user(user_id)
