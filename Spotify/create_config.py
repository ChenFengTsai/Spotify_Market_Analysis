import configparser

config = configparser.ConfigParser()
# Add the structure to the file we will create
config.add_section('KEYS')
config.set('KEYS', 'cid', '21fdb3d7196f40498694850370c60ade')
config.set('KEYS', 'secret', 'ca86ad661abf4530a9c83f48b6d12124')


# Write the new structure to the new file
if __name__ == "__main__":
    with open("./configfile.cfg", 'w') as configfile:
        config.write(configfile)