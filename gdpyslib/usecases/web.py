import aiohttp

# Geometry Dash firewall bypass.
_BYPASS_HEADERS = (
    "User-Agent",
    "Accept-Encoding",
)
_session = aiohttp.ClientSession(
    skip_auto_headers=_BYPASS_HEADERS,
)

async def post_boomlings(endpoint: str, data: dict) -> str:
    """Sends a POST request to `http://www.boomlings.com/database/{endpoint}`
    with `data` as POST data and returns the result text."""

    url = f"http://www.boomlings.com/database/{endpoint}"
    async with _session as session:
        async with session.post(url, data= data) as request:
            return await request.text()

def parse_gd_dict(response: str, separator: str = ":") -> dict[int, str]:
    """Parses a Geometry Dash dict response format into a `dict`."""

    # Funky but only way I have found so far to use the same iterator twice
    # per iteration.
    return {
        int(key): val
        for key, val in zip(*[iter(
            response.split(separator)
        )] * 2)
    }
