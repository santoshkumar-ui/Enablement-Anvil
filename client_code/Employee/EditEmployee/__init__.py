from ._anvil_designer import EditEmployeeTemplate
from anvil import *


class EditEmployee(EditEmployeeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
