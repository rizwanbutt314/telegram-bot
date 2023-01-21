import os
from importlib import import_module


def get_commands_function_mapping():
    path = os.path.dirname(os.path.abspath(__file__))
    commands_folder_path = os.path.join(path, "commands")

    commands_fn_mapping = {}

    for command_folder in os.listdir(commands_folder_path):
        import_statement = f"commands.{command_folder}.main"
        mod = import_module(import_statement)
        commands_fn_mapping[command_folder] = getattr(mod, "executor")

    return commands_fn_mapping


def get_query_handlers_function_mapping():
    path = os.path.dirname(os.path.abspath(__file__))
    commands_folder_path = os.path.join(path, "commands")

    handlers_fn_mapping = {}

    for command_folder in os.listdir(commands_folder_path):
        import_statement = f"commands.{command_folder}.handlers"
        try:
            mod = import_module(import_statement)
            handlers_fn_mapping[command_folder] = {"query_handler": getattr(
                mod, "query_handler"), "query_handler_filter": getattr(mod, "query_handler_filter")}
        except ModuleNotFoundError:
            pass

    return handlers_fn_mapping
