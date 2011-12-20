Usage
=====

In your settings.py::

    INSTALLED_APPS = (
        ...
        'debug_template',
        ...
    )


In you template::

  {% load debug %}
  {{ var|ipdb }}
