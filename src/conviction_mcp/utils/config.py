"""Load and validate config.yaml."""

from pathlib import Path
import yaml

CONFIG_PATH = Path(__file__).parents[3] / "data" / "config.yaml"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Config file not found at {CONFIG_PATH}. "
            "Copy config.example.yaml to data/config.yaml and fill in your credentials."
        )
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)
