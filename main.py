from nicegui import ui ,app
import os
from pages.home import *
from pages.signin import *
from pages.signup import *
from pages.event import *
from pages.college import *
from pages.create_event import *
from pages.not_found import *




app.add_static_files("/assets",os.path.join(os.getcwd(),"assets"))
  
ui.run()
