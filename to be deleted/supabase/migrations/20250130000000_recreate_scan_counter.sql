-- Recreate scan_counter table
-- This migration recreates the scan_counter table that was accidentally removed

-- Drop the table if it exists (to ensure clean recreation)
DROP TABLE IF EXISTS scan_counter;

-- Create the scan_counter table with proper structure
CREATE TABLE scan_counter (
    id SERIAL PRIMARY KEY,
    counter_value INTEGER NOT NULL DEFAULT 141
);

-- Insert initial counter value
INSERT INTO scan_counter (id, counter_value) VALUES (1, 141);

-- Add RLS (Row Level Security) policy to allow anonymous access for the application
ALTER TABLE scan_counter ENABLE ROW LEVEL SECURITY;

-- Create policy to allow anonymous users to read and update the counter
CREATE POLICY "Allow anonymous access to scan_counter" ON scan_counter
    FOR ALL USING (true)
    WITH CHECK (true);

-- Grant necessary permissions
GRANT ALL ON scan_counter TO anon;
GRANT ALL ON scan_counter TO authenticated;
GRANT USAGE, SELECT ON SEQUENCE scan_counter_id_seq TO anon;
GRANT USAGE, SELECT ON SEQUENCE scan_counter_id_seq TO authenticated; 