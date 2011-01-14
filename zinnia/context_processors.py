"""Context Processors for Zinnia"""
from zinnia import __version__
from zinnia.settings import STATIC_URL


def media(request):
    """Adds media-related context variables to the context"""
    return {'ZINNIA_MEDIA_URL': STATIC_URL}


def version(request):
    """Adds version of Zinnia to the context"""
    return {'ZINNIA_VERSION': __version__}
