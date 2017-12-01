###
#
#  Did US Mainstream Media sources talk about Trump or Clinton more in September 2016?"
#    David Anderton MAS.500
#
###

import mediacloud

# importing api keys
# https://stackoverflow.com/a/34165457/3700836
# https://docs.python.org/3/library/configparser.html
import ConfigParser


configParser = ConfigParser.RawConfigParser()   
configFilePath = r'config.ini'
configParser.read(configFilePath)

# debug
#print 'Currently having auth issues with API key :('
#print configParser.get('HW1', 'MediaCloudAPIKey')

mc = mediacloud.api.MediaCloud(configParser.get('HW1', 'MediaCloudAPIKey'))
trumpResults = mc.sentenceCount('( TRUMP )', '+publish_date:[2016-09-01T00:00:00Z TO 2016-10-011T00:00:00Z} AND +tags_id_media:1')
clintonResults = mc.sentenceCount('( CLINTON )', '+publish_date:[2016-09-01T00:00:00Z TO 2016-10-011T00:00:00Z} AND +tags_id_media:1')

if trumpResults['count'] > clintonResults['count']:
    print 'Trump was talked about more in US Mainstream media in September 2016 than Clinton'
else:
    print 'Clinton was talked about more in US Mainstream media in September 2016 than Trump'
