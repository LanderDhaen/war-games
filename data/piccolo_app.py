from piccolo.conf.apps import AppConfig
from data.models.configuration import Configuration
from data.models.guild import Guild


APP_CONFIG = AppConfig(
    app_name="wg",
    migrations_folder_path="data/migrations",
    table_classes=[Guild, Configuration],
    migration_dependencies=[],
    commands=[],
)
