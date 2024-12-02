-- Mass Following --
SELECT 
    c.follower_id AS follower_id,
    u.username AS follower_username,
    COUNT(c.followed_id) AS total_followed,
    COUNT(DISTINCT DATE(c.timestamp)) AS unique_follow_days,
    MIN(c.timestamp) AS first_follow_time,
    MAX(c.timestamp) AS last_follow_time,
    DATEDIFF(MAX(c.timestamp), MIN(c.timestamp)) + 1 AS following_duration_days,
    COUNT(c.followed_id) / (DATEDIFF(MAX(c.timestamp), MIN(c.timestamp)) + 1) AS avg_follows_per_day
FROM 
    connections c
JOIN 
    user u ON c.follower_id = u.user_id
GROUP BY 
    c.follower_id
HAVING 
    -- threshold for number of users followed
    COUNT(c.followed_id) > 1
    -- threshold for followed/day
    AND COUNT(c.followed_id) / (DATEDIFF(MAX(c.timestamp), MIN(c.timestamp)) + 1) > 1
ORDER BY 
    total_followed DESC, avg_follows_per_day DESC, following_duration_days ASC;

-- Mass Posting --
SELECT 
    p.user_id AS poster_id,
    u.username AS poster_username,
    COUNT(p.post_id) AS total_posts,
    COUNT(DISTINCT DATE(p.timestamp)) AS unique_post_days,
    MIN(p.timestamp) AS first_post_time,
    MAX(p.timestamp) AS last_post_time,
    DATEDIFF(MAX(p.timestamp), MIN(p.timestamp)) + 1 AS posting_duration_days,
    COUNT(p.post_id) / (DATEDIFF(MAX(p.timestamp), MIN(p.timestamp)) + 1) AS avg_posts_per_day
FROM 
    post p
JOIN 
    user u ON p.user_id = u.user_id
GROUP BY 
    p.user_id
HAVING 
    -- threshold for number of posts
    COUNT(p.post_id) > 1
    -- threshold for posts/day
    AND COUNT(p.post_id) / (DATEDIFF(MAX(p.timestamp), MIN(p.timestamp)) + 1) > 1
ORDER BY 
    total_posts DESC, avg_posts_per_day DESC, posting_duration_days ASC;

-- Repetitive Messages to Many Accounts --
SELECT 
    m.from_user_id AS sender_id,
    sender.username AS sender_username,
    m.text AS repetitive_message,
    COUNT(m.message_id) AS total_repetitive_messages,
    COUNT(DISTINCT m.to_user_id) AS unique_recipients,
    MIN(m.timestamp) AS first_sent_time,
    MAX(m.timestamp) AS last_sent_time
FROM 
    message m
JOIN 
    user sender ON m.from_user_id = sender.user_id
GROUP BY 
    m.from_user_id, m.text
HAVING 
    -- threshold for number of distinct recepients
    COUNT(DISTINCT m.to_user_id) > 1
    -- threshold for number of repeated message
    AND COUNT(m.message_id) > 1
ORDER BY 
    total_repetitive_messages DESC, unique_recipients DESC, first_sent_time ASC;

-- Same Commment on Multiple Posts --
SELECT 
    c.user_id AS commenter_id,
    u.username AS commenter_username,
    c.text AS comment_text,
    COUNT(DISTINCT c.post_id) AS unique_posts_commented_on,
    COUNT(c.comment_id) AS total_comments_made,
    GROUP_CONCAT(DISTINCT c.post_id ORDER BY c.post_id) AS commented_post_ids,
    MIN(c.timestamp) AS first_comment_time,
    MAX(c.timestamp) AS last_comment_time,
    DATEDIFF(MAX(c.timestamp), MIN(c.timestamp)) + 1 AS comment_duration_days,
    COUNT(c.comment_id) / (DATEDIFF(MAX(c.timestamp), MIN(c.timestamp)) + 1) AS avg_comments_per_day
FROM 
    comment c
JOIN 
    user u ON c.user_id = u.user_id
GROUP BY 
    c.user_id, c.text
HAVING
    -- threshold for distinct posts commented on --
    COUNT(DISTINCT c.post_id) > 5
    -- threshold for number of comments with same text
    AND COUNT(c.comment_id) > 5
    -- threshold for average comments/day
    AND COUNT(c.comment_id) / (DATEDIFF(MAX(c.timestamp), MIN(c.timestamp)) + 1) > 2
ORDER BY 
    unique_posts_commented_on DESC, total_comments_made DESC, comment_duration_days ASC;

-- Frequent Reports --
SELECT 
    u.user_id,
    u.username,
    COUNT(r.report_id) AS total_reports,
    COUNT(DISTINCT r.source_id) AS distinct_reporters,
    MAX(r.date) AS last_report_date,
    MIN(r.date) AS first_report_date,
    MAX(reason) AS most_common_reason
FROM 
    report r
JOIN 
    user u ON r.user_id = u.user_id
GROUP BY 
    u.user_id, u.username
HAVING 
    -- threhold for number of reports
    COUNT(r.report_id) > 1
ORDER BY 
    total_reports DESC, distinct_reporters DESC;
