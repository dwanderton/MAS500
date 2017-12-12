###
#
#  Did US Mainstream Media sources talk about Trump or Clinton more in September 2016?"
#    David Anderton MAS.500
#
###

import mediacloud
from pprint import pprint

# importing api keys
# https://stackoverflow.com/a/34165457/3700836
# https://docs.python.org/3/library/configparser.html
import ConfigParser
configParser = ConfigParser.RawConfigParser()
configFilePath = r'config.ini'
configParser.read(configFilePath)

# logger from https://docs.python.org/2.3/lib/node304.html
import logging
logger = logging.getLogger('mediacloudAPIcaller')
hdlr = logging.FileHandler('./logs.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


mc = mediacloud.api.MediaCloud(configParser.get('HW1', 'MediaCloudAPIKey'))

class MediaCloud:

    def __init__(self):
        self.connectToAPI()

    def connectToAPI(self):
        self.mc = mediacloud.api.MediaCloud(configParser.get('HW1', 'MediaCloudAPIKey'))
        logger.info("Connection to MediaCloud made."
        #pprint(type(self.mc))

    def trumpvclinton(self):
        trumpResults = self.mc.sentenceCount('( TRUMP )', '+publish_date:[2016-09-01T00:00:00Z TO 2016-10-011T00:00:00Z} AND +tags_id_media:1')
        clintonResults = self.mc.sentenceCount('( CLINTON )', '+publish_date:[2016-09-01T00:00:00Z TO 2016-10-011T00:00:00Z} AND +tags_id_media:1')
        logger.info("Comparing TRUMP vs CLINTON in SEPTEMBER 2016")
        if trumpResults['count'] > clintonResults['count']:
            print 'Trump was talked about more in US Mainstream media in September 2016 than Clinton'
        else:
            print 'Clinton was talked about more in US Mainstream media in September 2016 than Trump'

    def load(self):
        self.file = open(self.filename, 'r')
        self.all_lines = self.file.readlines()

    def states(self):
        all_names = []
        for line in self.all_lines:
            columns = line.split(',')
            all_names.append(columns[1])
        return all_names[1:]

#mediacloud = MediaCloud()
#mediacloud.trumpvclinton();
