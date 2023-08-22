from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "bet" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "amount" DOUBLE PRECISION,
    "state" SMALLINT NOT NULL,
    "event_uuid" VARCHAR(255)
);
COMMENT ON COLUMN "bet"."state" IS 'PENDING: 1\nFINISHED_WIN: 2\nFINISHED_LOSE: 3';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
