from ._anvil_designer import addemployeeTemplate
from anvil import *


class addemployee(addemployeeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
