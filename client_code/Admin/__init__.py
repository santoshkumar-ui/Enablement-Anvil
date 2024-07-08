from ._anvil_designer import AdminTemplate
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables


class Admin(AdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @anvil.server
  def store_user_input(user_name, email, password):
    app_tables.app_tables_adminapp_tables.app_tables_admin.add_row(Email=email, Name=user_name, Password=password)