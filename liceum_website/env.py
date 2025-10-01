import os

import environ

ROOT_DIR = environ.Path(__file__) - 2

env = environ.Env()

env_file = str(ROOT_DIR.path('.env'))

if os.path.exists(env_file):
    env.read_env(env_file)
