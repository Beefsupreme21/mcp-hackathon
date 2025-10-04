#!/usr/bin/env python3
"""
Test script to generate curl commands for Strava API
"""

import os
from dotenv import load_dotenv

def generate_curl_commands():
    """Generate curl commands for testing Strava API"""
    
    # Load environment variables from .env file
    load_dotenv()
    
    print("🔧 Strava API Curl Commands")
    print("=" * 50)
    
    # Get values from environment variables
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    
    if not all([CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN]):
        print("❌ Missing environment variables!")
        print("Please check your .env file contains:")
        print("- CLIENT_ID")
        print("- CLIENT_SECRET") 
        print("- ACCESS_TOKEN")
        return
    
    # Show loaded credentials (with masking for security)
    print(f"✅ Loaded credentials:")
    print(f"   CLIENT_ID: {CLIENT_ID}")
    print(f"   CLIENT_SECRET: {CLIENT_SECRET[:8]}...")
    print(f"   ACCESS_TOKEN: {ACCESS_TOKEN[:8]}...")
    
    print("\n1️⃣ Get Access Token (Client Credentials):")
    print("─" * 40)
    print(f'''curl -X POST "https://www.strava.com/api/v3/oauth/token" \\
  -H "Content-Type: application/x-www-form-urlencoded" \\
  -d "client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials&scope=read"''')
    
    print("\n2️⃣ Get Athlete Profile:")
    print("─" * 40)
    print(f'''curl -X GET "https://www.strava.com/api/v3/athlete" \\
  -H "Authorization: Bearer {ACCESS_TOKEN}" \\
  -H "Content-Type: application/json"''')
    
    print("\n3️⃣ Get Recent Activities (default - last 30):")
    print("─" * 40)
    print(f'''curl -X GET "https://www.strava.com/api/v3/athlete/activities?per_page=20&page=1" \\
  -H "Authorization: Bearer {ACCESS_TOKEN}" \\
  -H "Content-Type: application/json"''')
    
    print("\n4️⃣ Get Activities with Date Range:")
    print("─" * 40)
    print(f'''curl -X GET "https://www.strava.com/api/v3/athlete/activities?before=$(date +%s)&after=$(date -d '7 days ago' +%s)&per_page=10" \\
  -H "Authorization: Bearer {ACCESS_TOKEN}" \\
  -H "Content-Type: application/json"''')
    
    print("\n5️⃣ Get Specific Activity:")
    print("─" * 40)
    print(f'''curl -X GET "https://www.strava.com/api/v3/activities/123456789" \\
  -H "Authorization: Bearer {ACCESS_TOKEN}" \\
  -H "Content-Type: application/json"''')
    
    print("\n🎯 Setup Steps:")
    print("=" * 50)
    print("1. Go to https://www.strava.com/settings/api")
    print("2. Create an application to get CLIENT_ID and CLIENT_SECRET")
    print("3. Replace YOUR_CLIENT_ID, YOUR_CLIENT_SECRET in commands above")
    print("4. Run the first command to get an access token")
    print("5. Replace YOUR_ACCESS_TOKEN with the token from step 4")
    print("6. Use commands 2-5 to interact with Strava data")
    
    print("\n💡 Tips:")
    print("─" * 40)
    print("• Use 'jq' to format JSON responses: ... | jq")
    print("• Save token to file: token_response.json")
    print("• Check rate limits in response headers")

if __name__ == "__main__":
    generate_curl_commands()
