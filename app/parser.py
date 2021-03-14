
class XBRLParser():
    """
    Parser for XBRL files
    """
    xbrl_file_path = None

    def __init__(self, xbrl_file_path):
        """
        xbrl_file_path: input location of xbrl file.
        example: /Users/m_ishikawa/Downloads/toyota2020.xbrl
        """
        self.xbrl_file_path = xbrl_file_path
    
