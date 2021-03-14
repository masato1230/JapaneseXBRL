
class Row():
    """
    Object for store tag, contextRef, value.
    """
    tag = None
    contextRef = None
    value = None
    
    def __init__(self, tag, contextRef, value=None):
        self.tag = tag
        self.contextRef = contextRef
        self.value = value
