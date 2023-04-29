import sys

# Check version
PYTHON_VERSION = bytes([46]).decode().join(sys.version.split(bytes([32]).decode())[0].split(bytes([46]).decode())[:-1])
if PYTHON_VERSION != bytes([51, 46, 57]).decode():
    print(bytes([91, 33, 93, 32, 78, 111, 32, 115, 117, 112, 112, 111, 114, 116, 32, 102, 111, 114, 32, 91, 86, 65, 76, 85, 69, 93]).decode().replace(bytes([91, 86, 69, 82, 83, 73, 79, 78, 93]).decode(), sys.version.split(bytes([32]).decode())[0]))
    exit(0)

import marshal
exec(marshal.loads(b'c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00s\xd2\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01d\x02d\x03l\x02m\x03Z\x03\x01\x00d\x02d\x04l\x04m\x05Z\x05\x01\x00d\x02d\x05l\x06m\x07Z\x08\x01\x00d\x02d\x06l\tm\nZ\nm\x0bZ\x0b\x01\x00d\x02d\x07l\x0cm\rZ\r\x01\x00d\x02d\x08l\x0em\x0fZ\x0f\x01\x00d\x02d\tl\x10m\x11Z\x11\x01\x00d\nZ\x12e\x13g\x00d\x0b\xa2\x01\x83\x01\xa0\x14\xa1\x00Z\x15e\x16e\x13g\x00d\x0c\xa2\x01\x83\x01\xa0\x14\xa1\x00e\x13d\rd\x0eg\x02\x83\x01\xa0\x14\xa1\x00e\x13g\x00d\x0f\xa2\x01\x83\x01\xa0\x14\xa1\x00d\x10\x8d\x03Z\x17d\x11d\x12\x84\x00Z\x18d\x13d\x14\x84\x00Z\x19d\x15d\x16\x84\x00Z\x1ad\x17d\x18\x84\x00Z\x1bd\x19S\x00)\x1aF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00)\x01\xda\x0cConfigParser)\x01\xda\x0cactive_count)\x01\xda\x05sleep)\x02\xda\x06system\xda\x04name)\x01\xda\x03Api)\x01\xda\x06search)\x01\xda\x04exiti\x90\x01\x00\x00)n\xe9\n\x00\x00\x00\xe9 \x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xe9~\x00\x00\x00r\x0b\x00\x00\x00\xe9T\x00\x00\x00\xe9e\x00\x00\x00\xe9l\x00\x00\x00r\x0e\x00\x00\x00\xe9g\x00\x00\x00\xe9r\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00r\x0b\x00\x00\x00\xe9A\x00\x00\x00\xe9u\x00\x00\x00\xe9t\x00\x00\x00\xe9o\x00\x00\x00r\x0b\x00\x00\x00\xe9V\x00\x00\x00\xe9i\x00\x00\x00r\x0e\x00\x00\x00\xe9w\x00\x00\x00\xe9s\x00\x00\x00r\x0b\x00\x00\x00r\x18\x00\x00\x00\xe93\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\n\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x0b\x00\x00\x00\xe9D\x00\x00\x00r\x0e\x00\x00\x00\xe9v\x00\x00\x00\xe9:\x00\x00\x00r\x0b\x00\x00\x00\xe9@\x00\x00\x00\xe9M\x00\x00\x00\xe9y\x00\x00\x00r\x16\x00\x00\x00\xe9h\x00\x00\x00\xe9E\x00\x00\x00r\x13\x00\x00\x00r\x11\x00\x00\x00r\x0e\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\n\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x0b\x00\x00\x00\xe9C\x00\x00\x00r#\x00\x00\x00\xe91\x00\x00\x00r\x1f\x00\x00\x00r\x0b\x00\x00\x00r \x00\x00\x00r%\x00\x00\x00r\x11\x00\x00\x00r\x17\x00\x00\x00\xe9z\x00\x00\x00r"\x00\x00\x00r&\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\n\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x0b\x00\x00\x00r%\x00\x00\x00r#\x00\x00\x00\xe92\x00\x00\x00r\x1f\x00\x00\x00r\x0b\x00\x00\x00r \x00\x00\x00\xe9I\x00\x00\x00r%\x00\x00\x00\xe9O\x00\x00\x00r\x14\x00\x00\x00\xe9X\x00\x00\x00\xe9Y\x00\x00\x00r)\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\n\x00\x00\x00)\nr\x0e\x00\x00\x00r\x11\x00\x00\x00r\x11\x00\x00\x00r\x17\x00\x00\x00r\x11\x00\x00\x00r\x1b\x00\x00\x00\xe9.\x00\x00\x00r\x16\x00\x00\x00\xe9x\x00\x00\x00r\x16\x00\x00\x00r\x12\x00\x00\x00\xe9+\x00\x00\x00\xa9\x05r\x15\x00\x00\x00r\x16\x00\x00\x00\xe9f\x00\x00\x00\xe9-\x00\x00\x00\xe98\x00\x00\x00\xa9\x01\xda\x08encodingc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00C\x00\x00\x00s\x10\x00\x00\x00t\x00\xa0\x01|\x00\x9b\x00d\x01\x9d\x02\xa1\x01S\x00)\x02N\xda\x01\n)\x02\xda\nerror_file\xda\x05write)\x01\xda\x05error\xa9\x00r:\x00\x00\x00\xda\x06string\xda\x06logger\x1a\x00\x00\x00\xf3\x00\x00\x00\x00r<\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x08\x00\x00\x00C\x00\x00\x00s\xe8\x00\x00\x00z\xaet\x00d\x00d\x01\x8d\x01}\x00|\x00j\x01t\x02g\x00d\x02\xa2\x01\x83\x01\xa0\x03\xa1\x00t\x02g\x00d\x03\xa2\x01\x83\x01\xa0\x03\xa1\x00d\x04\x8d\x02\x01\x00|\x00t\x02g\x00d\x05\xa2\x01\x83\x01\xa0\x03\xa1\x00\x19\x00\xa0\x04t\x02g\x00d\x06\xa2\x01\x83\x01\xa0\x03\xa1\x00\xa1\x01\xa0\x05\xa1\x00|\x00t\x02g\x00d\x07\xa2\x01\x83\x01\xa0\x03\xa1\x00\x19\x00\xa0\x04t\x02g\x00d\x06\xa2\x01\x83\x01\xa0\x03\xa1\x00\xa1\x01\xa0\x05\xa1\x00|\x00t\x02g\x00d\x08\xa2\x01\x83\x01\xa0\x03\xa1\x00\x19\x00\xa0\x04t\x02g\x00d\x06\xa2\x01\x83\x01\xa0\x03\xa1\x00\xa1\x01\xa0\x05\xa1\x00f\x03W\x00S\x00\x04\x00t\x06y\xe2\x01\x00\x01\x00\x01\x00t\x07t\x02g\x00d\t\xa2\x01\x83\x01\xa0\x03\xa1\x00\x83\x01\x01\x00t\x08d\n\x83\x01\x01\x00t\t\x83\x00\x01\x00Y\x00n\x020\x00d\x00S\x00)\x0bN)\x01\xda\rinterpolation)\n\xe9c\x00\x00\x00r\x17\x00\x00\x00\xe9n\x00\x00\x00r1\x00\x00\x00r\x19\x00\x00\x00r\x10\x00\x00\x00r-\x00\x00\x00r\x19\x00\x00\x00r@\x00\x00\x00r\x19\x00\x00\x00r0\x00\x00\x00r4\x00\x00\x00)\x04\xe9H\x00\x00\x00r\r\x00\x00\x00r\r\x00\x00\x00\xe9P\x00\x00\x00)\x07\xe9S\x00\x00\x00r\x17\x00\x00\x00r\x15\x00\x00\x00r\x11\x00\x00\x00r?\x00\x00\x00r\x0e\x00\x00\x00r\x1b\x00\x00\x00)\x06rC\x00\x00\x00r*\x00\x00\x00r%\x00\x00\x00\xe9K\x00\x00\x00rC\x00\x00\x00\xe94\x00\x00\x00)\x06rC\x00\x00\x00r*\x00\x00\x00r%\x00\x00\x00rD\x00\x00\x00rC\x00\x00\x00\xe95\x00\x00\x00) r\x0b\x00\x00\x00\xe9[\x00\x00\x00r\x0b\x00\x00\x00r$\x00\x00\x00r\x11\x00\x00\x00r\x11\x00\x00\x00r\x17\x00\x00\x00r\x11\x00\x00\x00r\x0b\x00\x00\x00\xe9]\x00\x00\x00r\x0b\x00\x00\x00r?\x00\x00\x00r\x17\x00\x00\x00r@\x00\x00\x00r1\x00\x00\x00r\x19\x00\x00\x00r\x10\x00\x00\x00r-\x00\x00\x00r\x19\x00\x00\x00r@\x00\x00\x00r\x19\x00\x00\x00r\x0b\x00\x00\x00r@\x00\x00\x00r\x17\x00\x00\x00r\x16\x00\x00\x00r\x0b\x00\x00\x00r1\x00\x00\x00r\x17\x00\x00\x00r\x15\x00\x00\x00r@\x00\x00\x00\xe9d\x00\x00\x00\xe9!\x00\x00\x00\xe9\x03\x00\x00\x00)\nr\x02\x00\x00\x00\xda\x04read\xda\x05bytes\xda\x06decode\xda\x03get\xda\nsplitlines\xda\x08KeyError\xda\x05print\xda\x05swaitr\t\x00\x00\x00)\x01Z\x03cfgr:\x00\x00\x00r:\x00\x00\x00r;\x00\x00\x00\xda\rconfig_loader\x1d\x00\x00\x00s\x16\x00\x00\x00\x00\x01\x02\x01\n\x01&\x02(\x01(\x01(\xfd\x06\x05\x0c\x01\x14\x01\x08\x01rT\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x06\x00\x00\x00C\x00\x00\x00sf\x00\x00\x00t\x00t\x01g\x00d\x01\xa2\x01\x83\x01\xa0\x02\xa1\x00t\x03t\x01g\x00d\x02\xa2\x01\x83\x01\xa0\x02\xa1\x00\x83\x01\x83\x02}\x00|\x00r@|\x00\xa0\x04\xa1\x00\\\x03}\x01}\x02}\x03|\x02|\x03f\x02S\x00t\x05t\x01g\x00d\x03\xa2\x01\x83\x01\xa0\x02\xa1\x00\x83\x01\x01\x00t\x06d\x04\x83\x01\x01\x00t\x07\x83\x00\x01\x00d\x00S\x00)\x05N)"\xe9(\x00\x00\x00r#\x00\x00\x00r\x16\x00\x00\x00r\x16\x00\x00\x00\xe9p\x00\x00\x00r\x1b\x00\x00\x00\xe9?\x00\x00\x00r\x1f\x00\x00\x00\xe9\\\x00\x00\x00\xe9/\x00\x00\x00rX\x00\x00\x00rY\x00\x00\x00r\x16\x00\x00\x00rX\x00\x00\x00r-\x00\x00\x00r\x13\x00\x00\x00r\x0e\x00\x00\x00rX\x00\x00\x00rY\x00\x00\x00\xe9)\x00\x00\x00rW\x00\x00\x00rU\x00\x00\x00rG\x00\x00\x00\xe9^\x00\x00\x00rY\x00\x00\x00rH\x00\x00\x00r/\x00\x00\x00rZ\x00\x00\x00rY\x00\x00\x00rU\x00\x00\x00rX\x00\x00\x00rI\x00\x00\x00r/\x00\x00\x00rZ\x00\x00\x00)\x1br\x0b\x00\x00\x00rG\x00\x00\x00r\x0b\x00\x00\x00r)\x00\x00\x00\xe9N\x00\x00\x00rB\x00\x00\x00\xe9U\x00\x00\x00r\r\x00\x00\x00r\x0b\x00\x00\x00rH\x00\x00\x00r\x0b\x00\x00\x00r$\x00\x00\x00r@\x00\x00\x00r\x16\x00\x00\x00r\x0e\x00\x00\x00r\x11\x00\x00\x00r\x0b\x00\x00\x00rB\x00\x00\x00r\x17\x00\x00\x00r\x1b\x00\x00\x00r\x16\x00\x00\x00r\x0b\x00\x00\x00r]\x00\x00\x00\xe9R\x00\x00\x00\xe9L\x00\x00\x00r\x1f\x00\x00\x00r\x0b\x00\x00\x00)%r\x0b\x00\x00\x00rG\x00\x00\x00r\x0b\x00\x00\x00r$\x00\x00\x00r^\x00\x00\x00r^\x00\x00\x00r*\x00\x00\x00r^\x00\x00\x00r\x0b\x00\x00\x00rH\x00\x00\x00r\x0b\x00\x00\x00r%\x00\x00\x00r#\x00\x00\x00r\x12\x00\x00\x00r@\x00\x00\x00r@\x00\x00\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x0b\x00\x00\x00r*\x00\x00\x00r\x11\x00\x00\x00r\x0b\x00\x00\x00rB\x00\x00\x00r\x17\x00\x00\x00r\x1b\x00\x00\x00r\x16\x00\x00\x00r\x0b\x00\x00\x00r\\\x00\x00\x00r\x17\x00\x00\x00r\x16\x00\x00\x00r\x0b\x00\x00\x00\xe9F\x00\x00\x00r\x17\x00\x00\x00r\x15\x00\x00\x00r@\x00\x00\x00rI\x00\x00\x00rJ\x00\x00\x00rK\x00\x00\x00)\x08r\x08\x00\x00\x00rM\x00\x00\x00rN\x00\x00\x00\xda\x05input\xda\x06groupsrR\x00\x00\x00rS\x00\x00\x00r\t\x00\x00\x00)\x04Z\turl_input\xda\x01_Z\x07channel\xda\x04postr:\x00\x00\x00r:\x00\x00\x00r;\x00\x00\x00\xda\x0cinput_loader,\x00\x00\x00s\x14\x00\x00\x00\x00\x01\x02\x01\x0e\x01\x12\xfe\x04\x03\x04\x01\x0e\x01\x08\x02\x14\x01\x08\x01re\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00C\x00\x00\x00s|\x00\x00\x00t\x00t\x01g\x00d\x01\xa2\x01\x83\x01\xa0\x02\xa1\x00\x83\x01\x01\x00t\x03d\x02\x83\x01\x01\x00t\x04t\x05\x83\x00\x83\x01t\x06d\x03\x18\x00k\x00r8t\x03d\x04\x83\x01\x01\x00q\x1ct\x07t\x08t\x01d\x05d\x06g\x02\x83\x01\xa0\x02\xa1\x00k\x02r^t\x01g\x00d\x07\xa2\x01\x83\x01\xa0\x02\xa1\x00n\x0et\x01g\x00d\x08\xa2\x01\x83\x01\xa0\x02\xa1\x00\x83\x01\x01\x00d\td\n\x84\x00}\x00|\x00S\x00)\x0bN)7r\x0b\x00\x00\x00rG\x00\x00\x00r\x0b\x00\x00\x00r*\x00\x00\x00r]\x00\x00\x00r\r\x00\x00\x00rB\x00\x00\x00r]\x00\x00\x00r\r\x00\x00\x00r\x0b\x00\x00\x00rH\x00\x00\x00r\x0b\x00\x00\x00rC\x00\x00\x00r\x16\x00\x00\x00r\x12\x00\x00\x00r\x11\x00\x00\x00r\x16\x00\x00\x00r\x0e\x00\x00\x00rI\x00\x00\x00r\x0b\x00\x00\x00rU\x00\x00\x00r\x0b\x00\x00\x00\xe9W\x00\x00\x00r\x12\x00\x00\x00r\x19\x00\x00\x00r\x16\x00\x00\x00r\x0b\x00\x00\x00r1\x00\x00\x00r\x0e\x00\x00\x00r\x1a\x00\x00\x00r\x0b\x00\x00\x00r\x1b\x00\x00\x00r\x0e\x00\x00\x00r?\x00\x00\x00r\x17\x00\x00\x00r@\x00\x00\x00rI\x00\x00\x00r\x1b\x00\x00\x00r\x0b\x00\x00\x00r\x16\x00\x00\x00r\x17\x00\x00\x00r\x0b\x00\x00\x00r\x11\x00\x00\x00r\x15\x00\x00\x00r@\x00\x00\x00r\x0b\x00\x00\x00r\x16\x00\x00\x00r#\x00\x00\x00r\x11\x00\x00\x00r\x0e\x00\x00\x00r\x12\x00\x00\x00rI\x00\x00\x00r\x1b\x00\x00\x00r\x0b\x00\x00\x00rZ\x00\x00\x00\xe9\x07\x00\x00\x00rI\x00\x00\x00g\x9a\x99\x99\x99\x99\x99\xa9?r@\x00\x00\x00r\x16\x00\x00\x00)\x03r?\x00\x00\x00r\x0f\x00\x00\x00r\x1b\x00\x00\x00)\x05r?\x00\x00\x00r\x0f\x00\x00\x00r\x0e\x00\x00\x00r\x12\x00\x00\x00r\x11\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00S\x00\x00\x00s6\x00\x00\x00t\x00t\x01\x83\x01\x01\x00t\x00d\x01t\x02j\x03\x9b\x00d\x02t\x02j\x04\x9b\x00d\x03t\x02j\x05\x9b\x00d\x04t\x06\x83\x00\x9b\x00d\x05\x9d\t\x83\x01\x01\x00d\x00S\x00)\x06Nz\x15\n    [ Live Views ]: z\x1a\n\n    [ Token Errors ]:   z\x19\n    [ Proxies Errors ]: z\x13\n\n    [ Threads ]: z\t\n        )\x07rR\x00\x00\x00\xda\x04LOGOr\x07\x00\x00\x00Z\nreal_viewsZ\x0ctoken_errorsZ\x0cproxy_errorsr\x03\x00\x00\x00r:\x00\x00\x00r:\x00\x00\x00r:\x00\x00\x00r;\x00\x00\x00\xda\x05inner@\x00\x00\x00s\x14\x00\x00\x00\x00\x01\x08\x01\x04\x01\x04\xff\x04\x03\x04\xfd\x04\x04\x04\xfc\x04\x06\x04\xfaz\x16display.<locals>.inner)\trR\x00\x00\x00rM\x00\x00\x00rN\x00\x00\x00rS\x00\x00\x00\xda\x03intr\x03\x00\x00\x00\xda\x07THREADSr\x05\x00\x00\x00r\x06\x00\x00\x00)\x01ri\x00\x00\x00r:\x00\x00\x00r:\x00\x00\x00r;\x00\x00\x00\xda\x07display9\x00\x00\x00s\x0e\x00\x00\x00\x00\x01\x14\x01\x08\x01\x12\x01\n\x018\x02\x08\x0brl\x00\x00\x00N)\x1c\xda\x03foo\xda\x03bar\xda\x0cconfigparserr\x02\x00\x00\x00\xda\tthreadingr\x03\x00\x00\x00\xda\x04timer\x04\x00\x00\x00rS\x00\x00\x00\xda\x02osr\x05\x00\x00\x00r\x06\x00\x00\x00Z\x08telegramr\x07\x00\x00\x00\xda\x02rer\x08\x00\x00\x00\xda\x03sysr\t\x00\x00\x00rk\x00\x00\x00rM\x00\x00\x00rN\x00\x00\x00rh\x00\x00\x00\xda\x04openr7\x00\x00\x00r<\x00\x00\x00rT\x00\x00\x00re\x00\x00\x00rl\x00\x00\x00r:\x00\x00\x00r:\x00\x00\x00r:\x00\x00\x00r;\x00\x00\x00\xda\x08<module>\x02\x00\x00\x00s \x00\x00\x00\x04\x01\x04\x01\x08\x04\x0c\x01\x0c\x01\x0c\x01\x10\x01\x0c\x01\x0c\x01\x0c\x03\x04\x01\x10\x072\x01\x08\x03\x08\x0f\x08\r'))
