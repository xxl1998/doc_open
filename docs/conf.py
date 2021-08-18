# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'[飞觞醉月]博客、教程、项目、挖坑填坑'
copyright = u'2021, 飞觞醉月-www.fszy.xyz'
author = u'飞觞醉月- www.fszy.xyz'


# -- General configuration ---------------------------------------------------
# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark',
  'sphinx_markdown_tables',
  'sphinx.ext.autosectionlabel',
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', 'rest', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# default hightlight languate
highlight_language = "sh"

html_show_sourcelink = False

html_show_sphinx = False
###########################################################################
#                           pdf - configuration                           #
###########################################################################

project_language = 'zh_CN'
latex_use_xindy = True
latex_engine = 'xelatex'

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& START &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
# (源文件, '输出文档名称', u'封面标题', u'作者', '主题')
# 此处仅修改封面标题即可，与上方 “project = ‘’ ”保持一致,其他参数请勿修改
latex_documents = [
    (master_doc, 'output.tex_bak', u'[飞觞醉月]博客、教程、项目、挖坑填坑',
     u'飞觞醉月', 'manual'),
]
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  END  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#

#****************************** START **********************************#
#详细修改说明文中有标注，其中%为注释符号，
#可修改的部分为页面边距、目录深度、章节编号深度
#页眉的设定为必改项
latex_elements = {
    'preamble': r'''
\def\pageautorefname{page}
\usepackage{geometry}%用于设置页面上下左右页边距
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% start %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    \geometry{left=2cm,right=2cm,top=2.5cm,bottom=4cm}%页边距具体数值
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% end %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
\PassOptionsToPackage{quiet}{xeCJK}
\PassOptionsToPackage{quiet}{fontspec}
\usepackage{xeCJK}%设置中文字体
    \setCJKfamilyfont{hei}{SimHei} %黑体hei
    \setCJKfamilyfont{sun}{SimSun} %黑体hei
    \newcommand{\hei}{\CJKfamily{hei}} %黑体(Windows自带simhei.ttf,linux上需要安装字体)
    \newcommand{\sun}{\CJKfamily{sun}} %黑体(Windows自带simsun.ttf,linux上需要安装字体)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% start %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\setcounter{tocdepth}{2} %目录深度
\setcounter{secnumdepth}{4} %章节编号深度
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% end %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    

%生成的PDF标签带序号
%\hypersetup{bookmarksnumbered=true}

\usepackage{titlesec}
\usepackage{CJKnumb}
\usepackage{titletoc}
%修改文档中的章节名使用中文
\titleformat{\chapter}{\centering\Huge\bfseries}{}{1em} {}
%修改文档中的章节名前面空出的距离
\titlespacing{\chapter}{0cm}{0cm}{1em}  
%修改目录的章节名使用中文
\titlecontents{chapter}[0pt]{\addvspace{1.5pt}\filright\bf}%
               {\contentspush{\color{TitleColor} }}%
               {}{\titlerule*[8pt]{.}\contentspage}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% start %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%修改页眉设置，页眉分为两种格式
%一种是教程类：页眉右侧文字部分为标题和副标题
%另一类是手册类：页眉右侧文字部分只有主标题
%下面两种配置二选一，不使用的配置用‘%’屏蔽
%可根据生成的PDF来调整页眉字体，使观感协调
%字体大小：\tiny \scriptsize \footnotesize \small \normalsize \large \Large \LARGE \huge \Huge
%字体加粗：\textbf{} 括号内为加粗文本，可直接使用 \upname 的定义
%*******************************************%
\newcommand\upname{[飞觞醉月]博客、教程、项目、挖坑填坑}
\newcommand\downname{www.fszy.xyz}
\newcommand\fancyheadstyle{\fancyhead[R]{\LARGE \textbf{\upname} \\ \normalsize \downname}}
%*******************************************%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% end %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    

\usepackage{graphicx}
\usepackage[UTF8]{ctex}  
''',
#单页模式打印，否则有空白页
    'extraclassoptions': 'openany,oneside',
}

#*******************************  END  **********************************#