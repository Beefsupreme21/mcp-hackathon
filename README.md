# Strava MCP Server

A Model Context Protocol (MCP) server that provides Strava activity data to Cursor AI. Currently uses sample data, but easily extensible for real Strava API integration.

## 🤖 Add to Cursor

**The configuration has been automatically added to your Cursor MCP settings!**

If you need to add it manually or on another machine:

1. Open `~/.cursor/mcp.json` in a text editor
2. Replace the content with:

```json
{
  "mcpServers": {
    "strava": {
      "command": "python",
      "args": ["/Users/dylanmelotik/Code/melotik/mcp-hackathon/strava_mcp.py"],
      "env": {}
    }
  }
}
```

3. **Restart Cursor** for changes to take effect

## 🚀 Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Test the server:**
   ```bash
   python strava_mcp.py
   ```

## 🛠️ Available Tools

- **`get_strava_activities`** - Get recent Strava activities (sample data)
  - `limit` parameter (default: 10) - max number of activities to return

## Usage in Cursor

Once configured, you can ask Cursor: *"Show me my recent Strava activities"* and it will use the MCP server to return formatted activity data including:

- Activity name and type
- Distance and time  
- Date and description
- Activity ID

## 🔧 For Real Strava Integration

To connect to the actual Strava API:

1. Register at https://www.strava.com/settings/api
2. Replace the hardcoded activities in `get_strava_activities()` with real API calls
3. Add authentication handling

## License

MIT License - feel free to use and modify!
