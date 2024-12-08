-- Create indices for database
CREATE INDEX idx_user_post ON post(user_id);
CREATE INDEX idx_post_comments ON comment(post_id);
CREATE INDEX idx_user_comments ON comment(user_id);
CREATE INDEX idx_message_thread ON message(from_user_id, to_user_id);
CREATE INDEX idx_reported_user ON report(user_id);
CREATE INDEX idx_follows ON connections(follower_id);