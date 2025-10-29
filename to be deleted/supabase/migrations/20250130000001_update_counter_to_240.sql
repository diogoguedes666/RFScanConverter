-- Update scan_counter to start at 240
-- This migration updates the counter value to where it stopped

-- Update the counter value to 240
UPDATE scan_counter SET counter_value = 240 WHERE id = 1;

-- If no record exists, insert one with value 240
INSERT INTO scan_counter (id, counter_value) 
VALUES (1, 240) 
ON CONFLICT (id) DO UPDATE SET counter_value = 240; 