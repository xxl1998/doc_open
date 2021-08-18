.. vim: syntax=rst

.. _about_this_project:

这个仓库的搭建过程
====================


起源
--------------------

| 从初次接触编程，接触嵌入式，看很多在线文档时，都会感叹页面的整洁与层次，比如:
| https://docs.openmv.io/index.html
| http://www.openedv.com/docs/index.html
| http://doc.embedfire.com/products/link/zh/latest/index.html
| http://tutorial.linux.doc.embedfire.com
| https://book.openmv.cc/
| 于是在写文章、博客时，总会想到，能不能把自己的写作内容也整理成这样的？
随着挖坑越来越多，代码、笔记的整理也相当令人头疼，如果能和代码一样，将文章也使用git进行管理，那么备份、更新、
版本管理就相当方便，于是就开始寻找这些在线文档的共同之处。


调查
--------------------

查看各种网站，在很多地方都看到了这样的内容\ ``Built with Sphinx using a theme provided by Read the Docs .``\ 
搜索关键字得知了Sphinx这个构建文档的神器，通过reStructuredText编写的文档，可以方便地转换成html网页，LaTeX、PDF等格式，
除此之外，相比于markdown，reStructuredText可以进行多个文件之间的相互引用，这样对于大型的文档、教程等，就可以方便地分成多个文件，
进行版本管理，而不至于在一个文件中写上几百上千页，对读者也比较友好。

| 这时也看到了野火的开源项目：
| https://gitee.com/Embedfire/embed_linux_tutorial
| https://gitee.com/Embedfire/ebf_contribute_guide
| 恰好就是用的Sphinx+reStructuredText，于是参考野火的方案，做了这个仓库，在这里也对野火的开源表示感谢。


安装Sphinx
--------------------

Sphinx是基于Python的，首先从官网下载exe安装Python，然后使用pip安装Sphinx：

.. code-block:: shell

    python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx


新建Sphinx文档项目
--------------------

打开cmd窗口，使用cd命令进入目标文件夹（最好是空目录），然后使用如下命令创建新的Sphinx文档项目

.. code-block:: shell

    sphinx-quickstart

主要是填写作者、项目名、语言，作者、项目名自行填写，可用中文，语言输入zh_CN就行，其他选项全部使用默认的，直接回车。
这里我是使用了自动生成的基本目录，在野火的基础上修改的conf.py、layout.html等文件。


转换PDF
--------------------

转换PDF需要LaTeX环境，如果安装texlive，据说安装包有几个G，这里安装的是miktex和strawberryperl。

安装miktex，下载链接：
https://miktex.org/download
默认选择windows，64位的安装包，国内下载速度还行，安装包100多MB，一路默认安装即可，它和VSCode都是默认安装在用户目录下，
而不是像很多软件总是要管理员权限，默认是去C盘根目录创建新文件夹。
（没错，说的就是strawberryperl）

转换PDF用到的latexmk命令就在:\ ``C:\Users\your-name\AppData\Local\Programs\MiKTeX\miktex\bin\x64\latexmk.exe``\ 

安装strawberryperl，下载链接：
https://strawberryperl.com/
选择64位版本下载安装即可，我之前不知何时装过32位的strawberryperl，又安装64位的导致出现问题，两个都卸载了，重新安装64位的就好了。

另外需要在sphinx的conf.py里面配置latex_engine和latex_elements，这些我们已经配置好，
运行命令\ ``make latexpdf``\ 即可生成PDF文件。首次运行时，miktex需要安装一大堆的“宏包”，全部确定安装，
如果报错说miktex需要更新，打开“MiKTeX Console”（开始菜单有快捷方式）
更新一下，再使用命令转换PDF，安装完所需“宏包”，就能成功转换了。

在\ ``build/latex``\ 下可以查看到生成的 PDF 文档。

PDF空白页问题
--------------------

使用野火的conf.py模板，生成的PDF总是有些空白页面，观察发现空白页只在偶数页面出现，最终搜索到了解决方法：
在conf.py配置如下内容：

.. code-block:: shell

    latex_elements = {
        'extraclassoptions': 'openany,oneside',
    }

表示使用单页打印，这样PDF中就不会出现空白页面了。

参考链接：https://learn-rst.readthedocs.io/zh_CN/latest/reST-%E6%89%A9%E5%B1%95/latex.html#sphinx-latex-pdf

学习rst
--------------------

| 参考链接：
| https://www.sphinx.org.cn/usage/restructuredtext/basics.html
| https://github.com/readthedocs/sphinx_rtd_theme
| https://docgenerate.readthedocs.io/en/latest/index.html
