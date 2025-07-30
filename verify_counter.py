#!/usr/bin/env python3
"""
Quick verification script to check the counter value
"""

import os
from supabase import create_client, Client
import toml

def load_secrets():
    """Load secrets from .streamlit/secrets.toml"""
    secrets_path = ".streamlit/secrets.toml"
    if os.path.exists(secrets_path):
        secrets = toml.load(secrets_path)
        return secrets.get("SUPABASE_URL"), secrets.get("SUPABASE_KEY")
    else:
        raise FileNotFoundError(f"Secrets file not found at {secrets_path}")

def verify_counter():
    """Verify the counter value"""
    try:
        # Load secrets
        supabase_url, supabase_key = load_secrets()
        
        # Create Supabase client
        supabase: Client = create_client(supabase_url, supabase_key)
        
        # Get current counter value
        result = supabase.table('scan_counter').select('counter_value').single().execute()
        current_value = result.data['counter_value']
        
        print(f"📊 Current counter value: {current_value}")
        
        if current_value == 240:
            print("✅ Counter successfully updated to 240!")
            return True
        else:
            print(f"❌ Counter value is {current_value}, expected 240")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Verifying counter value...")
    success = verify_counter()
    if success:
        print("🎉 Counter verification completed successfully!")
    else:
        print("❌ Counter verification failed.") 