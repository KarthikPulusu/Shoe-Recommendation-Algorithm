
-- User Profiles
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    age INT NOT NULL,
    gender VARCHAR(10),
    typical_usage VARCHAR(50),
    preferred_weather VARCHAR(20),
    region VARCHAR(100)
);

-- Shoe Catalog
CREATE TABLE shoes (
    shoe_id SERIAL PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(50),
    type VARCHAR(50),
    material VARCHAR(50),
    color VARCHAR(30),
    size NUMERIC(4,1),
    care_level VARCHAR(20),
    weather_suitability VARCHAR(20)
);

-- User Interactions / History
CREATE TABLE interactions (
    interaction_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    shoe_id INT REFERENCES shoes(shoe_id) ON DELETE CASCADE,
    interaction_type VARCHAR(20), -- view, purchase, wishlist, etc.
    interaction_date DATE NOT NULL
);

-- Device-based Shoe Care History (Optional extension)
CREATE TABLE shoe_care_logs (
    care_log_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    shoe_id INT REFERENCES shoes(shoe_id) ON DELETE CASCADE,
    care_mode VARCHAR(50),
    care_date DATE NOT NULL,
    frequency INT 
);

-- Recommendation Results / Logs (optional but useful)
CREATE TABLE recommendation_logs (
    rec_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    shoe_id INT REFERENCES shoes(shoe_id) ON DELETE CASCADE,
    score NUMERIC(5,2),
    rec_type VARCHAR(20), -- content_based, collaborative, hybrid, etc.
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
