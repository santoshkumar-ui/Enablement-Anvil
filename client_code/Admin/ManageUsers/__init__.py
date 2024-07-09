from ._anvil_designer import ManageUsersTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ManageUsers(ManageUsersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Admin.ManageUsers.ManageAdmin')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Admin.ManageUsers.ManageEmployee')
