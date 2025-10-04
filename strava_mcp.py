#!/usr/bin/env python3
"""
Strava MCP Server - A basic MCP server for Strava integration
"""

from mcp.server import FastMCP


# Create the MCP server
app = FastMCP("strava-mcp")


@app.tool()
def get_strava_activities(limit: int = 10) -> str:
    """Get recent Strava activities (hardcoded for now)
    
    Args:
        limit: Maximum number of activities to return (default: 10)
    """
    # Hardcoded sample activities
    activities = [
        {
            "id": "12345",
            "name": "Morning Run",
            "type": "Run",
            "distance": "5.2 km",
            "moving_time": "25:30",
            "date": "2024-01-15T08:00:00Z",
            "description": "Beautiful morning run through the park"
        },
        {
            "id": "12346", 
            "name": "Cycling Commute",
            "type": "Ride",
            "distance": "12.8 km",
            "moving_time": "42:15",
            "date": "2024-01-14T18:30:00Z",
            "description": "Daily commute to work"
        },
        {
            "id": "12347",
            "name": "Weekend Hike",
            "type": "Hike", 
            "distance": "8.5 km",
            "moving_time": "2:15:30",
            "date": "2024-01-13T10:00:00Z",
            "description": "Mountain trail exploration"
        }
    ]
    
    # Limit results
    limited_activities = activities[:limit]
    
    # Format as readable text
    activity_list = []
    for activity in limited_activities:
        activity_text = f"""
📈 **{activity['name']}**
   Type: {activity['type']}
   Distance: {activity['distance']}
   Time: {activity['moving_time']}
   Date: {activity['date']}
   Description: {activity['description']}
   ID: {activity['id']}
"""
        activity_list.append(activity_text.strip())
    
    result_text = f"""
🏃‍♂️ **Recent Strava Activities** (showing {len(limited_activities)} activities)

{chr(10).join(activity_list)}
"""
    
    return result_text


def main():
    """Main entry point"""
    print("🚀 Starting Strava MCP Server...")
    print("📡 Server will run on stdio interface")
    print("🔧 Available tools: get_strava_activities")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Run the server
    app.run()


if __name__ == "__main__":
    main()