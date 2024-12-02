import random
import datetime

# Generate a list of unique usernames and profile names
def generate_unique_users(num_users):
    usernames = [f"user_{i}" for i in range(1, num_users + 1)]
    profile_names = [f"Profile {i}" for i in range(1, num_users + 1)]
    return list(zip(usernames, profile_names))

# Generate SQL insert statements for 200 users
def generate_sql_insert_statements(user_data):
    sql_statements = ['INSERT INTO user (username, profile_name, date_created) VALUES']
    
    for user in user_data:
        date_created = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 2000))
        sql = f"('{user[0]}', '{user[1]}', '{date_created}'),"
        sql_statements.append(sql)
    # Remove last comma
    sql_statements[-1] = sql_statements[-1][0:len(sql_statements[-1])-1]
    return sql_statements

# Generate 200 users
user_data = generate_unique_users(200)
sql_statements = generate_sql_insert_statements(user_data)

# Create the SQL file
sql_file_path = "InsertUsers.sql"
with open(sql_file_path, "w+") as file:
    file.write("-- SQL Statements to Populate User Table\n")
    file.write("\n".join(sql_statements))

sql_file_path

connections = []

# Generate SQL insert statements for the connections table
def generate_connections_sql(num_users, min_connections, max_connections):
    sql_statements = []
    sql_statements.append('INSERT INTO connections (followed_id, follower_id, timestamp) VALUES')
    for user_id in range(1, num_users + 1):
        num_connections = random.randint(min_connections, max_connections)
        followed_users = random.sample(
            [i for i in range(1, num_users + 1) if i != user_id], num_connections
        )
        for followed_id in followed_users:
            connections.append(f'{followed_id}-{user_id}')
            random_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 2000))
            sql = f"({followed_id}, {user_id}, '{random_date.strftime('%Y-%m-%d %H:%M:%S')}'),"
            sql_statements.append(sql)
    
    # Remove last comma
    sql_statements[-1] = sql_statements[-1][0:len(sql_statements[-1])-1]
    return sql_statements

# Generate SQL statements for connections
connections_sql_statements = generate_connections_sql(200, 5, 20)

# Create the SQL file for connections
connections_sql_file_path = "InsertConnections.sql"
with open(connections_sql_file_path, "w+") as file:
    file.write("-- SQL Statements to Populate Connections Table\n")
    file.write("\n".join(connections_sql_statements))

connections_sql_file_path

def generate_spam_connections_sql(num_users):
    sql_statements = []
    sql_statements.append('INSERT INTO connections (followed_id, follower_id, timestamp) VALUES')
    spam_users = random.sample(range(1, 201), num_users)
    for user_id in spam_users:
        followed_users = random.sample(range(1, 201), 30)
        if user_id in followed_users:
            followed_users.remove(user_id)
        random_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 2000))
        for followed_id in followed_users:
            if f'{followed_id}-{user_id}' not in connections:
                sql = f"({followed_id}, {user_id}, '{random_date}'),"
                sql_statements.append(sql)
    
    # Remove last comma
    sql_statements[-1] = sql_statements[-1][0:len(sql_statements[-1])-1]
    return sql_statements

# Generate SQL statements for spam connections
spam_connections = generate_spam_connections_sql(5)

# Create the SQL file for connections
connections_sql_file_path = "SpamConnections.sql"
with open(connections_sql_file_path, "w+") as file:
    file.write("-- SQL Statements to Populate Spam Connections Table\n")
    file.write("\n".join(spam_connections))

# Function to generate random post data
def generate_posts(num_users, min_posts, max_posts):
    captions = [
        "Having a great day!",
        "Exploring the outdoors.",
        "What a beautiful sunset!",
        "Just finished my workout.",
        "Loving this new hobby!",
        "Had the best meal ever.",
        "Life is good.",
        "Chasing dreams.",
        "Family time is the best time.",
        "Throwback to this amazing moment."
    ]
    
    sql_statements = []
    sql_statements.append(f"INSERT INTO post (user_id, caption, num_likes, num_com, num_shares, timestamp) VALUES")
    total_num_posts = 0
    for user_id in range(1, num_users + 1):
        num_posts = random.randint(min_posts, max_posts)
        for _ in range(num_posts):
            caption = random.choice(captions)
            num_likes = random.randint(0, 500)
            num_com = random.randint(0, 100)
            num_shares = random.randint(0, 50)
            random_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 2000))
            sql = (f"({user_id}, '{caption}', {num_likes}, {num_com}, {num_shares}, '{random_date.strftime('%Y-%m-%d %H:%M:%S')}'),")
            sql_statements.append(sql)
            total_num_posts+=1
    
    # Remove last comma
    sql_statements[-1] = sql_statements[-1][0:len(sql_statements[-1])-1]
    
    return sql_statements, total_num_posts

# Generate SQL insert statements
post_sql_statements, num_posts = generate_posts(200, 5, 20)

# Write to an SQL file
sql_file_path = "InsertPosts.sql"
with open(sql_file_path, "w") as file:
    file.write("-- SQL Statements to Populate Post Table\n")
    file.write("\n".join(post_sql_statements))

# Function to generate spam post data
def generate_spam_posts(num_users):
    captions = [
        "Having a great day!",
        "Exploring the outdoors.",
        "What a beautiful sunset!",
        "Just finished my workout.",
        "Loving this new hobby!",
        "Had the best meal ever.",
        "Life is good.",
        "Chasing dreams.",
        "Family time is the best time.",
        "Throwback to this amazing moment."
    ]
    
    sql_statements = []
    sql_statements.append(f"INSERT INTO post (user_id, caption, num_likes, num_com, num_shares, timestamp) VALUES")
    spam_users = random.sample(range(1, 201), num_users)
    for user_id in spam_users:
        random_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 2000))
        for _ in range(30):
            caption = random.choice(captions)
            num_likes = random.randint(0, 3)
            num_com = random.randint(0, 2)
            num_shares = random.randint(0, 2)
            sql = (f"({user_id}, '{caption}', {num_likes}, {num_com}, {num_shares}, '{random_date.strftime('%Y-%m-%d %H:%M:%S')}'),")
            sql_statements.append(sql)
    
    # Remove last comma
    sql_statements[-1] = sql_statements[-1][0:len(sql_statements[-1])-1]
    
    return sql_statements

# Generate SQL insert statements
post_sql_statements = generate_spam_posts(5)

# Write to an SQL file
sql_file_path = "SpamPosts.sql"
with open(sql_file_path, "w") as file:
    file.write("-- SQL Statements to Populate Spam Post Table\n")
    file.write("\n".join(post_sql_statements))

# Function to generate random messages
def generate_messages(num_users, min_messages, max_messages):
    sql_statements = []
    sql_statements.append(f"INSERT INTO message (from_user_id, to_user_id, text, timestamp) VALUES")
    count = 1
    for from_user_id in range(1, num_users + 1):
        num_messages = random.randint(min_messages, max_messages)
        for _ in range(num_messages):
            to_user_id = random.choice([i for i in range(1, num_users + 1) if i != from_user_id])
            text = f'normal message {count}'
            count+=1
            random_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 2000))
            sql = (f"({from_user_id}, {to_user_id}, '{text}', '{random_date.strftime('%Y-%m-%d %H:%M:%S')}'),")
            sql_statements.append(sql)

    # Remove last comma
    sql_statements[-1] = sql_statements[-1][0:len(sql_statements[-1])-1]

    return sql_statements

# Generate SQL insert statements
message_sql_statements = generate_messages(200, 5, 20)

# Write to an SQL file
sql_file_path = "InsertMessages.sql"
with open(sql_file_path, "w") as file:
    file.write("-- SQL Statements to Populate Message Table\n")
    file.write("\n".join(message_sql_statements))

# Function to generate spam messages
def generate_spam_messages(num_users):
    sql_statements = []
    sql_statements.append(f"INSERT INTO message (from_user_id, to_user_id, text, timestamp) VALUES")
    count = 1
    spam_users = random.sample(range(1, 201), num_users)
    for from_user_id in spam_users:
        for _ in range(30):
            to_user_id = random.choice([i for i in range(1, num_users + 1) if i != from_user_id])
            text = f'spam message from {from_user_id}'
            count+=1
            random_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 2000))
            sql = (f"({from_user_id}, {to_user_id}, '{text}', '{random_date.strftime('%Y-%m-%d %H:%M:%S')}'),")
            sql_statements.append(sql)

    # Remove last comma
    sql_statements[-1] = sql_statements[-1][0:len(sql_statements[-1])-1]

    return sql_statements

# Generate SQL insert statements
spam_message = generate_spam_messages(5)

# Write to an SQL file
sql_file_path = "SpamMessages.sql"
with open(sql_file_path, "w") as file:
    file.write("-- SQL Statements to Populate Spam Message Table\n")
    file.write("\n".join(spam_message))

# Function to generate random comments
def generate_comments(num_users, min_comments, max_comments):
    sql_statements = []
    sql_statements.append(f"INSERT INTO comment (post_id, user_id, text, timestamp) VALUES")
    count = 1
    for from_user_id in range(1, num_users + 1):
        num_comments = random.randint(min_comments, max_comments)
        for _ in range(num_comments):
            post_id = random.choice([i for i in range(1, num_posts)])
            text = f'normal comment {count}'
            count+=1
            random_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 2000))
            sql = (f"({post_id}, {from_user_id}, '{text}', '{random_date.strftime('%Y-%m-%d %H:%M:%S')}'),")
            sql_statements.append(sql)

    # Remove last comma
    sql_statements[-1] = sql_statements[-1][0:len(sql_statements[-1])-1]

    return sql_statements

# Generate SQL insert statements
comment_sql_statements = generate_comments(200, 5, 20)

# Write to an SQL file
sql_file_path = "InsertComments.sql"
with open(sql_file_path, "w") as file:
    file.write("-- SQL Statements to Populate comment Table\n")
    file.write("\n".join(comment_sql_statements))

# Function to generate spam comments
def generate_spam_comments(num_users):
    sql_statements = []
    sql_statements.append(f"INSERT INTO comment (post_id, user_id, text, timestamp) VALUES")
    count = 1
    spam_users = random.sample(range(1, 201), num_users)
    for from_user_id in spam_users:
        for _ in range(30):
            post_id = random.choice([i for i in range(1, num_posts)])
            text = f'spam comment from {from_user_id}'
            count+=1
            random_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 2000))
            sql = (f"({post_id}, {from_user_id}, '{text}', '{random_date.strftime('%Y-%m-%d %H:%M:%S')}'),")
            sql_statements.append(sql)

    # Remove last comma
    sql_statements[-1] = sql_statements[-1][0:len(sql_statements[-1])-1]

    return sql_statements

# Generate SQL insert statements
spam_comment = generate_spam_comments(5)

# Write to an SQL file
sql_file_path = "SpamComments.sql"
with open(sql_file_path, "w") as file:
    file.write("-- SQL Statements to Populate Spam comment Table\n")
    file.write("\n".join(spam_comment))

# Function to generate report data
def generate_reports(num_users, heavy_report_users, num_heavy_reports, total_reports):
    reasons = [
        "Inappropriate content",
        "Spam",
        "Harassment",
        "Fake profile",
        "Hate speech",
        "Scam or fraud",
        "Other",
    ]

    sql_statements = []
    sql_statements.append(f"INSERT INTO report (source_id, user_id, date, reason) VALUES")
    report_count = 0

    # Add heavy reports for specified users
    for user_id in heavy_report_users:
        for _ in range(num_heavy_reports):
            source_id = random.choice([i for i in range(1, num_users + 1) if i != user_id])
            reason = random.choice(reasons)
            random_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 2000))
            sql = (f"({source_id}, {user_id}, '{random_date.strftime('%Y-%m-%d %H:%M:%S')}', '{reason}'),")
            sql_statements.append(sql)
            report_count += 1

    # Add remaining random reports
    remaining_reports = total_reports - report_count
    for _ in range(remaining_reports):
        user_id = random.randint(1, num_users)
        source_id = random.choice([i for i in range(1, num_users + 1) if i != user_id])
        reason = random.choice(reasons)
        random_date = datetime.datetime(2023, 1, 1) + datetime.timedelta(
            days=random.randint(0, 364),
            seconds=random.randint(0, 86399)
        )
        sql = (f"({source_id}, {user_id}, '{random_date.strftime('%Y-%m-%d %H:%M:%S')}', '{reason}'),")
        sql_statements.append(sql)
    
    # Remove last comma
    sql_statements[-1] = sql_statements[-1][0:len(sql_statements[-1])-1]

    return sql_statements

# Generate SQL insert statements
heavy_report_users = random.sample(range(1, 201), 5)  # Select 10 users with 10+ reports
num_heavy_reports = 10  # Reports per heavy user
total_reports = 200  # Total number of reports

report_sql_statements = generate_reports(200, heavy_report_users, num_heavy_reports, total_reports)

# Write to an SQL file
sql_file_path = "InsertReports.sql"
with open(sql_file_path, "w") as file:
    file.write("-- SQL Statements to Populate Report Table\n")
    file.write("\n".join(report_sql_statements))
