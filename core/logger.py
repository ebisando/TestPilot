import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("TestPilot")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# Console
console = logging.StreamHandler()
console.setFormatter(formatter)

# File
file = logging.FileHandler(
    "logs/testpilot.log",
    mode="w"
)
file.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file)