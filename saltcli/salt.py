import sys
from lib.config import Config
from commands import get_method

def run(args, obj):
  """Kick off"""
  conf = _load_config(obj['config'])
  provider = obj['provider']
  # meth = getattr(commands, obj['command'])
  meth = get_method(obj['command'])
  meth(provider, args, conf, obj)
  # launch()

def _load_config(conf_file):
  return Config(conf_file)
  
def known_providers():
  """All know providers"""
  return ['aws']

def known_commands():
  """All known commands"""
  return ('launch', 'list', 'teardown', 'ssh', 'upload', 'bootstrap', 'highstate')