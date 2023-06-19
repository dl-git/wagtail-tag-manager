try:
    import django
except ImportError:
    # setup.py and docs do not have Django installed.
    django = None

if django and django.VERSION < (3, 2):
    default_app_config = "wagtail_tag_manager.config.WagtailTagManagerConfig"
