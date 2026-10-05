from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import BigInt
from piccolo.columns.column_types import Timestamptz
from piccolo.columns.defaults.timestamptz import TimestamptzNow
from piccolo.columns.indexes import IndexMethod

ID = "2026-10-05T16:23:28:470599"
VERSION = "1.36.0"
DESCRIPTION = "Initial migration"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="wg", description=DESCRIPTION
    )

    manager.add_table(
        class_name="Guild", tablename="guild", schema=None, columns=None
    )

    manager.add_column(
        table_class_name="Guild",
        tablename="guild",
        column_name="created_at",
        db_column_name="created_at",
        column_class_name="Timestamptz",
        column_class=Timestamptz,
        params={
            "default": TimestamptzNow(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Guild",
        tablename="guild",
        column_name="modified_at",
        db_column_name="modified_at",
        column_class_name="Timestamptz",
        column_class=Timestamptz,
        params={
            "default": TimestamptzNow(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Guild",
        tablename="guild",
        column_name="guild_id",
        db_column_name="guild_id",
        column_class_name="BigInt",
        column_class=BigInt,
        params={
            "default": 0,
            "null": False,
            "primary_key": True,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Guild",
        tablename="guild",
        column_name="joined_at",
        db_column_name="joined_at",
        column_class_name="Timestamptz",
        column_class=Timestamptz,
        params={
            "default": TimestamptzNow(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Guild",
        tablename="guild",
        column_name="left_at",
        db_column_name="left_at",
        column_class_name="Timestamptz",
        column_class=Timestamptz,
        params={
            "default": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    return manager
