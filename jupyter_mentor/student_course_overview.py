# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/14_student_course_overview.ipynb.

# %% auto 0
__all__ = ['FileDownloader', 'StudentCourseOverview']

# %% ../nbs/14_student_course_overview.ipynb 1
from .file_viewer import FileViewer
import ipywidgets as widgets
from ipywidgets import VBox, HBox, HTML, Button, Label, Text, Checkbox, Accordion, FileUpload
from ipyfilechooser import FileChooser
from IPython.display import display, clear_output
import ipyvuetify as v
from traitlets import observe

# %% ../nbs/14_student_course_overview.ipynb 2
class FileDownloader(widgets.VBox):
    def __init__(self):
        super().__init__()
        self.file_chooser = FileChooser()
        self.download_button = v.Btn(
            class_="ma-2",
            outlined=True,
            href="./course_files/hussey2015.pdf",
            attributes={"download": "hussey2015.pdf"},
            children=["Download All"]
        )
        self.children = [self.file_chooser, self.download_button]
		

# %% ../nbs/14_student_course_overview.ipynb 3
class StudentCourseOverview(VBox):
    def __init__(self):
        super().__init__()
        # global file viewer (that has model)
        #self.file_viewer = file_viewer
        # Course overview text
        self.course_overview_label = Label('Available Files:')
        # self.course_overview_text = Text(placeholder=‘Enter course overview’)

        self.file_downloader = FileDownloader()

    
        # Next button
        self.next_button = Button(description='Next')

        #Header
        self.header = v.Container(children=[
            v.Html(
                tag='h1',
                attributes={'title': 'a title'},
                children=['Student Course Overview']
            )
        ])

        
        # Arrange widgets vertically
        self.children = [
            self.header,  # Heading
            #self.file_viewer,
            self.course_overview_label,  # Course overview
            self.file_downloader,
            HBox([self.next_button], layout={'justify_content': 'flex-end'}),
        ]
