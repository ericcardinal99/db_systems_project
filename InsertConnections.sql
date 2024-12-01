-- Trigger to update counts after a new connection is added
CREATE TRIGGER after_connection_insert
AFTER INSERT ON connections
FOR EACH ROW
BEGIN
    -- Increment the following count for the follower
    UPDATE user SET following = following + 1 WHERE user_id = NEW.follower_id;

    -- Increment the followers count for the followed user
    UPDATE user SET followers = followers + 1 WHERE user_id = NEW.followed_id;
END;

-- Trigger to update counts after a connection is removed
CREATE TRIGGER after_connection_delete
AFTER DELETE ON connections
FOR EACH ROW
BEGIN
    -- Decrement the following count for the follower
    UPDATE user SET following = following - 1 WHERE user_id = OLD.follower_id;

    -- Decrement the followers count for the followed user
    UPDATE user SET followers = followers - 1 WHERE user_id = OLD.followed_id;
END;

