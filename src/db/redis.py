from src.config import Config
import redis.asyncio as aioredis

JTI_EXPIRY = 3600

# Create a Redis connection
token_blocklist = aioredis.from_url(
    Config.REDIS_URL
)

async def add_jti_to_blocklist(jti: str) -> None:
    await token_blocklist.set(name=jti, ex=JTI_EXPIRY, value="blocked")

async def token_in_blocklist(jti: str) -> bool:
    result = await token_blocklist.get(jti)
    return result is not None

# admin
[
    "adding users",
    "change roles",
    "crud on users",
    "book submissions",
    "curd on users",
    "crud on reviews",
    "revoking access"
]

# users
[ "crud on their own book submissions", "crud on their reviews", "crud on their own accounts" ]  