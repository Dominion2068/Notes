import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
from streamlit_player import st_player
import json
import requests
from streamlit_lottie import st_lottie
import io
from datetime import date
from datetime import datetime
from platform import python_version
from streamlit_ace import st_ace

icon = Image.open('icon.png')
st.set_page_config(layout = 'wide', page_title="Rython",page_icon= icon)

col1, col2, col3, = st.columns([0.5, 1, 0.05])
col2.header("Hosted Lesson Notes: Example")
st.write('---')
imp = '''import pandas as pd
import numpy as np'''

def R():
    st.caption('**---R Code---**')
def P():
    st.caption('**---Python Code---**')
def Res():
    st.caption('''**---Result---**  
    ---The most important results are posted. Run the codes to see other results---''')
def Re():
    st.caption('**---Report---**')
def Simi():
    st.caption('**---Coding Patterns---**')
def fo():
    st.caption('**---Code Formats---**')
def Teach():
    st.caption("**---Teacher's Note---**")
def App():
    st.caption("**---Applications---**")

def T():
    st.write('---')
    st.write('')
    st.caption('**---Get used to the codes in this section, type them out---**')
    ojo = st.text_area('Use the comments to separate each lines of code, Dont forget to import the necessary libraries.')
    if ojo:
        st.caption('Check the results and run on Jupyter Notebook or R Studio')
        st.code(ojo)
    st.write('---')
col1, col2 = st.columns(2)
imp = '''import pandas as pd
import numpy as np'''

col1_expander = col1.expander("Beginners' Class 1: Introduction & Rython Environments")
with col1_expander:
    gra = st.radio(label = 'Rython', options = ['Hold', 'What is Rython?',
                                                        'Introduction to Rython Environment',
                                                        'Download/Install R and Python',
                                                        'Download/Install the IDEs',
                                                        'Install Libraries and Packages',
                                                        'How to use the Rython Apps'
                                                        ])
    #st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write('---')
    
    if gra == 'What is Rython?':
        st.write('**What is Rython?**')
        st.write('''  
        Arguably, R and Python are the two major langauges for data science. Other languages exist with specific
        focus on certain areas example is SQL for database programming however, Python and R are the most general 
        and the most used. Companies and organizations data language preferences differ, to this end, applicants always
        look for organization with peference for the language of their choice. 

Rython is an attempt to bridge the knowledge or learning gap between the two langauges. We believe it is
        possible to teach and learn both langauges simultenously and that students can become profficient 
        in both languages at the same time. 
        It sounds incredible, but it is possible. It is a matter of the teaching style and the willingness 
        of the student to do extra work. 

Rython is simply an attempt to learn R and Python programming 
        languages for data science together. It is the intuitive understanding and interpretation of R 
        with respect to Python and vice versa. It is using one langauge as a link bridge to the other. 
        It is developing the ability to decipher which programming language is best suited for particular 
        projects in data science.''')
    if gra == 'Introduction to Rython Environment':
        st.write('**Environments for R and Python**')

        st.write('''This is a short tutotrial on how to set up your environment. By environment we mean getting all
        softwares and packages to enable you commence and sustain a data science journey cum lifestyle. We shall be
        downloading and installing R, and Python programming languages then we shall download and install the IDEs -
        Rstudio for R and Jupyter Notebook for Python and we shall be looking at how to use them effectively. 
        Also, we shall conduct a short tutorial on how to use Google Colab which is Jupyter Notebook in the 
        cloud. We shall also look at setting up Github - a place where employers and the world at large can 
        check and evaluate your data science projects and progress, which is very important for every data 
        scientist. Mention shall also be made of Kaggle, - arguably the largest repository for datasets where 
        you search for, download and use datasets and also participate in data science competitions.''')


        st.write('''**Objectives:** 
        
- To download and install the R and Python Programming Languages  
- To create the necessary Integrated Development Environments IDEs where you run the codes.
- To learn how to install the necessary libraries for different data operations/tasks. 
''')

    if gra == 'Download/Install R and Python':
        st.write('''**Download R and Python using the Links Below:**
- [Click to download Python here:](https://www.python.org/downloads/)  
- [Click to download R for windows here:](https://cran.r-project.org/bin/windows/base/)  
- [Click to download R for macOS here:](https://cran.r-project.org/bin/macosx/)  
Install after downloading and ensure to install remember to add Python to PATH during installation. You can 
do a Google search of how to install Python or R if you run into any problems.   
''')
    
    if gra == 'Download/Install the IDEs':
        st.write('''**Download IDEs**  
Integrated Development Environments - IDEs provide you with a digital or coding interface(s) where you can 
run your codes, its like providing you with an oven to bake your cakes. We recommend Jupyter Notebook for 
Python and Rstudio for R.  
[Click to download the free version of RStudio Desktop here:](https://www.rstudio.com/products/rstudio/download/)
''')

        st.write('**RStudio**')
        st.write('''RStudio is the best Integrated Dvelopment Environment(IDE) for R. It is specifically made for R 
        and it has all the functionalities to make the R coding experience smooth and enjoyable. Below is the
        RStudio's interface.''')
        RS = Image.open('Rs.PNG')
        st.image(RS, use_column_width=True, caption = 'RStudio Interface')

        st.write('''**The Coding Interface (Upper Left)**  
        This is where you write your codes and run them. Above the interface are the usual interactive icons
        starting with the File icon and ending with the Help icon. They corresponding with the usual uses and 
        you will get used to then with time. For example when you click the File icon, you get a drop down, 
        you can create a new R script, open an old one, you can save as, or save and rename a file etc. Another
        importnat icon is the session icon it allows you to set your working directory where your R scripts and 
        dataset files are currently located, the default directory is Documents. To run your codes, click the
        run sub-icon to the right just immediately above the coding pane or press ctrl + enter keys. Always
        ensure that your cursor is on the line of code you want to run or you hightlight(ctrl+A) to run
        all the codes at once.      
        **The Console Interface**  
        Directly below the coding interface is the console interface. It has 3 icons: Console, Terminal and Jobs.
        The console shows the results of the codes after running them. It is the information output 
        point always giving you instructions and infomation about your code and about the packages.  
        **Upper Right Interface**  
        There are 2 columns here the first column contains the names of the datset you have read while each line of the 
        second column contains the number of rows and columns in the datasets. This environment provides
        major infomation about your datasets and you can view the dataset by clicking on the 
        small light blue arrow indication before the name of the dataset or by clicking on the second column. 
        Every dataset you read is shown on this pane. This interface also contain the History icon which 
        shows the history of all the code you have run overtime, all you need do is to scroll upo and 
        down to see. It also contains the Connections and Tutorial icons.  
        **The Final Interface - Lower Right**  
        This contains Files, Plots, Packages, Help and Viewer icons The Files icon allows for file and folder management,
        you can open, create a folder or file, rename, delete etc. All your graphical plots are shown under the Plots
        icon, all internal and downloaded R libraries and packages are contained in the Packages icon.''')
    
        st.write('**Jupyter Notebook**')
        st.write('''Type and search for CMD on your computer, after successfully installing Python. An image of the Command 
        Prompt is shown below.''')
        cmd = Image.open('CMD.PNG')
        st.image(cmd, use_column_width=True,caption='Command Prompt or Terminal')

        st.write('Install the Jupyter Notebook using the command prompt:')
        jn = '''pip install jupyter notebook
#or
pip install notebook
'''
        st.code(jn)

        st.markdown('''Jupyter Notebook is an open-source IDE - Integrated Development Environment that enables you to
        create, run and share your Python codes. It is an interface that allow you to see the transformation 
        of your data from one stage to the other in the data pipeline''')

        st.write('**Jupyter Notebook Brief Tutorials**')
                    
        kd = "cd documents\\analyst"
        jup = 'jupyter notebook'
                               
        st.write('''On the Command Prompt, change directory; type: cd  address of the folder you 
        intend to use for your project, then press the enter key. For Example:''')
        st.code(kd)
            
        st.write('''In the above code for example, I have series of project folders in a 
            folder called analyst in my documents folder. Therefore, I have **changed directory (cd)** to that location''')

        st.write('Finally type:')
        st.code(jup)
        st.write('When you press the enter key, the Jupyter Notebook interface is opened on your local default browser, what you get is something like this:')
        first = Image.open('jup1.PNG')
        st.image(first, use_column_width=True,caption='')
        st.write('''
    Navigate and click on the folder of interest. Click New on the far right and click
    on Python 3 (ipykernel)''')
        second = Image.open('jup2.PNG')
        st.image(second, use_column_width=True,caption='')
        st.write('''The interface is interactive, and you will definitely get used to it in due course. 
        However, you should take note of the following:
                        
1. Click on **Untitled** to change the name of the file
2. For you to write Python codes ensure the 12th mini icon from the left is on code
3. Click on Code and pick on markdown to write texts
4. Click Run to execute the codes written in the cells
5. Place your cursor on the icons to reveal short instructions
6. Click on each of the items on the toolbar to reveal a dropdown of actions
7. Your file is resident in the folder you navigated to initially **ctrl s** will continually save in that folder
8. The hashtag -  before texts convert them into comments in Python''')

        st.write(' ')
        st.write('**Google Colab**')
        st.write('''Another fantastic option to run your python code is the cloud option provided by Google called
    Google Colab. It is Jupyter Notebook that runs in the cloud, instead of running the Jupyter Notebook locally
    you can write and execute Python code online in your browser. The benefits over Jupyter Notebook include:  
- The 3rd party libraries are all pre-installed, you only need to import them   
- Your final works are easier to share
- Your files are directly linked to your Google Drive if you have one
- However, you need data to use Google Colab
To begin, do a Google search on Google Colab''')
        st.write('')
        st.markdown('''GitHub is the LinkedIn for data scientists/analysts and software developers. It is a must for you 
        as an analyst to have a GitHub account. Your GitHub account contains a history of your data science works and projects
        for the world to see. Also, you get ready-made solutions to a lot of the problems you will face
        as a data analyst. Nothing is new, others have done what you are doing. You can always check their solutions
        on GitHub. You will also find it useful if you intend to do some web 
        hosting especially Streamlit and Dash data visualization applications''')
        #st.markdown('------')
        st.markdown('------')

    if gra == 'Install Libraries and Packages':
        st.write('**Install 3rd Party Libraries and Packages**')
        st.write(''' Packages and 3rd party libraries are very important in R and Python. 
        RStudio comes with some base packages. There are many useful packages necessry for you towards becoming a data analyst. 
        To install a package you might need to download and install Rtools. 
        The R package installation code format is: 
        install.packages('package name').  
        Copy and paste these codes on the coding interface(Upper Left) in RStudio to install the 
        following R packages.''')

        c = '''# Install a single package
install.packages('package name')

# Install Multiple packages or libraries at once
# You will find the following packages and libraries very useful
install.packages(c('dplyr', 'Lahman', 'tidyverse', 'nycflights13',
'shiny', 'ggplot2', 'caret', 'plotly', 'readxl', 'data.table', 
'tidyr', 'knitr', 'mlr3', 'xgboost', 'caret','lubridate'))
'''
        st.code(c)
        st.write('''You can also install packages in R by clicking on install located in the 
        Lower Right Interface in RStudio.''')

        st.write('''To install libraries in Python, use the Command Prompt - CMD, you can always do a Google search
        to read more about the libraries you intend to install. Install the following libraries.''')
        st.markdown('''**The Pandas Library**  
        Pandas is a crucial Python library, it is very useful for data wrangling.
        Infact for data analysts/scientists, machine learning engineers, visualization engineers etc. 
        Panads is the go to library especially at the begining of the data pipeline. The pandas library 
        provides the necessry tools for thorough data exploration. It is built on Numpy (Numeric Python) - another python library.''')
        st.write('Install some libraries in Python using the command prompt:') 
        c = '''# type these codes one after the other on the CMD and press enter afterwards

# Install the Pandas Library, this also installs the Numpy Library
pip install pandas

# Install some visualization libraries
# install matplotlib
pip install matplotlib
# install seaborn, this also install matplotlib because it is built on it
pip install seaborn
'''
        st.code(c)

    if gra == 'How to use the Rython Apps':
        st.write('**How to use this app?**')
        st.write('''  
        This app is a tutorial guide to enhance your coding and data analysis efficency for both R and Python. 
        It helps you become a master of both data science languages together. That may sound unrealistic, but it is true.
        We believe the best way to learn multiple langauges together is to learn one through the eye of the other.
        This app can be used by students and employees in data science and related fields. Though the results of the codes are 
        displayed in the app but in real world you will use the identified IDEs for data science projects
        therefore, it is advised that the R codes are copied and run in RStudio while Python codes are copied and 
        run on Jupyter Notebook and or in Google Colab. Always ensure that all projects you are working on
        are committed into Github and locally in Google Drive or OneDrive. This app also serve as a revision
        helper to help you quickly remember codes,code analysis and the results as an employee or a student.''')



col1_expander = col2.expander("Sample Class': Rython Data Structures & Data Types")
with col1_expander:
        st.subheader('''Rython's Data Structure & Data Types''')
        
        
        st.write('---')
        struc = st.radio(label = 'Select a Topic', options = ['Hold',
                                                        'Introduction',
                                                        "R and Python's Data Types",
                                                        'Atomic vectors and list in R vs. list and tuple in Python',
                                                        ])

        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.write('---')

        if struc == 'Introduction':
                st.write('**Introduction**')

                st.write('''In this section we are going to take a deep dive into how R and Python see data.
        How are data organized, processed, stored and accessed in both languages? What fundamental differences
        exist between both languages with respect to data structures and types? The knowledge gained here
        will be crucial towards the appreciation of the prowess of both languages and the understanding of 
        their best applications and utilizations.  
        The data types are better identified and discussed within the data structures which serve as a
        containers for them.''')
                st.caption('Major types of Data Structures')
                c = pd.DataFrame({"R's Data Structures":['atomic vectors', 'list', 'matrix', 'data frame'],
                        'Python Data Structures':['list','tuple','dictionary','set']})
                c
                st.write('''The list data structure is common to both R and Python. The data Frame and matrix data structures
        present in R are also utilized in Python however, they are data structures for 3rd party libraries.
        The DataFrame is the major data structure for the Pandas library while matrix is similar to the 
        NumPy's (Numerical Python) main data structure called ndarray which means N-dimensional array 
        and Tensorflow's (Python Library for Deep Learning) tensors.''')
        # teach()
                st.write('''To make sense of the inner workings of both languages and how they are interrelated, we
        organize this section as follows:  
- R and Python's Data Types
- Atomic vectors and list in R vs. list and tuple in Python
- Matrix in R vs. NumPy's ndarray in Python
- Pandas DataFrame in Python vs. data frame in R
- Factors in R vs. Panads Categorical data type in Python
- Dictionary and Set in Python
- Summary of findings and 
- Comparative Analysis R and Python's Data Structure''')
        
        
        
        
        if struc == "R and Python's Data Types":
                st.write('**Data Types: R and Python**')
                st.write('''Data type is the basic unit of a dataset, just like the family is the basic unit of the
                larger society. A column with a million rows is basically defined by its data type. Without seeing
                a dataset, the column headers can give you an indication of the major data type in each column. For example,
                if you are asked to come up with a dataset with the following headers: Names, Date, Sales, Country, Discount, and Profit
                the ensuring data types suitable for the headers gives you an indication of the type of dataset in question.
                Simply put, when you know the data types you not only know the dataset, you also know your way around it.''')
        
                c = pd.DataFrame({'DataType':['character','numeric','integer','logical','complex'],
                                'Examples':["'London',   'a',    'b'",'49,   3.5 ,  0.01', '6L,   0L','FALSE,    TRUE', '4 + 5i,    7i']})
                st.caption('R Data Types')
                c

                c = pd.DataFrame({'DataType':['string','float','integer','boolean','complex'],
                                'Examples':["'London',   'a',    'b'",'9.91,   3.5 ,  0.01', '7,   654,    89','False,    True', '4j + 2j - j,    7j']})
                st.caption('Python Data Types')
                c

                st.caption('Identify the data types using codes')

                st.write('**Complex Data Type in R and in Python**')
                c = ''' # Complex Data Type in R
dtype = 6i
# or
dtype = 4 + 5i - 15L
# or
dtype = 0L + 27i + 45i
# or
dtype = 7L + 5L - 19i
# or
dtype = 7L + 56L * 1L / 21L - 19i

# Data Type identification codes
typeof(dtype)
# or
class(dtype)
# or
storage.mode(dtype)

# The next code is asking R to confirm the data type
# code_format:- is.R_data_type(data type name)
is.complex(dtype) # is dtype a complex data type? - TRUE or FALSE'''
                R()
                st.code(c)
                Res()
                st.text(''' "complex" ''')

                c = ''' # Complex Data Type in Python
dtype = 9j
# Or
dtype = 4j + 2.9j - 4j
# Or
dtype = 13 + 8j
# or
dtype = 11 + 8j * 17j / 0.1j - (200%3)

# Data Type identification codes
type(dtype)
# or
# The next code is asking Python to confirm the data type
# code_format:- isinstance(data_type_name, Python_data_type)
isinstance(dtype, complex) # is dtype a complex data type? True or False
'''
                P()
                st.code(c)
                Res()
                dtype = 11 + 8j * 17j / 0.1j - (200%3)
                st.text(type(dtype))
                st.caption('''The complex data types in R and Python are real numbers with variables denoted
                by i and j respectively. Python takes decimal numbers with the variables while R does not.
                They are complex because just like any equation the variables are currently unknown.
                Notice that Python accepts decimal numbers before the variable, R does not.''')


                st.write('**Integer Data Type in R and in Python**')
                c = ''' # Integer Data Type in R
dtype = 45L
# Or
dtype = 7L + 5L + 200L
# Or
dtype = 0L
# or
dtype = 2L + 49L * 3L + 21L - 19L

# Data Type identification codes
typeof(dtype)
# or
class(dtype)
# or
storage.mode(dtype)

# The next code is asking R to confirm the data type
is.integer(dtype) # is dtype an integer data type? - TRUE or FALSE'''
                R()
                st.code(c)
                Res()
                st.text(''' "integer" ''')

                c = ''' # Integer Data Type in Python
dtype = 3
# Or
dtype = 18976

# Data Type identification codes
type(dtype)
# or
# The next code is asking Python to confirm the data type
isinstance(dtype, int) # is dtype an integer data type? True or False
'''
                P()
                st.code(c)
                Res()
                dtype = 18976
                st.text(type(dtype))
                st.caption('''Notice the 'L' in the R integer data type, it tells R to store the data as
                an integer while the normal whole numbers are the integers in Python. This is an interesting
                difference between the two languages, we should provide some perspectives on this before
                the end of the section. Also notice that the complex data type is similar to the integer
                data type in R. The difference is probably how they are stored in R based on the attached variable
                L for integer and i for complex. However, when you combine the variable L and i togther as shown above, 
                the ensuring data type becomes the complex R data type.''')

                st.write('**Character Data Type in R and String Data Type in Python**')
                c = ''' # Character Data Type in R
dtype = 'A'
# or
dtype = 'Dominion'
# or
dtype = 'Love is beautiful'

# Data type identification codes
typeof(dtype)
# or
class(dtype)
# or
storage.mode(dtype)

# The next code is asking R to confirm the data type
is.charcater(dtype) # is dtype a character data type? - TRUE or FALSE'''
                R()
                st.code(c)
                Res()
                st.text(''' "character" ''')

                c = ''' # String Data Type in Python
dtype = 'A'
# or
dtype = 'Dominion'
# or
dtype = 'Love is beautiful'

# Data type identification codes
type(dtype)
# or
# The next code is asking Python to confirm the data type
isinstance(dtype, str) # is dtype a string data type? True or False
'''
                P()
                st.code(c)
                Res()
                dtype = 'Love is beautiful'
                st.text(type(dtype))
                st.caption('''The string data type in Python and the character data type in R are not 
                different in code construct. However, R terminology for the data type is more intuitive.
                It refers to characters, words, and statements.''')

                st.write('**Numeric Data Type in R and Float Data Type in Python**')
                c = ''' # Numeric or Double Data Type in R
dtype = 456
# or
dtype = 4.5
# or
dtype = 30 + 20
# or
dtype = 2L/25*5L
# or
dtype = 5%%6
# or
dtype = 2L + 49L * 3L + 21L - 19L / 21L

# Data type identification codes
typeof(dtype)
# or
class(dtype)
# or
storage.mode(dtype)

# The next code is asking R to confirm the data type
is.numeric(dtype) # is dtype a numeric data type? - TRUE or FALSE
# or
is.double(dtype) # is dtype a double data type? - TRUE or FALSE'''
                R()
                st.code(c)
                Res()
                st.text(''' "numeric" or "double" ''')
                st.caption('''The result of the typeof() code is "double" while that of class() is "numeric"''')

                c = ''' # Float Data Type in Python
dtype = 0.12
# or
dtype = 2356.1
# or
dtype = 100/100
# or
dtype = 1/3

# Data type identification codes
type(dtype)
# or
# The next code is asking Python to confirm the data type
isinstance(dtype, float) # is dtype a float data type? True or False
'''
                P()
                st.code(c)
                Res()
                dtype = 1/3
                # Data type identification codes
                st.write(type(dtype))
                st.caption('''Mathematical division is seen as float in python and as numeric or double
                in R.''')

                st.write('**Logical Data Type in R and the Boolean Data Type in Python**')
                
                c = ''' # Logical Data Type in R
dtype = TRUE
# or
dtype = FALSE

# Data type identification codes
typeof(dtype)
# or
class(dtype)
# or
storage.mode(dtype)

# The next code is asking R to confirm the data type
is.logical(dtype) # is dtype a logical data type? - TRUE or FALSE'''
                R()
                st.code(c)
                Res()
                st.text(''' "logical" ''')
                

                c = ''' # Boolean Data Type in Python
dtype = True
# or
dtype = False

# Data type identification codes
type(dtype)
# or
# The next code is asking Python to confirm the data type
isinstance(dtype, bool) # is dtype a boolean data type? True or False
'''
                P()
                st.code(c)
                Res()
                dtype = False
                st.text(type(dtype))
                #st.text(''' bool ''')
                st.caption('''The difference in this instance is in the names(bool and logical), the code construct are almost
                exactly the same except that you have 'True or False' in Python and 'TRUE or FALSE' in R.''')

                App()
                st.write('''The knowledge of data types is at the core of understanding data gathering,
                collation, storage, and data reading. The small groceries store at the street corner has data
                but may not understand how to structure and collate them for proper storage and consequent reading.
                How do you come up with a dataset without the type of data that are necessary to capture the essence of 
                target subject matter? With the knowledge we have gained in this section we can develop a data
                collection and storage format for the grocery shop mentioned above. With this knowledge, raw 
                unorganized data becomes easy to arrange, into any format necessary for future actions.''')
                c = pd.DataFrame({'Column_Names': ['Date','Customer_Names','Gender','Location','Goods_Bought','Price','Discount','Debt_Status'],
                                "R's Data Type":['Date','Character','Character','Character','Character', 'Numeric, Double','Numeric, Double','Logical'],
                                "Pythonic Data Type":['Date','String','String','String','String','Float','Float','Boolean']})
                c
        
        
        def RL():
                st.caption('**---R Code: List---**')
        def RV():
                st.caption('**---R Code: Vector---**')
        def PL():
                st.caption('**---Python Code: List---**')
        def PT():
                st.caption('**---Python Code: Tuple---**')

        if struc == 'Atomic vectors and list in R vs. list and tuple in Python':
                st.write('**Introduction**')
                st.write('''Inherent in every definition of data is the word - **collection**. Basically, for you
                to have data, you must collect together things or items which you regard as informative 
                and good enough to provide a basis for reasoning, direction and action. In fact, in modern day data science
                what you collect as data can be anything ranging from numbers, words, measurements, observations,
                pictures, responses, sounds bites, music, videos, images etc. When you ask the question:
                how do we collect, gather, collate or '**structure**' these items together, you are indirectly
                seeking a container - a structure suitable enough to accommodate your collections. The way I collect
                pictures or images and represent them will be different from how I collect and represent real events 
                in numbers numbers or words, which may also be different from how I collate responses from a survey.
                To this end, the data collection methodology is the data structure. R and Python provide some data
                collection or structure types.''')

                st.write('**Vectors and Lists in R, Lists and Tuples in Python**')

                st.write('''A list in R is simply an atomic vector in a generic sense - it can contain a mixture
                of R data types and can contain other lists. An atomic vectors on the other hand holds data of a 
                single data type. For Python, list is simply a collection of items separated by commas in 
                inside square brackets. The above definition is definately layman and just a means of 
                identification. In a deeper sense a list in either for Python or R is the most rugged data
                structure, it serves as a proper container for all data types while the atomic vectors in 
                R discriminates between data types and rejects combinations, a list says: 'bring them on'.''')

                st.write('---')
                st.write('**This Section is Deactivated**')
                kedi = st.radio(label = 'Select a Topic', options = ['Hold',
                                                                'Empty Vectors, Lists and Tuple',
                                                                'Populating Vectors, Lists and Tuples',
                                                                'Vectors -> <- List and List -> <- Tuples',
                                                                'Manipulating Vectors Lists and Tuples',
                                                                'Rython Numeric Sequences',
                                                                'Access Elements of Vectors Lists and Tuples'
                                                                ])

                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                

#                 if kedi == 'Empty Vectors, Lists and Tuple':
                
#                         st.write('')
#                         st.write("**Empty Vectors, Lists and Tuple**")
#                         st.write('''Since a vector in R is homogenous - holds data of the same data type, it means
#                 you can create a vector of the different data types in R. To this end, a vector is always a vector 
#                 of a particular data type, whereas a list is a collection of a single data type or different data types.''')
#                         c = '''# Empty vector in R
# # This is the default vector with no assignment of length and data type
# vect = vector()
# vect

# # What is the data type of the default vector?
# class(vect)
# # or
# typeof(vect)
# # or
# storage.mode(vect)

# # The next code is asking R to confirm the data type is logical
# is.logical(vect)
# # The next code is asking R to confirm if the data structure is a vector
# is.vector(vect)
# '''
#                         RV()
#                         st.code(c)
#                         Res()
#                         st.write('logical(0)')

#                         c = '''# empty list with length 0 in R
# list_R <- list()
# list_R
# # or
# list_R = list()
# list_R

# # find the data structure type
# typeof(list_R)
# # or
# class(list_R)
# # or
# storage.mode(list_R)

# # Is the data structure a list?
# is.list(list_R)
# '''
#                         RL()
#                         st.code(c)
#                         Res()
#                         st.write('list()')

#                         c = '''# Empty list in Python
# py_list = []
# py_list

# # find the data structure type
# type(py_list)

# # Is the data structure a list?
# isinstance(py_list, list)'''
#                         st.write('')
#                         PL()
#                         st.code(c)
#                         Res()
#                         st.text([])

#                         c = '''# Empty tuple in Python
# py_tuple = ()
# py_tuple

# # find the data structure type
# type(py_tuple)

# # Is the data structure a tuple?
# isinstance(py_tuple, tuple)'''
#                         st.write('')
#                         PT()
#                         st.code(c)
#                         Res()
#                         py_tuple = ()
#                         st.text(py_tuple)

#                         st.write('''From the above, we can see that the empty list in Python is a vacant closed 
#                         pair of square barckets. A pair of closed circular barckets denote a vector and list in R and also
#                         a tuple in Python. The difference is the function before the barckets: 
# - list() = an empty list in R; 
# - vector() = an empty vector in R while 
# - () = a tuple in Python.
# - [] = a list in Python     
# Furthermore, an empty list is just an empty list in R because it has nothing within but an empty vector 
# in R is a logical vector, meaning it comes as a vector with logical data type.  
# In Python and in R, a bracket is an indication of the type of data type and data structure. This knowledge
# runs through the entire data analysis life cycle both in R and in Python. These are what we manipulate on a day
# to day basis to achieve our data analyses objectives.  
# To make more from data types you cannot leave them outside of brackets, immediately brackets are 
# introduced you change their forms and applications.''')

#                         st.write('')

#                         st.write("**Possible Contents of Vectors, Lists and Tuples**")
#                         st.write('''Just as we have said earlier, the vector in R is homogenous, it can only contain
#                         same data type at once. The lists and tuples can however contain 2 or more data types at once.
#                         To this end, the vector can be designed with a data type from the onset. It means you can
#                         specify the data type for a vector from the creation stage. The vector in R is like a house
#                         designed from the design stage to contain some specific type of finishings.''')

#                         c = '''
# # Empty numerical or double vector with lenght = 0 in R
# vect = vector(mode = 'numeric')
# vect
# # or
# vect = vector('numeric')
# vect
# # or
# vect = numeric()
# vect

# # Empty numerical or double vector with lenght = 10 in R
# vect = vector(mode = 'numeric', length = 10)
# vect
# # or
# vect = vector('numeric', length = 10)
# vect
# # or
# vect = numeric(10)
# vect

# # What is the data type?
# typeof(vect)
# # or
# class(vect)
# # or
# storage.mode(vect)

# # Is the data type numerical or double?
# is.numeric(vect)
# # or
# is.double(vect)
# # Is the data structure a vector?
# is.vector(vect)'''
#                         RV()
#                         st.code(c)
#                         st.caption('''The above shows the different ways of creating a vector of the numeric or 
#                         double data type and how to check and confirm the status(data type and structure).''')
#                         Res()
#                         st.write('''numeric(0)  
                
# [1] 0 0 0 0 0 0 0 0 0 0''')
                

#                         c = '''
# # Empty logical vector with lenght = 0 in R
# vect = vector('logical')
# vect
# # or
# vect = vector(mode = 'logical')
# vect
# # or
# vect = logical()
# vect

# # Empty logical vector with lenght = 10 in R
# vect = vector('logical', length = 10)
# vect
# # or
# vect = vector(mode = 'logical', length = 10)
# vect
# # or
# vect = logical(10)
# vect

# # What is the data type?
# typeof(vect)
# # or
# class(vect)
# # or
# storage.mode(vect)

# # Is the data type logical?
# is.logical(vect)
# # Is the data structure a vector?
# is.vector(vect)'''
#                         RV()
#                         st.code(c)
#                         st.write('')
#                         Res()
#                         st.write('''logical(0)  

# [1] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE''')


#                         c = '''
# # Empty character vector with lenght = 0 in R
# vect = vector('character')
# vect
# # or
# vect = vector(mode = 'character')
# vect
# # or
# vect = character()
# vect

# # Empty character vector with lenght = 10 in R
# vect = vector('character', length = 10)
# vect
# # or
# vect = vector(mode = 'character', length = 10)
# vect
# # or
# vect = character(10)
# vect

# # What is the data type?
# typeof(vect)
# # or
# class(vect)
# # or
# storage.mode(vect)

# # Is the data type = character?
# is.character(vect)
# # Is the data structure a vector?
# is.vector(vect)'''
#                         RV()
#                         st.code(c)
#                         Res()
#                         st.write('''character(0)  

# [1] "" "" "" "" "" "" "" "" "" ""''')

#                         c = '''# Empty integer vector with lenght = 0 in R
# vect = vector('integer')
# vect
# # or
# vect = vector(mode = 'integer')
# vect
# # or
# vect = integer()
# vect

# # Empty integer vector with lenght = 10 in R
# vect = vector('integer', length = 10)
# vect
# # or
# vect = vector(mode = 'integer', length = 10)
# vect
# # or
# vect = integer(10)
# vect

# # What is the data type?
# typeof(vect)
# # or
# class(vect)
# # or
# storage.mode(vect)

# # Is the data type = integer?
# is.integer(vect)
# # Is the data structure a vector?
# is.vector(vect)'''
#                         st.write('')
#                         RV()
#                         st.code(c)
#                         Res()
#                         st.write('''integer(0)  

# [1] 0 0 0 0 0 0 0 0 0 0''')


#                         c = '''# Empty complex vector with lenght = 0 in R
# vect = vector('complex')
# vect
# # or
# vect = vector(mode = 'complex')
# vect
# # or
# vect = complex()
# vect

# # Empty complex vector with lenght = 10 in R
# vect = vector('complex', length = 10)
# vect
# # or
# vect = vector(mode = 'complex', length = 10)
# vect
# # or
# vect = complex(10)
# vect

# # What is the data type?
# typeof(vect)
# # or
# class(vect)
# # or
# storage.mode(vect)

# # Is the data type = complex?
# is.complex(vect)
# # Is the data structure a vector?
# is.vector(vect)'''
#                         st.write('')
#                         RV()
#                         st.code(c)
#                         Res()
#                         st.write('''
# complex(0)''')
#                         st.write('''
# [1] 0+0i 0+0i 0+0i 0+0i 0+0i 0+0i 0+0i 0+0i 0+0i 0+0i''')

#                         st.write('''We have seen that vectors can be created with respect to each data type in R. 
#                         For lists in R and Python and tuple in Python you dont need to create them with respect to
#                         any data type because they can contain two or more different data types at once. Therefore, you do not need
#                         to specify a data type to create a list or a tuple. However, this does not mean that you cannot
#                         create a list or a tuple of the same data type.''')
#                         st.write('')

#                         c = '''# empty list with specified length in R
# list_R <- vector("list", length = 7) 
# list_R

# # What is the data structure?
# typeof(list_R)
# # or
# class(list_R)
# # or
# storage.mode(list_R)

# # Is the data structure a list?
# is.list(list_R)'''
#                         RL()
#                         st.code(c)
#                         Res()
#                         st.write('''[[1]]  
# NULL

# [[2]]  
# NULL

# [[3]]  
# NULL

# [[4]]  
# NULL

# [[5]]  
# NULL

# [[6]]  
# NULL

# [[7]]  
# NULL
# ''')
#                         c = '''# empty list with specified length in Python
# py_list = ['NULL']*7
# py_list

# # What is the data structure?
# type(py_list)

# # Is the data structure a list?
# isinstance(py_list, list)'''
#                         PL()
#                         st.code(c)
#                         Res()
#                         st.text(['NULL']*7)
                

#                         c = '''# empty tuple with specified length in Python
# py_tuple = ('NULL','NULL')*3
# py_tuple

# # What is the data structure?
# type(py_tuple)

# # Is the data structure a tuple?
# isinstance(py_tuple, tuple)'''
#                         PT()
#                         st.code(c)
#                         Res()
#                         st.text(('NULL','NULL')*3)
                        
#                         st.write('''For R, the list length assignment is inbuilt but for Python you have to
#                         replicate through multiplication to get same output. Also, the output of a list in
#                         R has a different display from that of a vector. The output of a list is vertically
#                         displayed while that of a vector is horizontal. Furthermore, the output of a list in Python
#                         comes with square backet while that of a tuple comes with the circular bracket.''')
                
                
#                 if kedi == 'Populating Vectors, Lists and Tuples':
#                         st.write('**Creating and Populating Vectors, Lists and Tuples**')

#                         c = '''
# # Create a vector with character data type as content in R
# vect <- c('Abuja','Accra','Lome', 'Pretoria','Cairo', 'Nairobi')
# vect

# # or you can also specify the data type from the beginning
# as.character(vect)

# # What is the data type in the vector?
# typeof(vect)
# # or
# class(vect)
# # or
# storage.mode(vect)

# # is the data type in the vector = character?
# is.character(vect)
# # Is the data structure a vector?
# is.vector(vect)
# '''
#                         RV()
#                         st.code(c)
#                         Res()
#                         st.write('[1] "Abuja"    "Accra"    "Lome"     "Pretoria" "Cairo"    "Nairobi"')


#                         c = '''
# # Create a list with character data type as content in R
# R_list <- list('Abuja','Accra','Lome', 'Pretoria','Cairo', 'Nairobi')
# R_list


# # Check the data type of any of the values
# # value on index position = 6
# class(R_list[[6]])
# # or
# # value on index position = 4
# typeof(R_list[[4]])
# # or
# # value on index position = 3
# storage.mode(R_list[[3]])

# # What is the data structure?
# typeof(R_list)
# # or
# class(R_list)
# # or
# storage.mode(R_list)


# # is the data structure = list?
# is.list(R_list)
# '''
#                         RL()
#                         st.code(c)
#                         Res()
#                         st.text('''[[1]]  
# [1] "Abuja"

# [[2]]  
# [1] "Accra"

# [[3]]  
# [1] "Lome"

# [[4]]  
# [1] "Pretoria"

# [[5]]  
# [1] "Cairo"

# [[6]]  
# [1] "Nairobi"''')

#                         c = '''# Create a list with string data type as content in Python
# py_list = ['Abuja','Accra','Lome', 'Pretoria','Cairo', 'Nairobi']
# py_list

# # Check the data type of any of the values
# # value on index position = 5
# type(py_list[5])

# # What is the data structure?
# type(py_list)

# # is the data structure = list?
# isinstance(py_list, list)
# '''
#                         PL()
#                         st.code(c)
#                         Res()
#                         py_list = ['Abuja','Accra','Lome', 'Pretoria','Cairo', 'Nairobi']
#                         st.text(py_list)
#                         st.caption('or')
#                         st.write(py_list)

#                         c = '''# Create a tuple with string data type as content in Python
# py_tuple = ('Abuja','Accra','Lome', 'Pretoria','Cairo', 'Nairobi')
# py_tuple

# # Check the data type of any of the values
# # value on index position = 1
# type(py_list[1])

# # What is the data structure?
# type(py_tuple)

# # is the data structure = list?
# isinstance(py_tuple, tuple)
# '''
#                         PT()
#                         st.code(c)
#                         Res()
#                         py_tuple = ('Abuja','Accra','Lome', 'Pretoria','Cairo', 'Nairobi')
#                         st.text(py_tuple)
#                         # st.write(py_tuple)

#                         st.write('''The outputs of Pythonic list and tuple and the list in R as demonstrated above have similar characteristics.
#                         They all come with quotes however, the display and the brackets are different, while the tuple and the
#                         list are separated by commas, the list in R is vertically numbered. The output of the vector
#                         comes without any barcket but it it is horizontal. The output of the list and tuple in Python
#                         can both be vertical or horizontal depending on the length.  
#                         For list and tuple you can check the data type by using the index positioning of each of
#                         the values as shown in the codes above. However, for a vector since it is homogenious - all values
#                         have same data type the same code apply to all, you have the same result for all values. There is 
#                         therefore no need to evaluate the index positions of each value.''')


#                         c = '''
# # Create a vector with numeric data type as content in R
# vect <- c(25, 59, 87, 135, 9, 201, 47, 998)
# vect

# # or you can also specify the data type from the beginning
# as.numeric(vect)

# # What is the data type in the vector?
# typeof(vect)
# # or
# class(vect)
# # or
# storage.mode(vect)

# # is the data type in the vector = character?
# is.numeric(vect)
# # Is the data structure a vector?
# is.vector(vect)
# '''
#                         RV()
#                         st.code(c)
#                         Res()
#                         st.write('[1]  25  59  87 135   9 201  47 998')


#                         c = '''
# # Create a list with numeric or double data type as content in R
# R_list <- list(25, 59, 87, 135, 9, 201, 47, 998)
# R_list

# # Check the data type of any of the values
# # value on index position = 6
# class(R_list[[6]])
# # or
# # value on index position = 4
# typeof(R_list[[4]])
# # or
# # value on index position = 3
# storage.mode(R_list[[3]])

# # What is the data structure?
# typeof(R_list)
# # or
# class(R_list)
# # or
# storage.mode(R_list)

# # is the data structure = list?
# is.list(R_list)
# '''
#                         RL()
#                         st.code(c)
#                         Res()
#                         st.text('''[[1]]  
# [1] 25

# [[2]]  
# [1] 59

# [[3]]  
# [1] 87

# [[4]]  
# [1] 135

# [[5]]  
# [1] 9

# [[6]]  
# [1] 201

# [[7]]  
# [1] 47

# [[8]]  
# [1] 998''')

#                         c = '''# Create a list with integer data type as content in Python
# py_list = [25, 59, 87, 135, 9, 201, 47, 998]
# py_list

# # Check the data type of any of the values
# # value on index position = 5
# type(py_list[5])

# # What is the data structure?
# type(py_list)

# # is the data structure = list?
# isinstance(py_list, list)
# '''
#                         PL()
#                         st.code(c)
#                         Res()
#                         py_list = [25, 59, 87, 135, 9, 201, 47, 998]
#                         st.text(py_list)
#                         st.caption('or')
#                         st.write(py_list)

#                         c = '''# Create a tuple with integer data type as content in Python
# py_tuple = (25, 59, 87, 135, 9, 201, 47, 998)
# py_tuple

# # Check the data type of any of the values
# # value on index position = 1
# type(py_list[1])

# # What is the data structure?
# type(py_tuple)

# # is the data structure = list?
# isinstance(py_tuple, tuple)
# '''
#                         PT()
#                         st.code(c)
#                         Res()
#                         py_tuple = (25, 59, 87, 135, 9, 201, 47, 998)
#                         st.text(py_tuple)
#                         st.write('''You can create lists, tuples and vectors for other data types using same code
#                         format as above.''')


#                         c = '''
# # Create a vector with a mixture of data types in R

# # This vector contains all the data types in R
# vect <- c(1L, 8L, 78L, 111L, 213L, 45, FALSE, 4i+6i, 'London', 78.9, TRUE)
# vect


# # or you can also specify the data type from the beginning
# as.numeric(vect)

# # What is the data type in the vector?
# typeof(vect)
# # or
# class(vect)
# # or
# storage.mode(vect)
# # or
# typeof(vect[[8]])


# # is the data type in the vector = character?
# is.numeric(vect)
# # Is the data structure a vector?
# is.character(vect)
# '''
#                         RV()
#                         st.code(c)
#                         Res()
#                         st.write('''[1] "1"      "8"      "78"     "111"    "213"    "45"     "FALSE"  "0+10i"   
#                         [9] "London" "78.9"   "TRUE" ''')
#                         st.write('''As you can see from the above result, the vector converted all data types
#                         into the character data type thereby overriding the other data types. A vector can only accommodate
#                         one data type at once - homogenious. It was supposed to have thrown an error but a vector
#                         is built in such a way to recognise one of the data type when they are mixed togther
#                         this might however not be very useful for the intended purpose for the data. Let us try
#                         the same with list. Run all the codes line by line in RStudio to check the results,
#                         I tried coercing the vector into a numeric vector it threw an error.''')


#                         c = '''
# # Create a list with a mixture of data types in R

# # This list contains all the data types in R
# R_list <- list(213L, 45, FALSE, 4i+6i, 'London', 78.9, TRUE)
# R_list

# # Check the data type of any of the values

# # data type of the value on index position = 7
# class(R_list[[7]])
# # or
# # data type of the value on index position = 4
# typeof(R_list[[4]])
# # or
# # data type of the value on index position = 1
# storage.mode(R_list[[1]])
# # or
# # data type of the value on index position = 5
# class(R_list[[5]])
# # or
# # data type of the value on index position = 2
# typeof(R_list[[2]])


# # What is the data structure?
# typeof(R_list)
# # or
# class(R_list)
# # or
# storage.mode(R_list)

# # is the data structure = list?
# is.list(R_list)
# '''
#                         RL()
#                         st.code(c)
#                         Res()
#                         st.text('''
# code:- R_list
# Result:
# [[1]]
# [1] 213

# [[2]]
# [1] 45

# [[3]]
# [1] FALSE

# [[4]]
# [1] 0+10i

# [[5]]
# [1] "London"

# [[6]]
# [1] 78.9

# [[7]]
# [1] TRUE''')

# # code:- class(R_list[[7]])
# # Result:
# # [1] "logical"

# # code:- typeof(R_list[[4]])
# # Result:
# # [1] "complex"

# # code:- storage.mode(R_list[[1]])
# # Result:
# # [1] "integer"

# # code:- class(R_list[[5]])
# # Result:
# # [1] "character"

# # code:- typeof(R_list[[2]])
# # Result:
# # [1] "double"

#                         st.write('''The list above accounted for all the data types separately, run each of the codes
#                         to check the data types of each of the values. However, we can check the different data type
#                         in a list with one line of code.''')

#                         c = '''# Code to check all data types in R at once
# # list with different data types
# R_list <- list(213L, 45, FALSE, 4i+6i, 'London', 78.9, TRUE)
# R_list

# # Codes to check all data types at once
# str(R_list)
# summary(R_list)
# '''
#                         R()
#                         st.code(c)
#                         Res()
#                         st.text('''code:- str(R_list)
# # Result
# List of 7      
#  $ : int 213       
#  $ : num 45      
#  $ : logi FALSE       
#  $ : cplx 0+10i       
#  $ : chr "London"      
#  $ : num 78.9      
#  $ : logi TRUE        
 

# # or
# code:- summary(R_list)
# # Result
# Length Class  Mode     
# [1,] 1      -none- numeric  
# [2,] 1      -none- numeric  
# [3,] 1      -none- logical  
# [4,] 1      -none- complex  
# [5,] 1      -none- character
# [6,] 1      -none- numeric  
# [7,] 1      -none- logical''')

#                         c = '''# Create a list with a mixture of data types in Python

# # This list contains all the data types in Python
# py_list = ['London',209, False, 12.6, 4j+2.6j-2j, True, 0.98]
# py_list


# # Check the data type of any of the values
# # value on index position = 5
# type(py_list[5])
# # or
# # value on index position = 4
# type(py_list[4])
# # or
# # value on index position = 0
# type(py_list[0])


# # What is the data structure?
# type(py_list)

# # is the data structure = list?
# isinstance(py_list, list)
# '''
#                         PL()
#                         st.code(c)
#                         Res()
#                         py_list = ['London',209, False, 12.6, 4j+2.6j-2j, True, 0.98]
#                         st.text(py_list)
#                         st.caption('or')
#                         st.write(py_list)

                
#                         c = '''# Create a tuple with a mixture of data types in Python

# # This tuple contains all the data types in Python
# py_tuple = ('London',209, False, 12.6, 4j+2.6j-2j, True, 0.98)
# py_tuple


# # Check the data type of any of the values
# # value on index position = 5
# type(py_tuple[5])
# # value on index position = 1
# type(py_tuple[1])
# # or
# # value on index position = 4
# type(py_tuple[4])
# # or
# # value on index position = 0
# type(py_tuple[0])


# # What is the data structure?
# type(py_tuple)

# # is the data structure = list?
# isinstance(py_tuple, tuple)
# '''
#                         PT()
#                         st.code(c)
#                         Res()
#                         py_tuple = ('London',209, False, 12.6, 4j+2.6j-2j, True, 0.98)
#                         st.text(py_tuple)
#                         st.write('''From the above we can see that when it comes to list amd tuples all data types
#                         are accommodated and accounted for at once while the vector in R can accomodate all data types
#                         at once without throwing an error but it only account for only one of the data types. In fact
#                         it convert all the other data types into this one overriding data type.''')


#                 if kedi == 'Vectors -> <- List and List -> <- Tuples':        
#                         st.write('''**Convert Lists to Vectors and vice versa in R**''')

#                         c = '''# Convert a vector to a list in R

# # create a vector of alphabet a to j in uppercase
# vect <- LETTERS[1:10]
# vect

# # create a vector of alphabet a to j in lowercase
# vect <- letters[1:10]
# vect

# # convert the vector into list
# code format:- list_name <- as.list(vector_name)
# R_list <- as.list(vect)
# R_list
# # check it out
# typeof(R_list)

# # convert list to vector
# R_list = list('Mangoes', 'Oranges', 'Apple', 'Berry')
# R_list
# # convert to character vector
# vect <- as.character(R_list)
# # or
# # remove the list using the unlist function
# vect <- unlist(R_list)
# vect

# # Other examples of vectors to lists
# vect = c(6:30)
# vect
# R_list = as.list(vect)
# R_list

# vect = seq(6:30)
# vect
# R_list = as.list(vect)
# R_list

# # lists to vectors
# R_list1 <- list(1L:5L)
# R_list2 <- list(10:14)

# vect1 <- unlist(R_list1)
# vect1
# vect2 <- unlist(R_list2)
# vect2
# '''
#                         R()
#                         st.code(c)
#                         Res()
#                         st.write('Result 1')
#                         st.text('''[1] "A" "B" "C" "D" "E" "F" "G" "H" "I" "J"''')
#                         st.write('Result 2')
#                         st.text('''[[1]]
# [1] "A"

# [[2]]
# [1] "B"

# [[3]]
# [1] "C"

# [[4]]
# [1] "D"

# [[5]]
# [1] "E"

# [[6]]
# [1] "F"

# [[7]]
# [1] "G"

# [[8]]
# [1] "H"

# [[9]]
# [1] "I"

# [[10]]
# [1] "J"
# ''')
#                         st.text('')
#                         st.write('**Convert Lists to Tuples and vice versa in Python**')

#                         c = '''# Convert a lists to a tuple in Python

# # create a list of alphabets from a to j in uppercase
# import string
# py_list = list(string.ascii_uppercase[0:10])
# py_list

# # create a list of alphabets from a to j in lowercase
# py_list = list(string.ascii_lowercase[0:10])
# py_list

# # convert the list to tuple
# py_tuple = (*py_list,)
# # or
# py_tuple = tuple(py_list)
# py_tuple
# # check it out
# type(py_tuple)

# # convert tuple to list
# py_tuple = ('Mangoes', 'Oranges', 'Apple', 'Berry')
# py_tuple

# py_list = [*py_tuple, ]
# # or
# py_list = list(py_list)
# py_list

# # number range to tuple and to lists
# numb_Range = range(6,30)
# # convert to list
# list(numb_Range)
# # convert to tuple
# tuple(numb_Range)
# '''
#                         P()
#                         st.code(c)
#                         Res()
#                         import string
#                         py_list = list(string.ascii_uppercase[0:10])
#                         st.text(py_list)
#                         st.write('or')
#                         py_list
#                         # convert the list to tuple
#                         py_tuple = (*py_list,)
#                         # or
#                         # py_tuple = tuple(py_list)
#                         st.text(py_tuple)
#                         # check it out
#                         # type(py_tuple)
#                         numb_Range = range(6,30)
#                         st.write('number range to list')
#                         st.text(list(numb_Range))
#                         st.write('number range to tuple')
#                         st.text(tuple(numb_Range))

#                 st.write('')
#                 if kedi == 'Manipulating Vectors Lists and Tuples':
#                         st.write('''**Manipulating Vectors Lists and Tuples**''')

#                         c = '''# add elements to a vector or add a vector to another vector
# x <- c('Abuja','Accra','Lome', 'Pretoria','Cairo', 'Nairobi')
# # add Tripoli  to the list at the end
# x[7] <- 'Tripoli'
# # or
# y <- c(x, 'Tripoli')
# # or
# y <- append(x, 'Tripoli')

# # add Cotonou to the list from the beginning
# x[1] <- 'Cotonou'
# # or
# vect <- c('Cotonou', y)
# # or
# vect <- append('Cotonou', y)
# vect

# # insert Yaounde on index position = 4
# # code format:- append(vector_name, element to append, after = index address(usually a number))
# append(x, 'Yaounde', after = 3)


# # add two or more vectors together
# x <- c('Abuja','Accra','Lome','Pretoria','Cairo','Nairobi')
# b <- c('Tipoli','Cotonou','Algiers','Rabat','Moscow','London')
# c <- c('Bueno Aries','Lima','Toronto')
# vect <- c(x, b, c)
# # or
# z <- append(x,b)
# vect <- append(z,c)
# vect


# # insert a vector in a particular index position = 3
# # code format:- append(vector_name, vector to append, after = index address(usually a number))
# append(x, c, after = 2)
# '''
#                         RV()
#                         st.code(c)
#                         Res()
#                         st.text('''Result 1:
# [1] "Cotonou"  "Abuja"    "Accra"    "Lome"     "Pretoria" "Cairo"    "Nairobi" 
# [8] "Tripoli"

# Result 2:
# [1] "Abuja"       "Accra"       "Lome"        "Pretoria"    "Cairo"      
# [6] "Nairobi"     "Tipoli"      "Cotonou"     "Algiers"     "Rabat"      
# [11] "Moscow"      "London"      "Bueno Aries" "Lima"        "Toronto"  
# ''')

#                         c = '''# add elements to a list or add a list to another list in R
# x <- list('Abuja','Accra','Lome', 'Pretoria','Cairo', 'Nairobi')
# # add Tripoli  to the list at the end
# x[7] <- 'Tripoli'
# # or
# y <- c(x, 'Tripoli')
# # or
# y <- append(x, 'Tripoli')

# # add Cotonou to the list from the beginning
# x[1] <- 'Cotonou'
# # or
# R_list <- c('Cotonou', y)
# # or
# R_list <- append('Cotonou', y)
# R_list

# # insert Yaounde on index position = 3
# # code format:- append(list_name, element to append, after = index address(usually a number))
# append(x, 'Yaounde', after = 2)

# # add two or more lists togther in R
# x <- list('Abuja','Accra','Lome','Pretoria','Cairo','Nairobi')
# b <- list('Tipoli','Cotonou','Algiers','Rabat','Moscow','London')
# c <- list('Bueno Aries','Lima','Toronto')
# R_list <- c(x, b, c)
# # or
# z <- append(x,b)
# R_list<- append(z,c)
# R_list

# # insert a list in a particular index position = 3
# # code format:- append(list_name, list to append, after = index address(usually a number))
# append(x, c, after = 2)
# '''
#                         RL()
#                         st.code(c)
#                         Res()
#                         st.text('''Result 1
# [[1]]
# [1] "Cotonou"

# [[2]]
# [1] "Abuja"

# [[3]]
# [1] "Accra"

# [[4]]
# [1] "Lome"

# [[5]]
# [1] "Pretoria"

# [[6]]
# [1] "Cairo"

# [[7]]
# [1] "Nairobi"

# [[8]]
# [1] "Tripoli"


# Result 2
# [[1]]
# [1] "Abuja"

# [[2]]
# [1] "Accra"

# [[3]]
# [1] "Lome"

# [[4]]
# [1] "Pretoria"

# [[5]]
# [1] "Cairo"

# [[6]]
# [1] "Nairobi"

# [[7]]
# [1] "Tipoli"

# [[8]]
# [1] "Cotonou"

# [[9]]
# [1] "Algiers"

# [[10]]
# [1] "Rabat"

# [[11]]
# [1] "Moscow"

# [[12]]
# [1] "London"

# [[13]]
# [1] "Bueno Aries"

# [[14]]
# [1] "Lima"

# [[15]]
# [1] "Toronto"
# ''')

#                         c = '''# Add an item a list or a tuple to the end of the list in Python
# py_list = ['Abuja','Accra','Lome', 'Pretoria','Cairo', 'Nairobi']
# # add Tripoli  to the list at the end
# py_list[len(py_list):] = ['Tripoli']
# py_list
# # you can also use append to achieve the above
# py_list.append('Tripoli')
# py_list

# # add a list or tuple to the end of a list
# py_list1 = ['Abuja','Accra','Lome','Pretoria','Cairo','Nairobi']
# py_list2 = ['Tipoli','Cotonou','Algiers','Rabat','Moscow','London']
# # add py_list 2 at the end of py_list1
# py_list1[len(py_list1):] = [py_list2]
# # or
# py_list1.append(py_list2)
# py_list1

# # add py_tuple at the end of py_list
# py_list = ['Abuja','Accra','Lome','Pretoria','Cairo','Nairobi']
# py_tuple = ('Tipoli','Cotonou','Algiers','Rabat','Moscow','London')
# py_list[len(py_list):] = [py_tuple]
# # or
# py_list.append(py_tuple)
# py_list

# # empty a list in a list by extending the number of elements
# py_list1 = ['Abuja','Accra','Lome','Pretoria','Cairo','Nairobi']
# py_list2 = ['Tipoli','Cotonou','Algiers','Rabat','Moscow','London']
# py_list3 = ['Bueno Aries','Lima','Toronto']
# py_list1[len(py_list1):] = py_list2
# # or
# py_list1.extend(py_list2)
# py_list1

# # insert an item or a list in a given index position
# fruits1 = ['Mangoes', 'Oranges', 'Apple', 'Berry']
# fruits2 = ['Carrot', 'Tangerine', 'Cashew']
# # insert an element - Wallnut in index position 3
# # code format:- list_name(index_position, new_item_to_add)
# fruits1.insert(3, 'Wallnut')
# fruits1
# # insert a list - fruit2 in index position 1
# # code format:- list_name1(index_position, list_name2)
# fruits1.insert(1, fruits2)
# fruits1

# # insert a tuple in an index position
# # code format:- tuple_name(index_position, tuple_name)
# fruits3 = ('Banana', 'Cherry', 'Watermelon', 'Lime', 'Plum', 'Apricot')
# fruits1.insert(1, fruits3)
# fruits1
# '''
#                         PL()
#                         st.code(c)
#                         Res()
#                         py_list = ['Abuja','Accra','Lome', 'Pretoria','Cairo', 'Nairobi']
#                         py_list[len(py_list):] = ['Tripoli']
#                         st.write('Result 1')
#                         st.caption('add Tripoli  to the list at the end')
#                         st.text(py_list)
#                         st.text('or')
#                         py_list

#                         st.caption('add a list or tuple to the end of a list')
#                         py_list1 = ['Abuja','Accra','Lome','Pretoria','Cairo','Nairobi']
#                         py_list2 = ['Tipoli','Cotonou','Algiers','Rabat','Moscow','London']
#                         py_list1[len(py_list1):] = [py_list2]
#                         st.write('Result 2')
#                         st.text(py_list1)
#                         st.text('or')
#                         py_list1

#                         py_list1 = ['Abuja','Accra','Lome','Pretoria','Cairo','Nairobi']
#                         py_list2 = ['Tipoli','Cotonou','Algiers','Rabat','Moscow','London']
#                         py_list3 = ['Bueno Aries','Lima','Toronto']
#                         #py_list1[len(py_list1):] = py_list2
#                         st.write('Result 3')
#                         st.caption('''empty a list in a list by extending the number of elements''')
#                         py_list1.extend(py_list2)
#                         py_list1


#                         st.write('''Tuples are immutable, the values cannot be changes neither can you update
#                         the tuple itself. Therefore, you cannot add items to a tuple. However, the only way you can
#                         increase the tuple to to add two or more different tuples together as demonstrated below.''')
                        
#                         c = '''# add tuples together
# country = ('COUNTRY:-','Ghana', 'Nigeria', 'Canada', 'Japan','France')
# capital = ('CAPITAL:-','Accra','Lagos','Ontario','Tokyo','Paris')
# continent = ('CONTINENT:-', 'Africa','Africa','North America','Asia','Europe')
# print(country + capital)
# print(country + capital + continent)'''
#                         PT()
#                         st.code(c)
#                         Res()
#                         country = ('COUNTRY:-','Ghana', 'Nigeria', 'Canada', 'Japan','France')
#                         capital = ('CAPITAL:-','Accra','Lagos','Ontario','Tokyo','Paris')
#                         continent = ('CONTINENT:-', 'Africa','Africa','North America','Asia','Europe')
#                         st.text(country + capital)
#                         st.text('or')
#                         st.write(list(country + capital))
#                         st.text((country + capital + continent))
#                         st.write('or')
#                         st.write(list(country + capital + continent))
#                         st.write('')

#                         st.write('''**Remove Elements from Vectors Lists and Tuples**''')

#                         c = '''# Remove elements from vectors
# # remove an item from a vector
# vect = c(23,45,67,89,19, 100, 45)
# # remove one item on index position = 2
# vect[-2]
# # remove more than one item on index positions = 1, 5, 7
# vect[-c(1,5,7)]
# # remove a sequence using index
# # code format:- vector_name[-c(first_index : last_index)]
# vect[-c(1:3)]

# # remove the last 4 elements
# head(vect,-4)
# # remove the last item
# vect[-length(vect)]

# # or

# # remove one or more items
# # code format:- vector_name[!(vector_name%in% c(elements to be removed))]
# vect[!(vect%in% c(89,100))]
# # remove a sequence using elements
# # code format:- vector_name[!vect %in% c(start : stop)]
# vect[!vect%in% c(0:80)] # remove all numbers from 0 to 80

# # remove items based on conditions
# # remove every value greater than 50 including those less than 10
# vect[!(vect > 50)]
# vect[!(vect < 10)]
# vect[!(vect > 50 | vect < 10)]


# # display values between 40 and 70
# vect[!(vect > 70)]
# vect[!(vect < 40)]
# vect[!(vect > 70 | vect < 40)]

# # students must learn the difference between | and & in R operations

# # remove values greater than 20 and those less than 70
# vect[!(vect > 20 & vect < 70)]

# # remove a vector totally from memory
# # code format:- rm(vector_name)
# rm(vect)
# '''
#                         RV()
#                         st.code(c)
#                         Res()

#                         c = '''# Remove elements from lists in R
# # remove an item from a list
# fruits = list('Banana', 'Cherry', 'Watermelon', 'Lime', 'Plum', 'Apricot')
# fruits
# # remove the first element = Banana
# # code format:- list_name[index address of element to remove] <- NULL
# fruits[1] <- NULL
# # or
# fruits[-1]
# # remove the first 3 elements = Banana, Cherry and Watermelon
# fruits[1:3] <- NULL
# # or
# # code format:- list_name[-c(first_index : last_index)]
# fruits[-(1:3)]
# # or
# fruits[-c(1,2,3)]
# # remove all items = NULL
# fruits <- NULL
# fruits


# R_list = list(23,45,67,89,19, 100, 45)
# # remove one item on index position = 2
# # code format:- list_name[index address of element to remove] <- NULL
# R_list[2] <- NULL
# # or
# R_list[-2]
# # remove more than one item on index positions = 1, 5, 7
# R_list[-c(1,5,7)]
# # remove a sequence using index
# # code format:- list_name[-c(first_index : last_index)]
# R_list[-c(1:3)]

# # remove the last 4 elements
# head(R_list,-4)
# # remove the last item
# fruits[-length(fruits)]

# # or - removing actual items

# # remove one or more actual items
# # code format:- list_name[!(list_name%in% c(elements to be removed separated by commas))]
# fruits[!(fruits%in% c('Watermelon','Plum'))]
# R_list[!(R_list%in% c(89,100))]
# # remove a sequence using elements
# # code format:- list_name[!list_name %in% c(start : stop)]
# R_list[!R_list%in% c(0:80)] # remove all numbers from 0 to 80
# # remove all items 
# R_list[!(R_list%in% c(R_list))] # = empty list

# # remove items based on conditions
# # remove every value greater than 50 including those less than 10
# R_list[!(R_list > 50)]
# R_list[!(R_list < 10)]
# R_list[!(R_list > 50 | R_list < 10)]

# # display values between 40 and 70
# R_list[!(R_list > 70)]
# R_list[!(R_list < 40)]
# R_list[!(R_list > 70 | vect < 40)]

# # remove values greater than 20 and those less than 70
# R_list[!(R_list > 20 & R_list < 70)]

# # create a condition to remove all items
# R_list[!(R_list > 0)] # = empty list

# # remove a list totally from memory
# # code format:- rm(list_name)
# rm(R_list)
# # or
# rm(fruits)
# '''
#                         RL()
#                         st.code(c)
#                         Res()

#                         c = '''# Remove elements from lists in Python
# # remove an item from a list
# fruits = ['Banana', 'Cherry', 'Watermelon', 'Lime', 'Plum', 'Apricot']
# fruits
# fruits.remove('Lime')
# fruits

# # Remove an item form an index position
# vegitables = ['Broccoli','Tomatoes','Carrots','Spinach','Cauliflower','Cabbage','Onions','Lettuce','Peas','Garlic','Cucumber']
# vegitables

# # remove the last vegitable on the list
# vegitables.pop()
# vegitables

# # remove the vegitable on index position = 7 = Lettuce
# vegitables.pop(7)
# vegitables

# # remove multiple vegitables from the list
# vegitables2 = ['Carrots','Cabbage','Onions','Peas']
# # remove Vegitables2 from Vegitables
# vegitables3 = list(set(vegitables) - set(vegitables2))
# vegitables3

# # remove multiple items based on index address

# # remove the first vegitable
# del vegitables[0]
# # or
# del vegitables[:1]
# vegitables
# # remove the last vegitable
# del vegitables[-1]
# # remove vegitables from index 0 to 7
# del vegitables[0:7]
# vegitables
# # remove from vegitable number 6 to the end
# del vegitables[5:]
# vegitables
# # remove the first 5 vegitables
# del vegitables[:5]
# vegitables
# # remove all vegitables
# del vegitables[0:] # = empty list
# vegitables
# # or
# del vegitables
# # or
# vegitables.clear() # = empty list
# vegitables
# '''
#                         PL()
#                         st.code(c)
#                         #Res()
#                         st.write('''You cannot remove an item in a tuple, however, you can delete an entire tuple
#                         using the same code as used in list = del tuple''')

#                 #st.write('')

#                 if kedi == 'Rython Numeric Sequences':
#                         st.write('**Rython Numeric Sequences**')
#                         st.write('''You might need to generate a sequence of numbers in both R and Python
#                         for specific purposes and tasks. Both langauges provide you with inbuilt functions
#                         for such purposes.''')
#                         st.write('**Generate Vectors of Numeric Sequence in R**')

#                         c = '''# Sequence of numbers in R
# # generate sequence of numbers from 6 to 30
# vect = c(6:30)
# # or
# vect = seq(6,30)
# # or
# 6:30
# vect

# # generates a sequence of number from 1 to 20
# seq(20)
# # or
# seq(1:20)
# # or
# seq(1,20)

# # code_format:- seq(lower_limit : upper_limit)
# vect = seq(10:30)
# vect # difference between lower_limit and Upper_limit + 1

# # sequence starting from pi = 3.14 or (22/7)
# pi:20
# # or
# seq(pi,20)
# # sequence in descending order
# 15:1
# # or
# seq(15:1)

# # sequence with conditions

# # sequence of odd numbers
# seq(1,20,2) # sequence of numbers from 1 to 20 step = 2
# # or
# seq(from = 1, to = 20, by = 2)
# # sequence of even numbers
# seq(2,20,2) # sequence of numbers from 2 to 20 step = 2
# # or
# seq(from = 2, to = 20, by = 2)
# # sequence of numbers divisible by 5
# seq(0,20,5)
# # or
# seq(from = 0, to = 100, by = 5)
# # sequence of numbers divisible by 10
# seq(0,20,10)
# # or
# seq(from = 0, to = 100, by = 10)


# # generate decimal numbers with measured difference
# seq(from = 1, to = 10, by = 0.1)
# # generate decimal numbers with measured difference in reverse order
# seq(from = 10, to = 1, by = -0.1)
# # specify the length of sequence to create measure sequence of whole and decimal numbers
# seq(1, 20, length = 11)

# # generate repitition

# # repeat integer 8 for 10 times
# rep(8,times = 10)
# # you can practically repeat all data types
# # repeat London - character 7 times
# rep('London', time = 7)
# # repeat complex numbers
# rep(56i+67i, time = 10)
# # repeat logical data type
# rep(FALSE, time = 9)
# rep(TRUE, time = 15)
# '''
#                         RV()
#                         st.code(c)
#                         st.write('''Note that all numeric sequence can also be generated using R integers
#                         identifiable with the use of L. Numeric and Integer generated sequences have same result.
#                         Also, you can always convert the vectors of numeric sequence to lists to get the list version by
#                         using as.list(vector). Check the conversion section above.''')
#                         #Res()

#                         st.write('')
#                         st.write('**Generate Lists and Tuples of Numeric Sequence in Python**')
                
#                         c = ''' # Lists and Tuple of numeric sequence
# # a list and tuple of numbers from 0 to 30
# list(range(0,31))
# # or 
# list(range(31))

# tuple(range(0,31))
# # or 
# tuple(range(11))

# # a sequence of even numbers from 1 to 20 in tuple and list
# # code_format:- list(range(lower_limit, upper_limit, sequence_difference))
# tuple(range(2,21,2))
# list(range(2,21,2))

# # sequence in descending order
# tuple(reversed(range(16)))
# # or
# tuple(reversed(range(1, 16)))

# list(reversed(range(16)))
# # or
# list(reversed(range(1, 16)))
# '''
#                         PL()
#                         PT()
#                         st.code(c)

#                         st.write('')
#                         st.write('''**Access Elements of Vectors Lists and Tuples**''')             
                
#                 if kedi == 'Access Elements of Vectors Lists and Tuples':
#                         st.write('**Access Elements of Vectors, Lists and Tuples**')
#                         st.write('''Making use of the values or elements of lists, vectors and tuples in
#                         Python and R is necessry because the reason for their creation is basically to make use of the
#                         elements. For example, we might need to examine or work on the employees who were employed
#                         in some certain years or the students admitted during some months or a group of numbers which
#                         falls within certain parameters etc.''')

#                         st.write('**Access Elements of Vectors and Lists in R**')
#                         c = '''
# # create a vector or a list
# cities <- c('Bradford','Manchester','Leeds','London','Liverpool')
# # generate months name from Janaury to December
# months <- (month.name) # Full months names
# # or
# months = month.abb # abbrevated months names
# # convert the vectors above to list
# as.list(cities)
# as.list(months)

# # use index position to access 3 months = April, August and December
# months[c(4,8,12)]
# # access months from April to August
# months[c(4:8)]
# # use negative numbers to remove the months you dont want
# # this code remove August, April, November
# months[c(-8, -4, -11)]
# # use logical datatype to access elements
# # this code looks through the vector and altenate its results
# # TRUE displays element in that position while FALSE does otherwise
# months[c(TRUE,FALSE)]
# cities[c(FALSE, TRUE)]
# '''
#                         RV()
#                         st.code(c)

#                         st.write('**Access Elements of Lists and Tuple in Python**')
                        
#                         c = '''# Create a list of English dishes
# foods = ["Shepherd's Pie", 'Beef Wellington', 'Fish and Chips', 'Chicken Tikka Masala', 'Steak and Kidney Pie','Eton Mess',
# 'Afternoon Tea','Cornish Pasty','A Full Breakfast', 'Roasted Dinner']
# # convert the list above to tuple
# # note all the codes below are also used to access elements of a tuple
# tuple(foods)
# # pick a particular food of interest = Fish and Chips
# foods[2] # Fish and Chips is on index number 2
# # pick the last 2 meals
# foods[8:10]
# # select the first 5 menu for guest during their stay
# foods[0:5]
# # select the last food
# foods[-1]
# # check out the results of these selections
# foods[-3:-1]
# foods[1:-3]
# '''
#                         PL()
#                         st.code(c)
#                         foods = ["Shepherd's Pie", 'Beef Wellington', 'Fish and Chips', 'Chicken Tikka Masala', 'Steak and Kidney Pie','Eton Mess',
#                                 'Afternoon Tea','Cornish Pasty','A Full Breakfast', 'Roasted Dinner']
#                         Res()
#                         foods

#                         @st.experimental_memo
#                         def get_data():
#                                 return pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

#                                 tab1, tab2, tab3 = st.tabs(["Filter Data", "Raw Data", "📈 Chart"])
#                                 with tab1:
#                                         col = st.selectbox("Select column", options=["a", "b", "c"])
#                                         filter = st.slider("Filter range", -2.5, 2.5, (-2.0, 2.0), step=0.01)
#                                         filter_query = f"{filter[0]} < {col} < {filter[1]}"

#                                 with tab2:
#                                         st.dataframe(get_data().query(filter_query))

#                                 with tab3:
#                                         st.line_chart(get_data().query(filter_query))







# st.write('---')

# col1, col2 = st.columns(2)
# col1_expander = col1.expander("Beginners' Class 3: Reading Rython Data Files")
# with col1_expander:
#     # st.write('**Different Ways of Reading a File in R**')

#     # first = pd.read_table('TimeInLifeData.txt',delimiter="\t", header = None)
#     # first
#     # first.columns = ['part', 'time', 'sex', 'age', 'diff','bodytemp', 'heartrate','marriage',
#     #                 'job','family','edu','support','health']
#     # first

#     gra = st.radio(label = 'Rython', options = ['Hold','Introduction to Rython',
#                                                         'Setup Your Envoronment',
#                                                         'How to Use this App',
#                                                         'Rython: Read Data Files',
#                                                         'Rython: Read Text Files',
#                                                         'Rython: Read CSV Files',
#                                                         'Rython: Read Excel Files',
#                                                         'Rython: Read URL Data Files',
#                                                         'Rython: Supply Column Headers',
#                                                         'Conclusions',
#                                                         'Multi-Choice Questions',
#                                                         'Evaluate Your Coding Skills'])
#     st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
#     st.write('---')
#     if gra == 'Introduction to Rython':
#         st.write('''**What is Rython?**  
#         Arguably, R and Python are the two major langauges for data science. Other languages exist with specific
#         focus on certain areas example SQL for database programming however, Python and R are the most general 
#         and the most used. Companies and organizations language preferences differ, to this end, applicants always
#         look for organization with peference to the language of their choice.  
#         Rython is an attempt to bridge the knowledge or learning gap between the two langauges. We believe it is
#         possible to teach and learn both langauges simultenously and that students can become profficient 
#         in both languages at the same time. 
#         It sounds incredible, but it is possible. It is a matter of the teaching style and the willingness 
#         of the student to do extra work.  
#         Rython is simply an attempt to learn R and Python programming 
#         languages for data science together. It is the intuitive understanding and interpretation of R 
#         with respect to Python and vice versa. It is using one langauge as a link bridge to the other. 
#         It is developing the ability to decipher which programming language is best suited for particular 
#         projects in data science.''')

#     if gra == 'Setup Your Envoronment':
#         st.subheader('Setting Up Your Environment')
#         st.write('''This is a short tutotrial on how to set up your environment. By environment we mean getting all
#         softwares and packages to enable you commence and sustain a data science journey cum lifestyle. We shall be
#         downloading and installing R, and Python programming languages then we shall download and install the IDEs -
#         Rstudio for R and Jupyter Notebook for Python and we shall be looking at how to use them effectively. 
#         Also, we shall conduct a short tutorial on how to use Google Colab which is Jupyter Notebook in the 
#         cloud. We shall also look at setting up Github - a place where employers and the world at large can 
#         check and evaluate your data science projects and progress, which is very important for every data 
#         scientist. Mention shall also be made of Kaggle, - arguably the largest repository for datasets where 
#         you search for, download and use datasets and also participate in data science competitions.''')

#         st.write('**RStudio**')
#         st.write('''RStudio is the best Integrated Dvelopment Environment(IDE) for R. It is specifically made for R 
#         and it has all the functionalities to make the R coding experience smooth and enjoyable. Below is the
#         RStudio's interface, click the double arrow by the top left of the picture to enlarge.''')
#         RS = Image.open('Rs.PNG')
#         st.image(RS, use_column_width=True, caption = 'RStudio Interface')
#         st.write('''**The Coding Interface (Upper Left)**  
#         This is where you write your codes and run them. Above the interface are the usual interactive icons
#         starting with the File icon and ending with the Help icon. They corresponding with the usual uses and 
#         you will get used to then with time. For example when you click the File icon, you get a drop down, 
#         you can create a new R script, open an old one, you can save as, or save and rename a file etc. Another
#         importnat icon is the session icon it allows you to set your working directory where your R scripts and 
#         dataset files are currently located, the default directory is Documents. To run your codes, click the
#         run sub-icon to the right just immediately above the coding pane or press ctrl + enter keys. Always
#         ensure that your cursor is on the line of code you want to run or you hightlight(ctrl+A) to run
#         all the codes at once.      
#         **The Console Interface**  
#         Directly below the coding interface is the console interface. It has 3 icons: Console, Terminal and Jobs.
#         The console shows the results of the codes after running them. It is the information output 
#         point always giving you instructions and infomation about your code and about the packages.  
#         **Upper Right Interface**  
#         There are 2 columns here the first column contains the names of the datset you have read while each line of the 
#         second column contains the number of rows and columns in the datasets. This environment provides
#         major infomation about your datasets and you can view the dataset by clicking on the 
#         small light blue arrow indication before the name of the dataset or by clicking on the second column. 
#         Every dataset you read is shown on this pane. This interface also contain the History icon which 
#         shows the history of all the code you have run overtime, all you need do is to scroll upo and 
#         down to see. It also contains the Connections and Tutorial icons.  
#         **The Final Interface - Lower Right**  
#         This contains Files, Plots, Packages, Help and Viewer icons The Files icon allows for file and folder management,
#         you can open, create a folder or file, rename, delete etc. All your graphical plots are shown under the Plots
#         icon, all internal and downloaded R libraries and packages are contained in the Packages icon.''')

#         st.write(''' Packages and 3rd party libraries are also very important in R. RStudio comes with some packages.
#         However, there are many useful packages necessry for you towards becoming a data analyst. To install
#         a package you might need to download and install Rtools. The R package installation code format is:  
#         install.packages('package name').  
#         Copy this code to install the following packages in RStudio.''')

#         c = '''# Install a single package
#     install.packages('package name')
#     # Install Multiple packages or libraries at once
#     # You will find the following packages and libraries very useful
#     install.packages(c('dplyr', 'Lahman', 'tidyverse', 'nycflights13',
#     'shiny', 'ggplot2', 'caret', 'plotly', 'readxl', 'data.table', 
#     'tidyr', 'knitr', 'mlr3', 'xgboost', 'caret','lubridate'))
#     '''
#         st.code(c)

#     if gra == 'How to Use this App':
#         st.write('''**How to use this app**  
#         This app is a tutorial guide to enhance your coding and data analysis efficency for both R and Python. 
#         It helps you become a master of both data science languages together. That may sound unrealistic, but it is true.
#         We believe the best way to learn multiple langauges together is to learn one through the eye of the other.
#         This app can be used by students and employees in data science and related fields. Though the results of the codes are 
#         displayed in the app but in real world you will use the identified IDEs for data science projects
#         therefore, it is advised that the R codes are copied and run in RStudio while Python codes are copied and 
#         run on Jupyter Notebook and or in Google Colab. Always ensure that all projects you are working on
#         are committed into Github and locally in Google Drive or OneDrive. This app also serve as a revision
#         helper to help you quickly remember codes,code analysis and the results as an employee or a student.''')

#     if gra == 'Rython: Read Data Files':
#         st.subheader('Rython: Read Data Files')
#         st.write('''The Rython language provides different ways for you to read data files with ease
# 1. CSV file
# 2. Excel File
# 3. Txt files
# 4. Url and Html files''')

#         st.write(' ')
#         st.write('''**Data Files and Resources**  
#         Ensure that the data files are in the current folder where your RStudio and Jupyter Notebook files are
#         currently located. For the purppose of this study, download the datasets and data documents in this link
#         [dataset link](http://courses.washington.edu/b517/Datasets/datasets.html). Ensure to put all your download in
#         your current folder.  
#         The images of the 3 important data files are given below(excel, text and csv respectively). When you righ-click on each of the files and scroll
#         down to Properties and check Type of File you have the following extensions
# - .xlsx for excel files
# - .txt for text files
# - .csv for CSV files''')

#         original = Image.open('file images.PNG')
#         st.image(original,use_column_width=True,caption = 'Excel, Text and CSV data files') 

#         st.write('''Reading a file is an important aspect of the processes in the data pipeline, it is an attempt
#         to transform raw compiled data into machine readable forms for the supretending programming language
#         to decipher and process. To read data in Rython, the following are important.
# 1. The name of the data file
# 2. The file extension
# 3. The Rython read-data functions
# 4. The current conditions/complilation of the dataset and
# 5. The directory where the file is currently located
# 6. The analyst desire to navigate to the file or to allow machine to read the file internally
# We take an example of a dataset:''')
#         st.write('''1. Name of file: TimeInLifeData
# 2. Extension: .txt
# 3. Rython Read-data function: Python or R function
# 4. Conditions: No columns or headers yet; delimiter/separators: Yes
# 5. Directory: Current
# 6. I want the machine to read internally
# As we will see, what differentiates the programming language is the read-function to be applied.
# It is always the same data with the same name, extension, directory, conditions and compilation. 
# Let us read the above text dataset.''')


#     if gra == 'Rython: Read Text Files':
#         st.write('**Read Text Files in Rython**')
#         c ='''# Read text file with R: function 1
# text1 = read.delim('TimeInLifeData.txt', header = FALSE)
# text1'''
#         R()
#         st.code(c)

#         c  = '''# Read text file with Python: function 1
# text1 = pd.read_table('TimeInLifeData.txt',delimiter="\\t", header = None)
# text1'''
#         P()
#         # st.code(imp)
#         st.write('Import the Pandas and Numpy libraries for Python')
#         st.code(imp)
#         st.code(c)
#         st.write('''**Code Intuition and Explanation**  
#         The codes are divided into 3
# 1. The subject matter of the code: text1 - which is the name given to the data we are reading. Anytime text1 is called, the data is displayed.
# 2. The Rython read functions
# 3. The display of the data by calling to its name
# As we can see, numbers 1 and 3 are the same for for Rython codes however, there are some differences and 
# similarities in the Rython functions.  
# The read-functions are different, note that Python always instantiates the library when performing
# many function in its operations else you have pd.read(where pd is the name representing the Pandas library at the importing stage)
# even after importing the libraries. R on the other hand is always good to go after importing the necessary libraries.  
# Another difference is that Python uses None to represent no header or columns while R uses FALSE in block 
# capital letters. Both functions use read however, R already uses the delimiter with read.delim outside the backet
# therefore, the delimiter condition in the backet as contained in the Python function is no longer necessary for R.''')   
#         Res()
#         text1 = pd.read_table('TimeInLifeData.txt',delimiter="\t", header = None)
#         text1
#         st.write('---')

#         c = '''#read.delim has 2 variants in R
# colon = read.delim2('colon.txt',sep = '')
# colon'''
#         R()
#         st.code(c)
#         c = '''#Python Code
# colon = pd.read_table('colon.txt',delimiter=" ")
# colon'''
#         P()
#         st.code(c)
#         Res()
#         colon = pd.read_table('colon.txt',delimiter =" ")
#         colon
#         st.write('''Note that the delim library is internal in R it does not need to be imported. However,
#     some other codes requires importing a library. You dont need to continually import the same library in
#     both R and Python. Once you import a particular library, it is stored in the computer's memory for subsequent use.''')

#         c = '''# Import the readr library
# #how to import a library in R = library(name of library)
# library(readr)
# text2 = read_tsv('TimeInLifeData.txt',col_names = FALSE)
# text2'''
#         R()
#         st.code(c)
#         Res()
#         st.write('''Result is same as above but you have to take note of the changes in the R function -read_tsv
#         which is different from the read.delim''')

#         c = '''#Read the SalaryData.txt file 
# salary = read.delim2('SalaryData.txt',sep = '')
# salary'''
#         R()
#         st.code(c)
#         c = '''#Use the pd.read_fwf to read the SalaryData.txt file in Python
# salary = pd.read_fwf('SalaryData.txt', sep = '')
# salary'''
#         P()
#         st.write('''pd.read_fwf - fixed-width lines is one of the functions for reading text files in Python
#     Note that the body of the code('SalaryData.txt', sep = '') is same as it is in R's delim or delim2 functions.''') 
#         st.code(c)
#         Res()
#         salary = pd.read_fwf('SalaryData.txt', sep = '')
#         salary

#         c = '''#Read the tumordata.txt file with R
# tumor = read.delim2('TUMORdata.txt',sep = '')
# tumor'''
#         R()
#         st.code(c)
#         c = '''#Reading text files with pd.read_csv in python
# tumor = pd.read_csv('TUMORdata.txt', delimiter = '\\t')
# tumor'''
#         P()
#         st.code(c)
#         Res()
#         tumor = pd.read_csv('TUMORdata.txt', delimiter = '\t')
#         tumor

#         c = ''' # This navigate to the folder to pick a text file
# text3 = read.delim(file.choose(),header = FALSE)
# text3
# # OR
# text3 = read.delim(file.choose(),sep = "\\t", header = FALSE)
# text3'''
#         st.write('''Sometimes you might want to navigate to particular folder to pick the data file in R,
#         however, you have to use an R-read function that is compatible to the file type and conditions of 
#         compilation. The navigate-to-data-file code below is meant to navigate to a particular folder to pick
#         a text file.''')
#         R()
#         st.code(c)
        
#         c = '''# read BirthsKingCounty2001.txt with R
# birth = read.delim2('BirthsKingCounty2001.txt',sep = '', header = FALSE)
# birth'''
#         R()
#         st.code(c)
#         c = '''# read another file with fwf Python function
# birth = pd.read_fwf('BirthsKingCounty2001.txt', header = None)
# birth'''
#         P()
#         st.code(c)
#         birth = pd.read_fwf('BirthsKingCounty2001.txt', header = None)
#         birth

#         st.text('')
#         st.text('')
    
#     if gra == 'Rython: Read CSV Files':
#         st.write('**Read CSV Files in R**')

#         c = '''# read the FEVdata csv file with the read.table function
# FEV = read.table('FEVdata.csv',header =TRUE, sep = ',')
# FEV'''
#         R()
#         st.code(c)
#         c = '''# read the FEVdata csv file with the Pandas Library
# FEV = pd.read_csv('FEVdata.csv')
# FEV'''
#         P()
#         st.code(imp)
#         st.code(c)
#         Res()
#         FEV = pd.read_csv('FEVdata.csv')
#         FEV

#         c = '''# read the insurance csv file with the read.csv2 function
# insurance = read.csv2('insurance.csv',header =TRUE, sep = ',')
# insurance'''
#         R()
#         st.code(c)
#         c = '''#read the insurance csv file with the Pandas Library
# insurance = pd.read_csv('insurance.csv')
# insurance'''
#         P()
#         st.code(c)
#         Res()
#         insurance = pd.read_csv('insurance.csv')
#         insurance

#         c = '''# read the PBCshort csv file with the read.csv function
# PBC = read.csv('PBCshort.csv')
# PBC
# # OR
# PBC = read.csv('PBCshort.csv',header =TRUE, sep = ',')
# PBC'''
#         st.write('''Note that the csv read-function in R is almost exactly the same as it is in Python, except for the fact
#         that Python takes the library initials with the read function pd.read_csv while in R what you have
#         is read.csv.''')
#         R()
#         st.code(c)
#         c = '''# read the PBCshort csv file with the Pandas Library
# PBC = pd.read_csv('PBCshort.csv')
# PBC'''
#         P()
#         st.code(c)
#         Res()
#         PBC = pd.read_csv('PBCshort.csv')
#         PBC

#         c = '''# read the Seattle Air Polution csv file with the readr Library
# #call the readr library
# library(readr)
# polution = read.csv('Seattle Air Polution.csv')
# polution'''
#         R()
#         st.code(c)
#         st.write('''Virtually no difference between read.csv when you use the internal library and when you import
#         the readr library in R''')
#         c = '''# read the Seattle Air Polution csv file with the Pandas Library
# polution  = pd.read_csv('Seattle Air Polution.csv')
# polution '''
#         P()
#         st.code(c)
#         Res()
#         polution = pd.read_csv('Seattle Air Polution.csv')
#         polution

#         c = '''# read the wcgs csv file with the read.csv function
# wcgs = read.csv('wcgs.csv')
# wcgs'''
#         R()
#         st.code(c)
#         c = '''# read the wcgs csv file with the Pandas Library 
# wcgs = pd.read_csv('wcgs.csv')
# wcgs'''
#         P()
#         st.code(c)
#         Res()
#         wcgs = pd.read_csv('wcgs.csv')
#         wcgs

#         c = '''# Navigate to a folder for the csv file
# csv_Navigate = read.csv(file.choose())
# csv_Navigate'''
#         R()
#         st.code(c)

#     if gra == 'Rython: Read Excel Files':
#         st.write('**Read Excel Files**')
#         st.write('''For you to read excel files successfuly in Python, you MUST must install the openpyxl library
#         without which pandas wont be able to read you excel files. It is an internal library, you dont need to import it
#         while attempting to read an excel file. For R, you can install and import any of the following: readxl,
#         xlsx, openxlsx, and XLConnect. For this study, we use readxl.''')
#         c = '''# load or call the readxl library
# # other libraries that can read excel files in R include: xlsx, openxlsx, XLConnect
# library(readxl)'''
#         st.code(c)

#         c = '''# Naviagte to the excel file in any folder
# excel_Naviagte = read_excel(file.choose())
# excel_Naviagte'''
#         R()
#         st.code(c)

#         c = '''# Read file_example excel file with readxl
# excel1 = read_excel('file_example.xlsx')
# excel1'''
#         R()
#         st.code(c)
#         st.write('''By default and without specification the read excel function in R or Python reads the
#         first sheet''')
#         c = '''# Read file_example excel file with Pandas
# excel1 = pd.read_excel('file_example.xlsx')
# excel1'''
#         P()
#         st.code(imp)
#         st.code(c)
#         Res()
#         excel1 = pd.read_excel('file_example.xlsx')
#         excel1

#         c = '''# Read SuperStore excel file with readxl
# store = read_excel('SuperStoreUS_2015.xlsx', sheet = 'Orders')
# store'''
#         R()
#         st.code(c)
#         st.write('''Only a slight difference exist beween the R and the Python codes - Python always carries the initials
#     of its library everwhere - pd.read_excel - when you remove the pd, you are close to completing the R code.''')
#         c = '''# Read SuperStore excel file with  Pandas
# store = pd.read_excel('SuperStoreUS_2015.xlsx', sheet_name = 'Orders')
# store'''
#         P()
#         st.code(c)
#         Res()
#         store = pd.read_excel('SuperStoreUS_2015.xlsx', sheet_name = 'Orders')
#         store

#         c = '''# Read the Stabucks excel file with readxl
# store1 = read_excel('Starbucks Dummy Data.xlsx', sheet = 1)
# store1'''
#         R()
#         st.code(c)
#         c = '''# Read the Stabucks excel file with Pandas
# store1 = pd.read_excel('Starbucks Dummy Data.xlsx', sheet_name = 0)
# store1'''
#         P()
#         st.code(c)
#         Res()
#         store1 = pd.read_excel('Starbucks Dummy Data.xlsx', sheet_name = 0)
#         store1

#         c = '''# Read the Customer Analysis excel file with readxl
# retail = read_excel('CUSTOMER ANALYSIS.xlsx', sheet = 'STORE')
# retail'''
#         R()
#         st.code(c)
#         c = '''# Read the Customer Analysis excel file Pandas
# retail = pd.read_excel('CUSTOMER ANALYSIS.xlsx', sheet = 'STORE')
# retail'''
#         P()
#         st.code(c)
#         Res()
#         retail = pd.read_excel('CUSTOMER ANALYSIS.xlsx', sheet_name = 'STORE')
#         retail


#     if gra == 'Rython: Read URL Data Files':
#         st.write('**Read File from the Internet in R**')
#         st.write('''This depends on the type of file, you can use any of the functions that reads files above
#     read.csv if the file is csv, read_excel if the file is excel, read.delim if the file is txt''')

#         st.write('**R Code**')
#         c = '''# read from internet: format
# # read a csv data online
# csvURL = read.csv('URL.csv')
# csvURL
# # read an excel data online
# excelURL = read_excel('URL.xlsx')
# excelURL
# # read a txt data online
# txtURL = read.delim('URL.txt')
# txtURL
# # read a txt data online
# txtURL = read.delim2('URL.txt')
# txtURL
# '''
#         st.code(c)
        
#         st.write('')

#     if gra == 'Rython: Supply Column Headers':   
#         st.write('**Supply Column Headers**')
#         st.write('''As we have seen, there are some files uploaded without columns headers and one of the first thing
#     you have to do is to supply headers to make the dataset more readable and readers friendly. In Python, you can
#     supply the names with the read function or supply them after reading the file. Let us use the TimeInLifeData.txt
#     dataset as an example here''')
    
#         c = '''# First, read the dataset
# time = read.delim2('TimeInLifeData.txt',sep = '')
# time
# # Second supply headers
# # Method 1
# colnames(time) = c('part', 'time', 'sex', 'age', 'diff',
#                     'bodytemp', 'heartrate','marriage',
#                     'job','family','edu','support','health')

# # Method 2
# # The difference between the first and second method is the function head: names and colnames
# names(time) = c('part1', 'time2', 'sex', 'age', 'diff',
#                   'bodytemp', 'heartrate','marriage',
#                   'job','family','edu','support','health')
# # Check to see if the headers are effected
# time'''
#         R()
#         st.code(c)
#         c = '''# First supply the headers
# Life = ['part1', 'time2', 'sex', 'age', 'diff',
#                   'bodytemp', 'heartrate','marriage',
#                   'job','family','edu','support','health']
# # Read data with Python and supply the columns with the read function
# time = pd.read_csv('TimeInLifeData.txt',delimiter="\\t", names = Life)
# time'''
#         P()
#         st.code(c)
#         Res()
#         Life = ['part1', 'time2', 'sex', 'age', 'diff',
#                   'bodytemp', 'heartrate','marriage',
#                   'job','family','edu','support','health']
#         time = pd.read_csv('TimeInLifeData.txt',delimiter="\t", names = Life)
#         time

#         st.write('''**Supply Columns Headers after Reading Data in Python**''')
#         c = '''# first Read data with Python
# time = pd.read_csv('TimeInLifeData.txt',delimiter="\\t")
# time.head()
# '''
#         P()
#         st.code(c)
#         Res()
#         time = pd.read_csv('TimeInLifeData.txt',delimiter="\t")
#         st.write(time.head())

#         c = '''# Second, supply the headers into the data with the code below
# time.columns =['part1', 'time2', 'sex', 'age', 'diff',
#                   'bodytemp', 'heartrate','marriage',
#                   'job','family','edu','support','health']                 
# # View the dataset again
# time.head()
# '''
#         P()
#         st.code(c)
#         Res()
#         st.caption('View the dataset again')
#         time.columns =['part1', 'time2', 'sex', 'age', 'diff',
#                     'bodytemp', 'heartrate','marriage',
#                     'job','family','edu','support','health']
#         st.write(time.head())
#         st.write(' ')

#     if gra == 'Conclusions':
#         st.write('''As we round off on reading data files in Rython note the following:
# 1. Sep is interchangeable with delimiter in python
# 2. ' ' and " " single and double quotes are the same for both R and Python
# 3. You need to see your raw data first before you read them, this is to enable you understand the approptiate functions to use
# 4. You need to try as much as possible to know the 3 variants of reading text files for both programmes because you might need to do trial and error sometimes
# 5. The data documentation is always very important to enable you fill the blank spaces and to supply the columns where columns are absent from the datasets as it is presented
# 6. Apart from the text files functions the difference between reading data files in R and and Pythons are minimal. Python is in the habit of carrying initials everywhere whereas R does not mind you calling it by its name directly without any title.
#         To this end, Python is like an African chief who is very title conscious. You must put the title before his name if you wish to get a response   
# 7. If your excel data file is below the 2010 version you might need to 'save as' the current version you have in your system to make it readable.
# 8. = (equality sign) and <- (back arrow) can be used interchangeably in R''')
#     st.write('')
    
#     if gra == 'Multi-Choice Questions':
#         st.write('Mutli-Choice Quiz Question for Reading Data Files in RPython')
#         st.write('**Instruction: Pls pick one option at a time and wait for the result**')
#         st.write('---')
#         st.write('**Question 1**')
#         st.write('**Mention the Programming Languages for Data Science**')

#         quest = st.radio(label = 'Programming Languages', options = ['Hold','A. Python, R, Julia, SQL',
#                                                     'B. MATLAB, Java, SAS, Scala',
#                                                     'C. C/C++, JavaScript, Swift, Go',
#                                                     'D. All of the above',
#                                                     'E. A and B above'])
#         # st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
#         if quest == 'Hold':
#             st.write('')

#         elif quest == 'D. All of the above':
#             st.success('You are correct!!')
#             st.snow()
#             st.balloons()
#             st.caption('''There are various programming languages for data science some serve different purposes.
#             SQL for example is a database language.''')
#         else:
#             st.error('Your answer is partially correct, there are other programming languages for Data Science')
#         st.caption('''[Read this short article to gain more insights:](https://www.datacamp.com/blog/top-programming-languages-for-data-scientists-in-2022)''')
#         st.write('---')

#         st.write('**Which of the follwing statements is True**')
#         quest = st.radio(label = 'Data Science Misconception', options = ['Hold',
#                                                     'A. Data scientists MUST have computer science degree',
#                                                     'B. You cannot learn data science until you have a university degree',
#                                                     'C. Statistics and Linear Algebra are crucial to data science',
#                                                     'D. Data science is only necessry for business related endeavours',
#                                                     'E. Data Science is multi-discplinary',
#                                                     'F. The Data Analyst and Data Scientists are the most significant roles in Data Science',
#                                                     'G. Building predictive models is the most important process in data science',
#                                                     'H. All of the above are true',
#                                                     'I.- C AND E are true',
#                                                     'J. Only in the university can you learn data science, once you are out of the university you cannot become a good data scientist',
#                                                     'K. A, B, F and J are true'])
#         # st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
#         if quest == 'Hold':
#             st.write('')

#         elif quest == 'I.- C AND E are true':
#             st.success('You are correct!!')
#             st.snow()
#             st.balloons()
#             st.caption('''Data Science is multi-discplinary, machine learning are extensively used in: medicine, music
#             engineering, economics, e-commerce etc.''')
#             st.caption('''[Read about how big companies are using machine leraning to solve daily problems here:](https://www.tensorflow.org/about/case-studies?filter=all)''')
#         else:
#             st.error('This is one of the misconceptions about data science: do a google search on: data science misconceptions')
#             st.caption('''[Read about some of the major data science misconceptions or myths here:](https://www.analyticsvidhya.com/blog/2020/09/11-data-science-myths/)''')

#     if gra == 'Evaluate Your Coding Skills':
#         load = st.text_input('Type your code here')
#         if load:
#                 df = pd.read_csv(load)
#                 df
        
        
        
        
        
#         st.write('---')
       
# col1_expander = col2.expander("Beginners' Class 4: Datasets' Information")
# with col1_expander:
#     st.subheader("Gain Access to Datasets' Information")
#     st.write('''**Introduction**
    
# Our main objective here is to present the infomation inherent in a dataset as they currently are. It is like performing a
# KYC(know your client) on individual clients. The information gathered go a long way to help our undestanding of the dataset
# and its adequacy for the task which it is meant for.''')

#     views = st.radio(label = "Select a topic", options = ['Hold','General Dataset Info','Column Based Information',
#                                                             'Components Information',
#                                                             'Columns Pairwise Information'])
#     st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
#     st.markdown('----')


#     if views == 'General Dataset Info':
#         # st.write('''In this section, we attempt to gain valuable insights into the dataset by examining
#         # the general information as currently contained in the dataset - the raw information that came through 
#         # data pipeline''')
#         st.write('''The general dataset info is divided into two: Structural Composition, and the Statistical Composition''')
        
#         st.write('---')
#         vw = st.radio(label = "Info Parts", options = ['Hold','Structural Composition',
#                                                         'Statistical Composition',
#                                                         'Preliminary Report'])
        
#         st.write('---')
#         if vw == 'Structural Composition':
#                 st.write('''Dataset's structural composition inculdes information on:  dataset shape(number of rows and columns), 
#                 the columns names and the data type of each column. First, we have display the dataset.''')
#                 st.write(' ')
#                 st.write('**Read and Display Dataset**')
#                 st.write('First, we need to read that dataset both in R and in Python')
#                 R()
#                 c = '''# Read the MRI.txt dataset with R
# mri = read.delim2('MRI.txt',sep = '')
# # Display the dataset 1
# mri
# # Display the dataset on the coding interface
# View(mri)'''

#                 st.code(c)
#                 st.write('Import the Pandas and Numpy libraries for Python')
#                 st.code(imp)
#                 c = '''# Read the MRI.txt dataset with Pandas
# mri = pd.read_fwf('MRI.txt')
# # Display the dataset 1
# mri
# # Display the dataset 2
# print(mri)'''
#                 P()
#                 st.code(c)
#                 Res()
#                 mri = pd.read_fwf('MRI.txt')
#                 mri
        
#                 st.write('**Dataset Display**')
#                 c = '''# Display the first and the last 6 rows using R
# head(mri)
# tail(mri)
# '''
#                 R()
#                 st.code(c)

#                 c = '''# Display the first and the last 5 rows using Pandas in Python
# mri.head()
# mri.tail()
# '''
#                 P()
#                 st.code(c)
#                 Res()
#                 st.write('First 5 Rows')
#                 st.write(mri.head())
#                 st.write('Last 5 Rows')
#                 st.write(mri.tail())
#                 st.write('''Note that using the head and tail Python displays 5 rows each while R displays 6 rows each.
#                 The question is, from the above codes, what is common in code formation? How does R use the bracket differently from Python?
#                 It seems that R puts the functions first before the dataset, with the dataset's name within the barckets. With Python,
#                 dataset's name comes first. Is this a trend or one-off? We need to look at more codes to see the coding trends between the 2 languages.  
#                 Supposing I want to see more than 5 or 6 rows at the head or tail of the dataset?''')

#                 c = '''# Display the first and the last 10 rows using R
# head(mri, 10)
# tail(mri, 10)'''
#                 R()
#                 st.code(c)

#                 c = '''# Display the first and the last 10 rows using Pandas in Python
# mri.head(10)
# mri.tail(10)
# '''
#                 P()
#                 st.code(c)
#                 Res()
#                 st.write('First 10 Rows')
#                 st.write(mri.head(10))
#                 st.write('Last 10 Rows')
#                 st.write(mri.tail(10))

#                 st.write('''Notice how the 2 languages play upon the words that makeup the codes. Notice the use of 
#                 comma , in R and dot . in Python''')
                
#                 # rp = ["R's Head-Rows", "Python's Head-Rows", "R's Tail-Rows", "Python's Tail-Rows" ]
#                 # a = st.selectbox('Select the Program', rp)
#                 # b = st.number_input('Choose the number of rows you want to display', min_value = 1)
#                 # st.write('You want to display',b,'rows of', a)

#                 st.write('')
#                 st.write('**Check The Shape of Dataset**')
#                 st.write('We want to see the number of rows and columns in the dataset')

#                 c = ''' # Data shape in R
# dim(mri)'''
#                 R()
#                 st.code(c)

#                 c = ''' # Data shape using Pandas for Python
# mri.shape'''
#                 P()
#                 st.code(c)
#                 Res()
#                 st.text(mri.shape)
#                 st.write('Currently before data cleaning the dataset has:',len(mri),'rows', 'and', len(mri.columns),'columns.')
#                 st.write('What if I want to find the number of rows without the columns and vice versa?')

#                 c = ''' # Number of rows and columns done separately in R

# # number of rows 1
# nrow(mri)
# # number of rows 2
# count(mri)

# # number of columns
# ncol(mri)'''
#                 R()
#                 st.code(c)

#                 c = ''' # Number of rows and columns done separately using Pandas for Python

# # number of rows 1
# mri.shape[0]
# # number of rows 2
# len(mri)

# # number of columns 1
# len(mri.columns)
# # number of columns 2
# mri.shape[1]'''
#                 P()
#                 st.code(c)
#                 Res()
#                 st.caption('number of rows:')
#                 st.text(mri.shape[0])
#                 st.caption('number of columns:')
#                 st.text(mri.shape[1])
#                 # st.text(len(mri))
#                 # st.text(mri.count())
#                 st.write('Suppose you want to include the number of rows and columns in a report, how do you go about that?')

#                 c = '''# Introduction to the print function in R
# print(paste("Number of columns in the MRI dataset is:",ncol(mri),
#             "While the number of rows is:",nrow(mri)))
# # OR
# print(paste("Number of columns and rows in the MRI dataset are:",ncol(mri),'and',
#             nrow(mri),'respectively'))'''
#                 R()
#                 st.code(c)

#                 c = '''# Introduction to the print function in Python
# print("Number of columns in the MRI dataset is:",mri.shape[1],
#             "While the number of rows is:",len(mri))
# # OR
# print("Number of columns and rows in the MRI dataset are:",mri.shape[1],'and',len(mri),
#         'respectively')'''
#                 P()
#                 st.code(c)
#                 Res()
#                 st.write("Number of columns in the MRI dataset is:",mri.shape[1],
#                 "While the number of rows is:",len(mri))
                
#                 st.write("Number of columns and rows in the MRI dataset are:",mri.shape[1],'and',len(mri),
#                         'respectively')
#                 st.write('''Notice the difference between the R and Python print functions, Infact, when you initiate a one argument
#                 print function both R and Python print codes are the same''')

#                 c = '''# When R and Python print function are the same
# print('My names are: Boris Obama Biden')'''
#                 R()
#                 P()
#                 st.code(c)
#                 Res()
#                 st.write('My names are: Boris Obama Biden')
#                 st.write('''The difference comes when you want to add another function or argument within the print function.
#                 Suppose I want to add my street number as a function''')

#                 c = '''# add another function to the above introduction of myself
# print(paste('My names are: Boris Obama Biden, I live at number',ncol(mri),
#       'Beautiful Street New York'))'''
#                 R()
#                 st.code(c)

#                 c = '''# add another function to the above introduction of myself
# print('My names are: Boris Obama Biden, I live at number',ncol(mri),
#       'Beautiful Street New York')'''

#                 P()
#                 st.code(c)
#                 Res()
#                 st.write('My names are: Boris Obama Biden, I live at number',mri.shape[1],
#                         'Beautiful Street New York')
#                 st.write('''When you add another argument to the function Python remains same but R changes with the addition of the paste function
#                 within the print function, then you have to adjust the barckets to accomodate the new argument.  
#                 Lets get back to accessing data info.''')
#                 st.write('')
#                 st.write('**List the Column Names**')
#                 st.write('Here, we want to display the names of the columns in the datasets.')

#                 c = '''# List the column names in R
# names(mri)'''
#                 R()
#                 st.code(c)

#                 c = '''# List the column names in Python
# mri.columns'''
#                 P()
#                 st.code(c)
#                 Res()
#                 st.text(mri.columns)
        
#                 st.write('')
#                 st.write('**Columns Data Types**')
#                 st.write('What data types are the columns made of? Data types naming is different in both languages.')

#                 c = '''# Columns datatypes in R

# # first activate or call the tidyverse library
# library(tidyverse)

# # Columns datatypes 1
# sapply(mri, class)

# # Columns datatypes 2
# sapply(mri, typeof)

# '''
#                 R()
#                 st.code(c)

#                 st.caption('Remember to always copy and run the R code in R studio and the Python codes in Jupyter notebook and or Google Colab')
                
#                 c = '''# Columns datatypes in R
# mri.dtypes'''
#                 P()
#                 st.code(c)
#                 Res()
#                 st.text(mri.dtypes)
#                 st.caption('''The above result is a Python result using the Pandas Library. In R, there are 2 data types:
#                 Integer (representing all numeric columns - int64 and float64 in Python) and Character(representing the object or category data type in Python)''')


#         # for i in mri.columns:
#         #         d2 = mri[i].unique()[:10]
#         #         a = (i,':',d2)
#         #         st.text(a)


#                 st.text('')
#                 st.write('**Generate General Information Summary**')

#                 st.caption('General Info Summary for R')
#                 c = ''' # General Info Summary in R

# # General Info Summary 1
# str(mri)

# # General Info Summary 2
# glimpse(mri)

# # General Info Summary 3
# as_tibble(mri)'''
#                 R()
#                 st.code(c)

#                 buffer = io.StringIO()
#                 mri.info(buf = buffer)
#                 abio = buffer.getvalue()
#                 st.caption('General Info Summary for Python')
#                 P()
#                 c = 'mri.info()'
#                 st.code(c)
#                 Res()
#                 st.text(abio)

#                 st.caption('''It must be stated that Python has a better and more concise result with respect to general
#                 information summary. As stated earlier, In R, there are 2 data types:
#                 Integer (representing all numeric columns - int64 and float64 in Python) and 
#                 Character(representing the object or category data type in Python)''')
#                 T()

#                 st.text('')

#         if vw == 'Statistical Composition':
#                 mri = pd.read_fwf('MRI.txt')

#                 st.write('**Descriptive Statistical Information Report**')
#                 st.caption('''Here we display the result for R and then the result for Python 
#                 because the layouts of both results are radically different. R takes each column at a time while Python
#                 put all the columns togther.''')
#                 c = '''# Statistical and Data Info Report in R
# summary(mri)'''
#                 R()
#                 st.code(c)
#                 Res()
                
#                 mri.columns = ['ptid', 'mridate', 'age', 'male', 'race', 'weight', 'height,packyrs',
#                 'yrsquit, alcoh, physact', 'chf', 'chd', 'stroke', 'diabet', 'genhlth',
#                 'ldl', 'alb', 'crt', 'plt', 'sbp', 'aai', 'fev', 'dsst', 'atrophy',
#                 'whgrd', 'numinf', 'volinf', 'obstime', 'death']
    
#                 mri[['height', 'packyrs']]= mri['height,packyrs'].str.split(expand=True)#.astype(np.number)
#                 mri['packyrs'] = mri['packyrs']. replace('NA',0)
#                 mri[['yrsquit', 'alcoh', 'physact']]= mri['yrsquit, alcoh, physact'].str.split(expand=True).astype(np.number)
#                 mri[['height', 'packyrs']] = mri[['height', 'packyrs']].astype(float)
#                 mri = mri.drop(['height,packyrs','yrsquit, alcoh, physact'], axis = 1)

#                 nume = mri.select_dtypes(np.number)
#                 cate = mri.select_dtypes(object)
#                 flo = mri.select_dtypes(float)
#                 inte = mri.select_dtypes(int)
#                 date = mri.select_dtypes('datetime64[ns]')

#                 for f in nume:
#                         st.text('')
#                         st.write('Column_Name:',f)

#                         domy = pd.DataFrame({'Min.':[mri[f].min()],
#                                                 '1st Qu.':[mri[f].quantile(0.25)],
#                                                 'Median.':[mri[f].median()],
#                                                 'Mean.':[round(mri[f].mean(),2)],
#                                                 '3rd Qu.':[mri[f].quantile(0.75)],
#                                                 'Max.':[mri[f].max()],
#                                                 'Std':[round(mri[f].std(),2)],
#                                                 "Na's":[mri[f].isna().sum()]})
#                         domy = domy.T
#                         domy = domy.rename(columns={0:' '})
#                         st.text(domy)

#                 for f in cate:
#                         st.text('')
#                         st.write('Column_Name:',f)

#                         domy = pd.DataFrame({'Length.':[mri[f].count()],
#                                         'Class.':['Character'],
#                                         'Mode.':['Character'],
#                                         "Na's.":[mri[f].isna().sum()]})
#                         domy = domy.T
#                         domy = domy.rename(columns={0:' '})
#                         st.text(domy)

#                 c = '''# Statistical and Data Info Report in Python
# mri.describe()'''
#                 st.text('')
#                 P()
#                 st.code(c)
#                 Res()
#                 st.write(mri.describe())

#                 st.write('''Find the descriptive statistical summary of selected columns instead of the
#                 whole dataset.''')
#                 c = '''# summary of one column in R
# summary(mri$age)
# # or
# summary(mri[('age')])

# # summary of two or more columns
# summary(mri[c('age','race','weight')])
# # or
# apply(mri[c('age','race','weight')], MARGIN = 2, FUN = summary)
# lapply(mri[c('age','race','weight')], function(x) summary(x))
# sapply(mri[c('age','race','weight')], function(x) summary(x))

# # Selected columns with selected descriptive statistics
# sapply(car[c('mpg', 'cyl', 'drat')], function(x) 
#   c(MIN=min(x), AVERAGE = mean(x), MEDIAN = median(x), MAX = max(x), 
#     quantile(x)))
# # or
# # this code selects the quantiles the above output all the quantiles
# sapply(car[c('mpg', 'cyl', 'drat')], function(x) 
#   c(MIN=min(x), AVERAGE = mean(x), MEDIAN = median(x), MAX = max(x), 
#     quantile(x, probs = c(0.25,0.5,0.75))))
# '''
#                 R()
#                 st.code(c)
#                 Res()
#                 st.text('''> summary(mri[('age')])
#       age       
#  Min.   :65.00  
#  1st Qu.:71.00  
#  Median :74.00  
#  Mean   :74.57  
#  3rd Qu.:78.00  
#  Max.   :99.00''')
#                 st.text('''> summary(mri[c('age','race','weight')])
#       age             race          weight         
#  Min.   :65.00   Min.   :1.000   Length:735        
#  1st Qu.:71.00   1st Qu.:1.000   Class :character  
#  Median :74.00   Median :1.000   Mode  :character  
#  Mean   :74.57   Mean   :1.318                     
#  3rd Qu.:78.00   3rd Qu.:1.000                     
#  Max.   :99.00   Max.   :4.000''')
#                 st.text('''sapply(car[c('mpg', 'cyl', 'drat')], function(x) 
# +   c(MIN=min(x), AVERAGE = mean(x), MEDIAN = median(x), MAX = max(x), 
# +     quantile(x)))
#              mpg    cyl     drat
# MIN     10.40000 4.0000 2.760000
# AVERAGE 20.09062 6.1875 3.596563
# MEDIAN  19.20000 6.0000 3.695000
# MAX     33.90000 8.0000 4.930000
# 0%      10.40000 4.0000 2.760000
# 25%     15.42500 4.0000 3.080000
# 50%     19.20000 6.0000 3.695000
# 75%     22.80000 8.0000 3.920000
# 100%    33.90000 8.0000 4.930000''')

#                 c = '''# Descriptive Statistics for one or selected columns in Python
# # one column
# mri['race'].describe()
# # or
# mri.race.describe()

# # two or more columns
# mri[['age','race','weight']].describe()
# mri[['age','race','weight']].quantile([0.25,0.75,0.5])

# # Selected columns with selected descriptive statistics
# mri[['age','race','weight']].agg(['count','sum','mean','median','quantile']
# '''                
                
                
#                 st.caption('Note that R used summary as the function head-word while Python used describe')

#                 st.write('''We are noticing a growing trend that differentiate Python and R coding. It seems that
#                 R encloses the name of the dataset in a bracket with the function on the left outside of the barcket,
#                 while python uses the dot to separate the function and the name of the dataset. Python always call the name
#                 of the dataset first while R calls the function first. We need more coding evidences to asertain whether this
#                 is always true.''')
                
#                 P()
#                 st.code(c)
#                 Res()
#                 st.write(mri['race'].describe())
#                 #st.text(mri.race.describe())
#                 st.write(mri[['age','race','weight']].describe())
#                 st.write(mri[['age','race','weight']].quantile([0.25,0.75,0.5]))
#                 onC = mri[['age','race','weight']].agg(['count','sum','mean','median','quantile'])
#                 st.write(onC)
#                 T()

# #                 c = '''# MRI dataset preliminary general information report in Python
# # print("MRI - Magnetic Resonance Imaging is a a government sponsored cohort study of 
# # adult aged 65 years and older was conducted to observe the incidence of cardiovascular 
# # diseases (especially heart attacks and cognitive heart failures) and cerebrovascular 
# # diseases (especially strokes) in elderly over 11-year period and to relate the incidence 
# # of those diseases to various risk factors measured in population on a regular basis. For more, proceed to... 
# # [MRI datasets documentation link](http://courses.washington.edu/b517/Datasets/datasets.html). The dataset has a total of:")
# # print(mri.shape[0], 'rows','and',mri.shape[1],'columns. There are',
# # len(mri.select_dtypes(np.number).columns), 'numerical columns out of which',
# # len(mri.select_dtypes(float).columns), 'are float data type',
# # len(mri.select_dtypes(int).columns),'are integer data type', 
# # len(mri.select_dtypes(object).columns),'are object or categorical data types', 'while',
# # len(mri.select_dtypes('datetime64[ns]').columns), 'are date data types.')
# # print("However, from the documentation we noticed some discrepancies in data types. the column: 'mriate' is a date
# # data type. We also noticed that many of the columns like (race, male, packyrs, chf, chd etc.) 
# # can be mapped into categorical data types for future analysis. Find below the Pythonic generated
# # structural and statistical composition of the dataset:")'''
# #                 P()
# #                 st.code(c)

#         if vw == 'Preliminary Report':
#                 mri = pd.read_csv('MRIdata.csv')

#                 buffer = io.StringIO()
#                 mri.info(buf = buffer)
#                 abio = buffer.getvalue()

#                 st.write('**Preliminary General Information Report**')
#                 st.write('This report is what we have at present, it is subject to modification during data cleaning.')
#                 Re()
#                 st.write('''MRI - Magnetic Resonance Imaging is a a government sponsored cohort study of 
#                 adult aged 65 years and older was conducted to observe the incidence of cardiovascular 
#                 diseases (especially heart attacks and cognitive heart failures) and cerebrovascular 
#                 diseases (especially strokes) in elderly over 11-year period and to relate the incidence 
#                 of those diseases to various risk factors measured in population on a regular basis. For more, proceed to... 
#                 [MRI dataset's documentation link](http://courses.washington.edu/b517/Datasets/datasets.html).  
#                 The dataset has a total of:''',mri.shape[0], 'rows','and',mri.shape[1],'columns. There are',
#                 len(mri.select_dtypes(np.number).columns), 'numerical columns out of which',
#                 len(mri.select_dtypes(float).columns), 'are float data type',
#                 len(mri.select_dtypes(int).columns),'are integer data type', 
#                 len(mri.select_dtypes(object).columns),'are object or categorical data types', 'while',
#                 len(mri.select_dtypes('datetime64[ns]').columns), 'are date data types.','''However, from
#                 the documentation we noticed some discrepancies in data types. the column: 'mriate' is a date
#                 data type. We also noticed that many of the columns like (race, male, packyrs, chf, chd etc.) 
#                 can be mapped into categorical data types for future analysis. Find below the Pythonic generated
#                 structural and statistical composition of the dataset:''')
#                 st.text(abio)
#                 st.write(mri.describe())
#                 st.write('The above report is generated using Python find the R report below. Copy and paste and run in RStudio')

#                 c = '''# Preliminary general information Report template in R

# print(paste("What the dataset is all about.[dataset documentation link](the url)"))
# "The dataset has a total of:",nrow(mri),"rows and",ncol(mri),"columns. There are a total of:",
# ncol(mri %>% select_if(is.numeric)),"numeric columns and",
# ncol(mri %>% select_if(negate(is.numeric))),"non numeric columns"))'''
#                 R()
#                 st.code(c)
                
#                 c = '''# MRI dataset preliminary general information report in R

# print(paste("MRI - Magnetic Resonance Imaging is a a government sponsored cohort study of 
# adult aged 65 years and older was conducted to observe the incidence of cardiovascular 
# diseases (especially heart attacks and cognitive heart failures) and cerebrovascular 
# diseases (especially strokes) in elderly over 11-year period and to relate the incidence 
# of those diseases to various risk factors measured in population on a regular basis. For more, proceed to... 
# [MRI dataset's documentation link](http://courses.washington.edu/b517/Datasets/datasets.html)
# The dataset has a total of:",nrow(mri),"rows and",ncol(mri),"columns. There are a total of:",
# ncol(mri %>% select_if(is.numeric)),"numeric columns and",
# ncol(mri %>% select_if(negate(is.numeric))),"non numeric columns. However,
# we noticed that the non numeric columns are actually numeric columns but they
# were described as non-numeric because of the incedences of of NA (null values) within 
# the columns.  Find below the R generated structural and statistical composition of the dataset:"))
# str(mri)
# summary(mri)'''
#                 R()
#                 st.code(c)


#     if views == 'Column Based Information':
#         st.write('**Column Based Information**')
#         st.write('''Our objective here is to help the students gain access to the information contained 
#         in the columns of a dataset. Before you proceed to data warngling it is important that you have access to all the 
#         information necessary for you to work with especially those within the columns.''')
#         st.write('-----')


#         colv = st.radio(label = "Select a topic", options = ['Hold','Null Values',
#                                                             'Unique Values Counts',
#                                                             'Columns Pairwise Information'])
#         st.write('-----')
#         if colv == 'Null Values':
#             st.write('**Null Values in each Columns of the Dataset**')
#             st.write('''Null values are also referred to as missing values. They are missing by reason of omission
#             or non-availability. Theye are usually carried over from the data gathering stage.
#             We are interested in gaining access to the null or missing data in this section.
#             It is an important part of the data cleaning process. Null value treatment will come later
#             during the data cleaning stage.''')
            
#             c = '''# Read the Iowa Housing Datatset in R
# iowa = read.csv('Iowa.csv')'''
#             R()
#             st.code(c)

#             c = '''# Read the Iowa Housing Datatset in Python
# iowa = pd.read_csv('Iowa.csv')'''

#             P()
#             st.code(imp)
#             st.code(c)
#             iowa = pd.read_csv('Iowa.csv')
#             st.caption('Read the Iowa Housing Dataset for this purpose')
#             iowa
            
#             st.caption('Display the sum of all null values in every column')
           

#             c = '''# sum of missing values in all columns using R
#         # Use any of these codes
# # Sum of missing values 1
# sapply(iowa, function(x) sum(is.na(x)))
# # Sum of missing values 2
# lapply(iowa, function(x) sum(is.na(x)))
# # Sum of missing values 3
# mapply(function(x) sum(is.na(x)), iowa)
# # Sum of missing values 4
# colSums(is.na(iowa))
# # Sum of missing values 5
#         # MARGIN = 1: operation across the rows,
#         # MARGIN = 2: operation across the columns,
# apply(X = is.na(iowa), MARGIN = 2, FUN = sum)
# # Sum of missing values 6
# apply(iowa, MARGIN = 2, function(x) FUN = sum(is.na(x)))
# # you dont need to include: MARGIN and FUN as long as the arguments are represented
# apply(iowa, 2, function(x) sum(is.na(x)))'''
#             R()
#             st.code(c)
#             fo()
#             st.error('''The apply function takes 3 input arguments:- apply(X, MARGIN, FUN)  
#             X:- an array or matrix   
#             MARGIN decides where the operation will take place on the columns or rows?   
#             MARGIN = 1: operation across the rows  
#             MARGIN = 2: operation across the columns  
#             FUN = operational functions to be applied: sum, mean, median, max, min and users-defined functions     
#             -----  
#             sapply and lapply takes 2 input arguments:- sapply/lapply(X, FUN)  
#             X:- A vector or an object  
#             FUN:- function applied to each elements of x  
#             for the mapply function the reverse is the case:- mapply(FUN, X).  
#             it looks at the function to be applied to each element of x before considering X  
#             -----  
#             sapply and lapply in R are the same, they take the same input however, 
#             lapply returns the output as a list while sapply returns the output as a vector.  
#             apply is different from sapply and lapply based on input arguments  
#             apply takes an array or matrix  
#             sapply and lapply take a vector or nan onject  
#             Also in apply you need to specify the MARGIN: row or column. However,
#             sapply, lapply or mapply automatically performs the operation on the column(s)''')
#             Teach()
#             st.caption('''*The teacher should at this point seize the opportunity to introduce students to the following
#             functions: apply, sapply, lapply and mapply, with many examples and situations where they can be used.
#             The functions are general and they can be applied generally in R, especially for statistical
#             operations.*''')

#             c = '''# sum of missing values in all columns using Python
# # Sum of missing values 1
# iowa.isnull().sum()
# # Sum of missing values 2
# iowa.isna().sum()'''
#             P()
#             st.code(c)
#             Res()
#             st.write(iowa.isnull().sum())
            
#             c = '''# Mean and percentage of null values in each column in R
# # Mean of null values in each column
# colMeans(is.na(iowa))
# # Multiply the above code by 100 to get Percentage of null values
# colMeans(is.na(iowa))*100
# # Round to 2 decimal places
# round(colMeans(is.na(iowa))*100, 2)
# '''
#             R()
#             st.code(c)


#             c = '''# Mean and percentage of null values in each column in Python
# # Mean of null values in each column
# iowa.isna().mean()
# # Multiply the above code by 100 to get Percentage of null values
# iowa.isna().mean()*100
# # Round to 2 decimal places
# round(iowa.isna().mean(),2)*100
# '''
#             P()
#             st.code(c)
#             Res()
#             (round(iowa.isna().mean(),2)*100)

#             c = '''# Null values greater than 0 in R
# nan = colSums(is.na(iowa))
# nan = nan[nan > 0]
# nan

# # Percentage null values greater than 0 to 2 decimal places in R 1
# # Notice that colSums changed to colMeans
# nan = colMeans(is.na(iowa))
# nan = nan[nan > 0]*100
# round(nan, 2)

# # Percentage null values greater than 0 to 2 decimal places in R 2
# nan = apply(X = is.na(iowa), MARGIN = 2, FUN = mean)
# nan = nan[nan > 0]*100
# round(nan, 2)
# '''
#             R()
#             st.code(c)

#             c = '''# Null values greater than 0 in Python
# nan = iowa.isna().sum()
# nan[(nan)!=0]

# # Percentage null values greater than 0 to 2 decimal places in Python
# nan = round(iowa.isna().mean(),2)*100
# nan[(nan)!=0]
# '''
#             P()
#             st.code(c)
#             Res()
#             nan = round(iowa.isna().mean(),2)*100
#             st.text(nan[(nan)!=0])

#             st.write('''Compare the last 2 results.
#         From the results, we can see that columns: Pool QC, Fence, Misc Feature have 
#         100%, 80%, and 97%, null values respectively amongst others. All the other columns outside the displayed
#         have no null items.''')
#             st.text('')
#             st.write('''**Display sum of Null Values in one column**''')

#             c = '''# Display sum of null values in a single column in R

#         # Use any of these codes will do
# # sum of null values in a single column 1
# colSums(is.na(iowa['Lot.Frontage']))
# # sum of null values in a single column 2
# apply(X = is.na(iowa['Lot.Frontage']), MARGIN = 2, FUN =sum)
# # sum of null values in a single column 3
# sapply(iowa['Lot.Frontage'], function(x) sum(is.na(x)))
# # sum of null values in a single column 4
# lapply(iowa['Lot.Frontage'], function(x) sum(is.na(x)))
# # sum of null values in a single column 5
# mapply(function(x) sum(is.na(x)), iowa['Lot.Frontage'])
# # sum of null values in a single column 6
# sum(is.na(iowa$Lot.Frontage))
# # sum of null values in a single column 7
# sum(is.na(iowa$Alley))'''
#             R()
#             st.code(c)

#             c = '''# Display the sum of null values in a single column in Python
#         # Use any of these codes
# # sum of null values in a single column code 1
# iowa['Lot Frontage'].isna().sum()
# # sum of null values in a single column code 2
# iowa.Fence.isna().sum()
# # sum of null values in a single column code 3
# iowa['Lot Frontage'].isnull().sum()'''
#             P()
#             st.code(c)
#             Res()
#             st.text(iowa.Fence.isna().sum())
#             st.text(iowa['Lot Frontage'].isnull().sum())
#             st.text(iowa['Alley'].isna().sum())


#             st.write('''**Display sum of Null Values in two or more columns**''')

#             c = '''# missing values in some columns in R
#             # Use any of these codes
# # missing values in some columns code 1
# colSums(is.na(iowa[c('Lot.Frontage','Fence','Pool.QC')]))
# # missing values in some columns code 2
# apply(X = is.na(iowa[c('Lot.Frontage','Fence','Pool.QC')]), MARGIN = 2, FUN =sum)
# # missing values in some columns code 3
# sapply(iowa[c('Lot.Frontage','Fence','Pool.QC', 'Alley')], function(x) sum(is.na(x)))
# # missing values in some columns code 4
# lapply(iowa[c('Lot.Frontage','Fence','Pool.QC','Alley')], function(x) sum(is.na(x)))
# # missing values in some columns code 5
# mapply(function(x) sum(is.na(x)), iowa[c('Lot.Frontage','Fence','Pool.QC','Alley')])'''

#             R()
#             st.code(c)

#             c = '''# missing values in some columns in Python
# iowa[['Lot Frontage', 'Fence','Pool QC', 'Alley']].isna().sum()'''
#             P()
#             st.code(c)
#             Res()
#             st.write(iowa[['Lot Frontage', 'Fence','Pool QC', 'Alley']].isna().sum())

#             st.write('**Location of Null Values**')
#             c = '''# Location of null values in R
#         # use any of these codes
# # location of missing values in the entire dataset 1
# which(is.na(iowa))
# # location of missing values in the entire dataset 2
# apply(is.na(iowa), 2, which)
# # location of missing values in the entire dataset 3
# sapply(iowa, function(x) (is.na(x)))
# # location of missing values in the entire dataset 4
# lapply(iowa, function(x) (is.na(x)))
# # location of missing values in the entire dataset 5
# mapply(function(x) (is.na(x)), iowa)
# # location of missing values in a column
# which(is.na(iowa$Alley))
# '''
#             R()
#             st.code(c)
#             c = '''# Location of null values in Python
#         # use any of these codes
# # location of missing values in the entire dataset 1
# iowa.isna()
# # location of missing values in the entire dataset 2
# iowa.isnull()'''
#             P()
#             st.code(c)
#             Res()
#             st.caption('''The result here is True for null values and false otherwise both for R and Python.
#             For the displayed result here the tick-box is True and false when empty. However, the 'which' function
#             in R gives you the index address of the null values''')
#             st.write(iowa.isnull())
            
            

#             st.write('''Note that isna and isnull mean exactly the same in Python, they can replace each other.
#         Notice the difference: is.na in R and isna in Python. Also, the trend of R starting with the function instead
#         of the dataset's name in Python has continued.
        
# The treatment of null values in datasets have far reaching implications, it always boils down to the possible impact 
# of removing and replacing null values in the dataset and how this might likely affect the final outcome of the project. 
# We shall delve into this in details in subsequent sections''')
#             T()
        

#         if colv == 'Unique Values Counts':
#                 st.write('**Access the Composition of the Unique Values in a Column**')
#                 st.write('''Unique values are the building blocks of each column especially when the 
#                 data types is object or categorical data type in Python or Character in R. The dataset is defined 
#                 by the combination of its unique values. For example, the country column is defined by 
#                 the type of countries listed. The list of countries will determine the direction and 
#                 focus of the dataset. Is the dataset focussed on a particular continent or worldwide
#                 or countries in a particular economic bloc? The year column will define the years when 
#                 the data were collected or years when the sales happend or when the events were recorded
#                 thereby enabling us to situate the dataset in a particular period in history.  
#                 Gaining access to the composition of a column enables you to answer a very simple question:
#         'how many of a particular component are present in the dataset, and how many of the same type are represented
#         in other components? We look at the Insurance dataset with respect to this.''')
#                 c = '''# Read the insurance dataset in R
# insurance = read.csv('insurance.csv')
# insurance'''
#                 R()
#                 st.code(c)
#                 P()
#                 st.code(imp)
#                 c = '''# Read the insurance dataset in Python
# insurance = pd.read_csv('insurance.csv')'''
                
#                 st.code(c)
#                 Res()
#                 insurance = pd.read_csv('insurance.csv')
#                 insurance

                
#                 c = '''# displays the unique values in a column in R
#         # Use any of these codes
# # Unique values in the region column 1
# unique(insurance$region)
# # Unique values in the region column 2
# unique(insurance[c('region')])
# # Unique values in the region column 3
# unique(insurance[('region')])
# # Unique values in the region column 4
# distinct(insurance, region)'''
#                 R()
#                 st.code(c)
#                 c = '''# displays the unique values in a column in Python

# # Unique values in the region column 1
# insurance['region'].unique()
# # Unique values in the region column 2
# insurance.region.unique()'''
#                 P()
#                 st.code(c)
#                 fo()
#                 st.error('''       
#                 Python:- dataset['column_name'].function_term()  
#                 R:- function_term(dataset[c('column_name')])- necessary when you want to access more that one column  
#                 R:- function_name(dataset$column_name)- for accessing single columns  
#                 R:- function_name(dataset, column_name)   
#                 Python:- dataset.column_name.function()- when column_name is one word or 2 or more words linked together  
#                 ''')
#                 Res()
#                 st.text(insurance['region'].unique())
#                 st.write('Now, what is the number of the unique values in R and Python?')

#                 c = '''# number of the unique values in a column in R
                
#         # use any of these codes
# # number of the unique values in a column 1
# length(unique(insurance$region))
# # number of the unique values in a column 2
# length(table(insurance[c('region')]))
# # number of the unique values in a column 3
# length(table(insurance[('region')]))
# # number of the unique values in a column 4
# sapply(unique(insurance[c('region')]), function(x) length(x))
# # number of the unique values in a column 5
# lapply(unique(insurance[c('region')]), function(x) length(x))'''
#                 R()
#                 st.code(c)
#                 c = '''# displays the unique values in a column in Python

#         # Use any of the following codes
# # number of the unique values in a column 1
# insurance['region'].nunique()
# # number of the unique values in a column 2
# insurance.region.nunique()
# # number of the unique values in a column 3
# len(insurance['region'].unique())
# # number of the unique values in a column 3
# len(insurance.region.unique())'''
#                 P()
#                 st.code(c)
#                 Res()
#                 st.write('Number of unique values in the region column =', insurance['region'].nunique())
                
#                 Simi()
#                 st.success('''Notice that for both Python and R the codes contain 3 common terms but
#                 with different arrangement for each language:  
#                 1. The function - unique  
#                 2. Dataset's name - insurance or any dataset name   
#                 3. The target column - region or any column for that matter  
#                 ----  
#                 Task: Find the unique values in a categorical or object or character column  
#                 Again R's First Question is Which function will I use for this purpose?      
#                 Python's First Question is: Which dataset are we looking at for this purpose?  
#                 However, for both languages the dataset comes before the target column, which makes sense
#                 because you need a dataset for you to get a column. But R puts the function forward before the
#                 dataset and the column while Python presents the function last after the dataset and the column
#                 in that order. So far, we see that when R calls the function, the dataset and the column are enclosed
#                 in a bracket, whereas the function is separated from the dataset and the column by a dot '.' in Python  
#                 ''')
                

#                 st.write('')
#                 st.write('**Unique Values Count**')

#                 c = '''# Frequency of each unique value in the column in R

# # Fequency of the unique values in the region column 1
# table(insurance$region)
# # Fequency of the unique values in the region column 3
# table(insurance[c('region')])
# # Fequency of the unique values in the region column 3
# table(insurance[('region')])'''
#                 st.code(c)
#                 c = '''# Frequency of each unique value in the column in Python

# # Fequency of the unique values in the region column 1
# insurance['region'].value_counts()
# # Fequency of the unique values in the region column 2
# insurance.region.value_counts()'''
#                 P()
#                 st.code(c)
#                 Res()
#                 st.text(insurance['region'].value_counts())
#                 st.write('The result in percentage')
#                 st.text(insurance['region'].value_counts(normalize = True)*100)
#                 # a = len(insurance[(insurance['region']== 'southeast')])
#                 # b = len(insurance['region'])
#                 # st.text((a/b)*100)
#                 st.caption('''Notice that in Python the result is sorted while that R arranges the result 
#                 of the unique value count as they occure in the dataset. We can however sort the result:''')

#                 c = '''# Sort the unique values count in descending order in R

# # Sort the unique values count 1
# sort(table(insurance$region),decreasing = TRUE)
# # Sort the unique values count 2
# sort(table(insurance[c('region')]),decreasing = TRUE)
# # Sort the unique values count 3
# sort(table(insurance[('region')]),decreasing = TRUE)'''
#                 R()
#                 st.code(c)
#                 Res()
#                 st.text(insurance['region'].value_counts())

#                 st.write('''Note that the count in the code is plural - comes with an s. 
#                 Also note that this sections works better for columns with the object data type. 
#                 Furthermore, null values are not counted by default. However, if you want to access the 
#                 composition of null values you add another parameter. Check the code below, where 
#                 dropna means 'drop-null', and you set it to false.''')
#                 c = '''# Count null values with the unique values in python
# insurance['smoker'].value_counts(dropna = False)'''
#                 P()
#                 st.code(c)
#                 T()
#                 st.text(insurance.region.unique())
                
#                 st.text(insurance.region.nunique())
                
                

# # @st.experimental_memo
# # def get_data():
# #     return pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# # tab1, tab2, tab3 = st.tabs(["Filter Data", "Raw Data", "📈 Chart"])
# # with tab1:
# #     col = st.selectbox("Select column", options=["a", "b", "c"])
# #     filter = st.slider("Filter range", -2.5, 2.5, (-2.0, 2.0), step=0.01)
# #     filter_query = f"{filter[0]} < {col} < {filter[1]}"

# # with tab2:
# #     st.dataframe(get_data().query(filter_query))

# # with tab3:
# #     st.line_chart(get_data().query(filter_query))

# st.write('---')

# tab1, tab2 = st.tabs(["tab1", "tab2"])

# with tab1:
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.selectbox("City", ["City1", "City2"])
#     with col2:
#         st.selectbox("District", ["District1", "District2"])
#     with col3:
#         st.write('**Notes**')
#         exp = st.expander('Explanation')
#         exp.write('God loves you')

# with tab2:
#     col1, col2 = st.columns(2)
#     with col1:
#         st.selectbox("Another City", ["Another_City1", "Another_City2"])
#     with col2:
#         st.selectbox("Another District", ["Another_District1", "Another_District2"])

# st.write('---')


# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# with tab1:
#     st.header("A cat")
#     try:
#         st.image("_", width=200) # I changed here on purpose to raise an error
#     except FileNotFoundError:
#         st.text("File not found")

# with tab2:
#     st.header("A dog")
#     try:
#         st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
#     except FileNotFoundError:
#         st.text("File not found")

# with tab3:
#     st.header("An owl")
#     try:
#         st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
#     except FileNotFoundError:
#         st.text("File not found")


# st.write('---')


# col1, col2, col3 = st.columns(3)
# with col1:
#         st.header('Stage 1')

#         hold, tab1, tab2, tab3 = st.tabs(['Hold',"Cat", "Dog", "Owl"])

#         def compute_tab1():
#                 st.header("A cat")
#                 try:
#                         st.image("_", width=200) # I changed here on purpose to raise an error
#                 except FileNotFoundError:
#                         st.text("File not found")


#         def compute_tab2():
#                 st.header("A dog")
#                 try:
#                         st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
#                 except FileNotFoundError:
#                         st.text("File not found")

#         def compute_tab3():
#                 st.header("An owl")
#                 try:
#                         st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
#                 except FileNotFoundError:
#                         st.text("File not found")

#         with tab1:
#                 compute_tab1()

#         with tab2:
#                 compute_tab2()

#         with tab3:
#                 compute_tab3()

# with col2:
#         st.header('Stage 2')
#         @st.experimental_memo
#         def get_data():
#                 return pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

#         tabA, tab1, tab2, tab3 = st.tabs(['Hold',"Filter Data", "Raw Data", "📈 Chart"])
        
#         with tab1:
#                 col = st.selectbox("Select column", options=["a", "b", "c"])
#                 filter = st.slider("Filter range", -2.5, 2.5, (-2.0, 2.0), step=0.01)
#                 filter_query = f"{filter[0]} < {col} < {filter[1]}"

#         with tab2:
#                 st.dataframe(get_data().query(filter_query))
#         with tab3:
#                 st.line_chart(get_data().query(filter_query))


                





