import ConfigParser, os, pickle

class Config():
  
  configfile = "/etc/cloudresize/cloudresize.conf"
  
  def __init__( self ):
    self.config = ConfigParser.ConfigParser()
    self.config.readfp( open(self.configfile) )
    # verify we have needed params
    self.config.get("AWS", "AWSID")
    self.config.get("AWS", "SECRETKEY")
    self.config.get("AWS", "QUEUE")
    self.config.get("AWS", "BUCKET")
    
  def get ( self, section, key ):
    return self.config.get(section, key)

  def save (self ):
    with open(self.configfile, 'wb') as configdetail:
      self.config.write(configdetail)