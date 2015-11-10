import re

logparser = r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2},\d{3})\s+' \
            r'(DEBUG|ERROR|INFO)\s+\[(\w+):(\w+):?(\w+)?\]\s+(.+)$'

regex = re.compile(logparser)
assert regex.findall(
    "2003-07-08 16:49:45,896 ERROR [user1:mainfunction:subfunction] "
    "We have a problem") == \
       [('2003-07-08 16:49:45,896', 'ERROR', 'user1', 'mainfunction',
         'subfunction', 'We have a problem')]
assert regex.findall(
    "2003-07-08 16:49:46,896 INFO [user1:mainfunction] "
    "We don't have a problem") == \
       [('2003-07-08 16:49:46,896', 'INFO', 'user1', 'mainfunction', '',
         "We don't have a problem")]
assert len(regex.findall(
    "2003-07-08 16:49:45,896 ERROR [user1:mainfunction:subfunction] "
    "We have a problem")[0]) == 6
