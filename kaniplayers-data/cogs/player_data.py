# ================ IMPORT ================ #
from requests import get
from json import loads

# ================= CLASS ================ #
class APIError(Exception):
  """
  Class for custom error message
  Extention of the Exception class
  """
  pass

class PlayerData:
  """
  Class to store datas for a player
  """
  def __init__(self, raw: dict):
    """
    Constructor

    Args:
      raw (dict): The raw datas for the player
    """
    # Get all the raw thing and wrap them into attributs
    self.name: str = raw["name"]
    self.playTime: int = raw["playTime"]
    self.deaths: int = raw["deaths"]
    self.netheriteMine: int = raw["netheriteMine"]
    self.jump: int = raw["jump"]
    self.totalKills: int = raw["totalKills"]
    self.damageTaken: int = raw["damageTaken"]
    self.chestOpened: int = raw["chestOpened"]
  
  def __str__(self) -> str:
    """
    String

    Returns:
        str
    """
    return (f"Player Data for : {self.name}")

# ============= API REQUEST ============== #

# Get things on the custom API in Node.js using express.js
REQ = get("http://fantomitechno.ovh:3000/api/kaniplayers")
JSON = loads(REQ.text)

# Cut the json datas in two with in one hand
# the code of error or no and in the other
# hand the result (with a message error or 
# an object)
CODE = JSON["code"]
RAW = JSON["result"]

# ============ ERROR HANDLING ============ #

if CODE == 1:
  """
  If an error is launched with the error "cannot read property items of undefined"
  at the first launch, just relaunch the program
  
  If it keep sending this error it can be because a server restart happen at 
  6AM UTC+1 (aka French TZ) so it's possible that the api is disconnected
  from the minecraft server if that happen contact Simon RENOUX
  """
  raise APIError(f"An error occurred on the API : {RAW}")

# =============== DATA TAB =============== #

DATAS = [PlayerData(r) for r in RAW]