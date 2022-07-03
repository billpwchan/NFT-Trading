import platform

from magic_eden import magiceden, monkelabs
from util.global_vars import *

isWindows = True if platform.system() == 'Windows' else False

mint_config = [config['MAGICEDEN.API'][item] for item in config['MAGICEDEN.API']]
print(mint_config)

# if mint on magiceden.io
if "magiceden.io" in mint_config[0]:
    print("Found magiceden.io link")
    magiceden.MagicEden(mint_config, isWindows)

# if mint on monkeylabs.io
elif "monkelabs.io" in mint_config[0]:
    print("Found monkelabs.io link")
    monkelabs.mint(mint_config, isWindows)

# if platform not supported
else:
    print("Could not recognize link")
