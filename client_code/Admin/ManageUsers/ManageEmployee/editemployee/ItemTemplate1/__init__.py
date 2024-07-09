from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.item.delete()
    self.remove_from_parent()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('Your Details Has Been Saved')

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
