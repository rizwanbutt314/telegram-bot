from .main import executor

def query_handler_filter(call): return call.data == "activate"

def query_handler(call, bot):
    executor(call.message, bot)