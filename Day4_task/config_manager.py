# Task 06: JSON Config Manager
# Builds a config manager to save, load, and update JSON configuration files.

import json

def save_config(data: dict, filename: str) -> None:
    """Writes a dictionary to a JSON file with readable indentation."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Config saved to '{filename}'.")


def load_config(filename: str) -> dict:
    """Reads a JSON file and returns its contents as a dictionary."""
    with open(filename, "r") as f:
        data = json.load(f)
    print(f"Config loaded from '{filename}'.")
    return data


def update_config(filename: str, key: str, value) -> None:
    """Loads a JSON config, updates a single key, and saves it back."""
    data = load_config(filename)
    old_value = data.get(key, "N/A")
    data[key] = value
    save_config(data, filename)
    print(f"Updated '{key}': {old_value} → {value}")


# Test the config manager 
if __name__ == "__main__":
    config_file = "ml_config.json"

    # Create initial config
    initial_config = {
        "model":         "linear_regression",
        "learning_rate": 0.01,
        "epochs":        10
    }

    print(" Saving initial config ")
    save_config(initial_config, config_file)

    print("\n Loading config ")
    loaded = load_config(config_file)
    print("Contents:", loaded)

    print("\n Updating 'epochs' to 20 ")
    update_config(config_file, "epochs", 20)

    print("\n Final config after update ")
    final = load_config(config_file)
    print("Contents:", final)

# json.dumps() → converts a Python dict to a JSON-formatted STRING (in memory, not to a file).
# json.dump()  → writes a Python dict directly to a FILE object as JSON (needs open() file handle).