# ================ IMPORT ================ #
from datetime import datetime

# ================ CLASS ================= #
class Logger:
  """
  Just a custom logger because why not :shrug:
  """
  def __init__(self, debug: bool = False) -> None:
    """
    Constructor

    Args:
        debug (bool, optional): Print debug message or not. Defaults to False.
    """
    self.debug_mode = debug
  
  def __date__(self) -> None:
    """
    Get the date in a readable format
    """
    return datetime.today().strftime('%d/%m/%Y %H:%M:%S')
  
  def debug(self, text: any, title: str = "DEBUG") -> None:
    """
    Log something with the debug level

    Args:
        text (any)
        title (str, optional) Defaults to "DEBUG"
    """
    if self.debug_mode:
      print(f"\033[94m[{self.__date__()}] {title.upper()}: {str(text)}\033[0m")
  
  def comment(self, text: any, title: str = "COMMENT") -> None:
    """
    Log something with the comment level

    Args:
        text (any)
        title (str, optional) Defaults to "COMMENT"
    """
    print(f"\033[93m[{self.__date__()}] {title.upper()}: {str(text)}\033[0m")

  def info(self, text: any, title: str = "INFO") -> None:
    """
    Log something with the info level

    Args:
        text (any)
        title (str, optional) Defaults to "INFO"
    """
    print(f"\033[96m[{self.__date__()}] {title.upper()}: {str(text)}\033[0m")

  def error(self, text: any, title: str = "ERROR") -> None:
    """
    Log something with the error level

    Args:
        text (any)
        title (str, optional) Defaults to "ERROR"
    """
    print(f"\033[91m{self.__date__()}] {title.upper()}: {str(text)}\033[0m")

# ================ TESTS ================= #
if __name__ == "__main__":
  testLogDebug = Logger(True)
  testLogDebug.comment("This is a comment")
  testLogDebug.debug("This is a debug")
  testLogDebug.error("This is an error")
  testLogDebug.info("This is an info")
  
  testLognNoDebug = Logger()
  testLognNoDebug.comment("This is a comment")
  testLognNoDebug.debug("This is a debug")
  testLognNoDebug.error("This is an error")
  testLognNoDebug.info("This is an info")