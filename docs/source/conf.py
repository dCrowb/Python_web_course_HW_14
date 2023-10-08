import sys
import os

sys.path.append(os.path.abspath("..."))
project = "Python_web_course_HW_14"
copyright = "2023, dcrowb"
author = "dcrovb"


extensions = ["sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


html_theme = "nature"
html_static_path = ["_static"]
