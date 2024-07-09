from ._anvil_designer import editemployeeTemplate
from anvil import *


class editemployee(editemployeeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.users.search(user_type='employee')


    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('Your Details Has Been Saved')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Admin.ManageUsers.ManageEmployee.editemployee')
