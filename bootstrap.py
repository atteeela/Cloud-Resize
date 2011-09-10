
from config import Config

class Bootstrap:

  def bootstrap ( ) :
    try:
      configuration = Config()
    except IOError:
      print "Unable to load configuration from", Config.configfile,", create one from cloudresize.conf.example"
    except Exception as error:
      print "Unknown error when reading configuration file"
      print error
    else:
      return configuration
    
  bootstrap = staticmethod(bootstrap)