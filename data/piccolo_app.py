from piccolo.conf.apps import AppConfig
from data.models.configuration import Configuration
from data.models.guild import Guild
from data.models.tournament import Tournament


APP_CONFIG = AppConfig(
    app_name="war_games",
    migrations_folder_path="data/migrations",
    table_classes=[Guild, Configuration, Tournament],
    migration_dependencies=[],
    commands=[],
)
