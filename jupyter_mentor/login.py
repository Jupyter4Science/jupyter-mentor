# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_login.ipynb.

# %% auto 0
__all__ = ['Login']

# %% ../nbs/01_login.ipynb 2
import ipywidgets as widgets
from ipywidgets import VBox, HTML, HBox, Label, Tab, Output, Button, Text
from IPython.display import display, clear_output
import ipyvuetify as v


# %% ../nbs/01_login.ipynb 3
class Login(VBox):
    
    def __init__(self):
        super().__init__()
        
        # Username input
        self.username_label = Label('Username:')
        self.username_input = Text(placeholder='Enter username')
        
        # Password input
        self.key_label = Label('API Key:')
        self.key_input = Text(placeholder='Enter API key', password=True)
        
        # Login button
        self.login_button = Button(description='Login')
        
        # Arrange labels and inputs horizontally
        self.username_box = HBox([self.username_label, self.username_input])
        self.key_box = HBox([self.key_label, self.key_input])
        
        # Arrange widgets vertically
        self.children = [
            HTML('<h2>Login</h2>'),  # Heading
            self.username_box,       # Username label and input box
            self.key_box,       # Password label and input box
            HBox([self.login_button], layout={'justify_content': 'flex-end'}),  # Login button aligned to the right
        ]

