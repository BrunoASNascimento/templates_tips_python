import json
from dataclasses import dataclass, field

from fastapi import FastAPI, HTTPException, Response

app = FastAPI()


@dataclass
class Channel:
    id: str
    name: str
    tags: list[str] = field(default_factory=list)
    description: str = ""


channels: dict[str, Channel] = {}

with open("data/channels.json", encoding="utf8") as file:
    channels_raw = json.load(file)
    for channel_raw in channels_raw:
        channel = Channel(**channel_raw)
        channels[channel.id] = channel


@app.get("/")
def read_root() -> Response:
    """
    Get the root endpoint.

    :return: The server is running
    :rtype: Response
    """
    return Response("The server is running!", status_code=200)


@app.get("/channels/{channel_id}", response_model=Channel)
def read_item(channel_id: str) -> Channel:
    """
    Retrieves a channel by its ID.

    Parameters:
        channel_id (str): The ID of the channel to retrieve.

    Returns:
        Channel: The retrieved channel.

    Raises:
        HTTPException: If the channel with the specified ID is not found.
    """
    if channel_id not in channels:
        raise HTTPException(status_code=404, detail="Channel not found")
    return channels[channel_id]
