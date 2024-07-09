from ._anvil_designer import ItemTemplate1Template
from anvil import *


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.users.serach(user_type='employee')

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('Your Details Has Been saved')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.item.delete()
    self.remove_from_parent()
