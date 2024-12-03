DROP TABLE IF EXISTS comment;
DROP TABLE IF EXISTS tagged_users;
DROP TABLE IF EXISTS message;
DROP TABLE IF EXISTS report;
DROP TABLE IF EXISTS connections;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS user;

-- Table for Users
CREATE TABLE user (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    profile_name VARCHAR(100),
    date_created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    following INT DEFAULT 0,
    followers INT DEFAULT 0
);

-- Table for Posts
CREATE TABLE post (
    post_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    caption TEXT,
    num_likes INT DEFAULT 0,
    num_com INT DEFAULT 0,
    num_shares INT DEFAULT 0,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- Table for Comments
CREATE TABLE comment (
    comment_id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    text TEXT,
    likes INT DEFAULT 0,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES post(post_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- Table for Messages
CREATE TABLE message (
    message_id INT PRIMARY KEY AUTO_INCREMENT,
    from_user_id INT NOT NULL,
    to_user_id INT NOT NULL,
    text TEXT,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_user_id) REFERENCES user(user_id),
    FOREIGN KEY (to_user_id) REFERENCES user(user_id)
);

-- Table for Reports
CREATE TABLE report (
    report_id INT PRIMARY KEY AUTO_INCREMENT,
    source_id INT NOT NULL,
    user_id INT NOT NULL,
    date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    reason TEXT,
    FOREIGN KEY (source_id) REFERENCES user(user_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- Table for Connections (Follows)
CREATE TABLE connections (
    followed_id INT NOT NULL,
    follower_id INT NOT NULL,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (followed_id, follower_id),
    FOREIGN KEY (followed_id) REFERENCES user(user_id),
    FOREIGN KEY (follower_id) REFERENCES user(user_id)
);

-- Table for Tagged Users (in Posts)
CREATE TABLE tagged_users (
	post_id INT NOT NULL,
	user_id INT NOT NULL,
	timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (post_id, user_id),
	FOREIGN KEY (post_id) REFERENCES post(post_id),
	FOREIGN KEY (user_id) REFERENCES user(user_id)
);