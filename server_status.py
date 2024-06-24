import a2s
import time

# Server addresses with keys
servers = {
    "Gmod": [("gmodttt.steam-gamers.net", 27015)],
    "CS2": [
        ("retakes.steam-gamers.net", 27015),
        ("bhop.steam-gamers.net", 27015),
        ("surf.steam-gamers.net", 27015),
    ],
    "VRising": [("135.148.3.9", 9877)],
}

# Global variable to store server info cache
server_info_cache = {}


def query_server(address):
    try:
        info = a2s.info(address)
        players = a2s.players(address)
        player_list = [
            {"name": player.name, "score": player.score} for player in players
        ]
        return {
            "server_name": info.server_name,
            "map": info.map_name,
            "players": info.player_count,
            "max_players": info.max_players,
            "player_list": player_list,
        }
    except Exception as e:
        return {"error": str(e)}


def update_server_info():
    global server_info_cache
    while True:
        server_info_cache = {
            key: {
                f"{address[0]}:{address[1]}": query_server(address)
                for address in addresses
            }
            for key, addresses in servers.items()
        }
        time.sleep(60)  # Wait for 60 seconds before the next update
