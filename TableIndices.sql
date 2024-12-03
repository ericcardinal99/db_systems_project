-- Create indices for database
CREATE INDEX idx_user_post ON post(user_id);
CREATE INDEX idx_post_comments ON comment(post_id);
CREATE INDEX idx_message_thread ON message(from_user_id, to_user_id);
CREATE INDEX idx_reported_user ON report(user_id);
CREATE INDEX idx_follows ON connections(follower_id);

-- Demonstrate use of index on user_id in post table
EXPLAIN (
SELECT * 
FROM post 
USE INDEX (idx_user_post)
WHERE user_id = 50
);

EXPLAIN (
SELECT * 
FROM post
IGNORE INDEX (idx_user_post)
WHERE user_id = 50
);

-- Demonstrate use of index on from_user_id and to_user_id in message table
EXPLAIN (
SELECT * 
FROM message 
USE INDEX (idx_message_thread)
WHERE from_user_id = 64 AND to_user_id = 62
);

EXPLAIN (
SELECT * 
FROM message
IGNORE INDEX (idx_message_thread)
WHERE from_user_id = 64 AND to_user_id = 62
);

-- Demonstrate use of index on follower_id in connections table
EXPLAIN (
SELECT * 
FROM connections 
USE INDEX (idx_follows)
WHERE user_id = 50
);

EXPLAIN (
SELECT * 
FROM connections
IGNORE INDEX (idx_follows)
WHERE user_id = 50
);