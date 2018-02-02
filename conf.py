from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

master_doc = 'index'
project = u'Artwork Archive'
copyright = u'CC-BY-SA, Max Lupo, 2018'

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Artwork Archive'
epub_author = u'Max Lupo'
epub_publisher = u'Max Lupo'
epub_copyright = u'2018, Max Lupo'

# def setup(app):
#     app.add_stylesheet('css/resize.css')
