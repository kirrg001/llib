from django.utils import simplejson
from django.utils.functional import Promise
from django.utils.encoding import force_unicode

class LazyEncoder(simplejson.JSONEncoder):
    """Encodes django's lazy i18n strings.
    """
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return obj