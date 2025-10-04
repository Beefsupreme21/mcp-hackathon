#!/usr/bin/env python3
"""
Simple script to run the Strava MCP server
"""

import subprocess
import sys
import os

def main():
    """Run the Strava MCP server"""
    
    # Check if we're in a virtual environment or if requirements are installed
    try:
        import mcp
        print("✓ MCP dependencies found")
    except ImportError:
        print("❌ MCP dependencies not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✓ Dependencies installed")
    
    # Run the server
    print("🚀 Starting Strava MCP Server...")
    print("📡 Server will run on stdio interface")
    print("🔧 Available tools: get_strava_activities")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        subprocess.run([sys.executable, "strava_mcp.py"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error running server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
