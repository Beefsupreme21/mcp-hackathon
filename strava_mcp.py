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
    # Hardcoded sample activities for half marathon training in Denver
    activities = [
        {
            "id": "98765",
            "name": "Long Run Training",
            "type": "Run",
            "distance": "16.1 km",
            "moving_time": "1:45:30",
            "date": "2024-01-20T08:00:00Z",
            "description": "Half marathon training - building endurance. Cherry Creek Trail to downtown Denver and back. Felt strong despite the cold!"
        },
        {
            "id": "98764", 
            "name": "Tempo Run - Wash Park",
            "type": "Run",
            "distance": "8.0 km",
            "moving_time": "38:45",
            "date": "2024-01-19T17:30:00Z",
            "description": "Tempo training around Washington Park. Maintained 7:40/mile pace - felt challenging but manageable."
        },
        {
            "id": "98763",
            "name": "Recovery Run",
            "type": "Run", 
            "distance": "5.6 km",
            "moving_time": "32:15",
            "date": "2024-01-18T06:45:00Z",
            "description": "Easy recovery run through City Park. Focused on form and staying relaxed."
        },
        {
            "id": "98762",
            "name": "Track Intervals",
            "type": "Run",
            "distance": "6.4 km",
            "moving_time": "35:20",
            "date": "2024-01-16T19:00:00Z",
            "description": "Track workout at East High School. 6x800m @ 3:20 pace with 400m recovery. Denver altitude is tough!"
        },
        {
            "id": "98761",
            "name": "Hill Workout - Lookout Mountain",
            "type": "Run",
            "distance": "7.8 km",
            "moving_time": "52:30",
            "date": "2024-01-14T07:00:00Z",
            "description": "Hill repeats up Lookout Mountain Road. Built strength and confidence on climbs. Beautiful sunrise over the Rockies."
        },
        {
            "id": "98760",
            "name": "Easy Run - Platte River Trail",
            "type": "Run",
            "distance": "6.8 km",
            "moving_time": "41:15",
            "date": "2024-01-12T17:45:00Z",
            "description": "Relaxed run along South Platte River Trail. Perfect weather for January in Denver!"
        },
        {
            "id": "98759",
            "name": "Long Run Progress",
            "type": "Run",
            "distance": "14.5 km",
            "moving_time": "1:38:42",
            "date": "2024-01-10T08:30:00Z",
            "description": "Progression long run - easy for first 10k, picked up pace for final 5k. Starting to feel ready for half marathon distance!"
        },
        {
            "id": "98758",
            "name": "Fartlek Training",
            "type": "Run",
            "distance": "7.2 km",
            "moving_time": "39:50",
            "date": "2024-01-08T18:00:00Z",
            "description": "Play Fartlek run in Cheesman Park. 15x1min hard/1min easy. Enjoyed the freedom of unstructured speed work."
        },
        {
            "id": "98757",
            "name": "Recovery Mileage",
            "type": "Run",
            "distance": "4.8 km",
            "moving_time": "28:45",
            "date": "2024-01-06T07:15:00Z",
            "description": "Short recovery run before weekend long run. Focused on breathing and staying relaxed despite cold temps."
        },
        {
            "id": "98756",
            "name": "Park Run Denver",
            "type": "Run",
            "distance": "5.0 km",
            "moving_time": "22:30",
            "date": "2024-01-04T09:00:00Z",
            "description": "5K Park Run at Civic Center Park. Great community event and good baseline fitness check. Aiming for sub-20 in race!"
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