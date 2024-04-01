# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_chatbot.ipynb.

# %% auto 0
__all__ = ['ChatBot', 'StudentChatBot', 'EducatorChatBot']

# %% ../nbs/05_chatbot.ipynb 1
import ipywidgets as widgets
from ipywidgets import Textarea, Text, Layout, HBox

# %% ../nbs/05_chatbot.ipynb 2
class ChatBot(widgets.VBox):
    
    def __init__(self):
        # If you forget to call the superconstructor on an extended widget
        # you will get an AttributeError: object has no attribute '_model_id'
        super().__init__()

        example_convo = '''
User: Hello, bot!

Bot: Hi there! How can I assist you today?

User: I need help setting up my email account. Can you guide me through the process?

Bot: Of course! Could you please provide me with the email service provider you're using?

User: I use Gmail.

Bot: Great! First, go to the Gmail website and click on the "Create account" button.

User: Okay, I'm there. What's next?

Bot: Enter your personal information such as your name, desired email address, password, and recovery information.

User: Done! What's next?

Bot: Follow the prompts to verify your phone number and agree to the terms of service.

User: All set! Thank you for your help, bot!

Bot: You're welcome! If you have any more questions, feel free to ask.
'''
        self.chat = Textarea(
            disabled = True,
            value = example_convo,
            layout=Layout(width='90%', height='400px')
        )
        self.user_input_and_submit = HBox()
        self.user_input = widgets.Text(
            placeholder='Message AI chatbot...',
            #layout=Layout(width='100%')
        )
        self.submit = widgets.ToggleButton(
            value=False,
            disabled=False,
            button_style='success',
            icon='arrow-circle-right' 
        )
        self.user_input_and_submit.children = (self.user_input, self.submit)

        self.children = (self.chat, self.user_input_and_submit) 

# %% ../nbs/05_chatbot.ipynb 4
class StudentChatBot(widgets.VBox):
    
    def __init__(self):
        # If you forget to call the superconstructor on an extended widget
        # you will get an AttributeError: object has no attribute '_model_id'
        super().__init__()

        self.chat_bot = ChatBot()

        self.suggestion_buttons = HBox()
        self.step_by_step = widgets.Button(
            description='Step-by-Step',
            button_style='info',
            tooltip='Description',
        )
        self.metaphor = widgets.Button(
            description='Metaphor',
            button_style='info',
            tooltip='Description',
        )
        self.hints = widgets.Button(
            description='Hints',
            button_style='info',
            tooltip='Description',
        )
        self.guided_questions = widgets.Button(
            description='AI Guided Questions',
            button_style='info',
            tooltip='Description', 
        )
        self.suggestion_buttons.children = (self.step_by_step, self.metaphor, self.hints, self.guided_questions)
        self.children = (self.chat_bot, self.suggestion_buttons)

# %% ../nbs/05_chatbot.ipynb 6
class EducatorChatBot(widgets.VBox):
    
    def __init__(self, ):
        # If you forget to call the superconstructor on an extended widget
        # you will get an AttributeError: object has no attribute '_model_id'
        super().__init__()

        self.chat_bot = ChatBot()

        self.suggestion_buttons = HBox()
        self.exam_questions = widgets.Button(
            description='Exam Questions',
            button_style='info',
            tooltip='Description',
        )
        self.lesson_plan = widgets.Button(
            description='Lesson Plan',
            button_style='info',
            tooltip='Description',
        )
        self.suggestion_buttons.children = (self.exam_questions, self.lesson_plan )
        self.children = (self.chat_bot, self.suggestion_buttons)
