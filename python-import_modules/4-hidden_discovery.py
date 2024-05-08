#!/usr/bin/python3

import importlib.util
import os


module_name = "hidden_4"
module_path = "hidden_4.pyc"

spec = importlib.util.spec_from_file_location(module_name, module_path)
hidden_4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hidden_4)


def main():

    names = dir(hidden_4)
    non_names = sorted(name for name in names if not name.startswith("__"))

    for name in non_names:
        print(name)


if __name__ == "__main__":
    main()
