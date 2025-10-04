#!/usr/bin/env python3
"""
Test script to verify the Strava MCP server setup
"""

import asyncio
from strava_mcp import app


async def test_mcp():
    """Test the MCP server functionality"""
    print("🧪 Testing Strava MCP Server...")
    
    try:
        # Test the tool function directly
        print("\n📊 Testing get_strava_activities function...")
        result = await app.call_tool("get_strava_activities", {"limit": 2})
        
        print("✅ Function executed successfully!")
        print(f"📄 Output type: {type(result)}")
        
        print("\n📋 Sample output:")
        print("-" * 50)
        print(result)
        print("-" * 50)
        
        print("\n🎉 All tests passed! MCP server is ready to run.")
        print("\n💡 Next steps:")
        print("   1. Run: python run_server.py")
        print("   2. Connect with an MCP client")
        print("   3. Call get_strava_activities tool")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = asyncio.run(test_mcp())
    if not success:
        exit(1)