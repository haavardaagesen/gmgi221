import importlib
names = ['jupyter_book','jupyter_book.build','sphinx','myst_nb','myst_parser','sphinx_book_theme']
for n in names:
    try:
        m = importlib.import_module(n)
        print(n, '->', getattr(m, '__file__', 'built-in'))
    except Exception as e:
        print(n, 'import error:', e)
