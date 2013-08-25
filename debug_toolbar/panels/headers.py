from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from debug_toolbar.panels import DebugPanel


class HeaderDebugPanel(DebugPanel):
    """
    A panel to display HTTP headers.
    """
    name = 'Header'
    template = 'debug_toolbar/panels/headers.html'
    has_content = True
    # List of headers we want to display
    HEADERS = [
        'CONTENT_TYPE',
        'HTTP_ACCEPT',
        'HTTP_ACCEPT_CHARSET',
        'HTTP_ACCEPT_ENCODING',
        'HTTP_ACCEPT_LANGUAGE',
        'HTTP_CACHE_CONTROL',
        'HTTP_CONNECTION',
        'HTTP_HOST',
        'HTTP_KEEP_ALIVE',
        'HTTP_REFERER',
        'HTTP_USER_AGENT',
        'QUERY_STRING',
        'REMOTE_ADDR',
        'REMOTE_HOST',
        'REQUEST_METHOD',
        'SCRIPT_NAME',
        'SERVER_NAME',
        'SERVER_PORT',
        'SERVER_PROTOCOL',
        'SERVER_SOFTWARE',
    ]

    def nav_title(self):
        return _('HTTP Headers')

    def title(self):
        return _('HTTP Headers')

    def url(self):
        return ''

    @property
    def header_filter(self):
        if hasattr(settings, 'DEBUG_TOOLBAR_CONFIG'):
            extra_headers = settings.DEBUG_TOOLBAR_CONFIG.get('EXTRA_HEADERS', [])
        else:
            extra_headers = []
        return self.HEADERS + extra_headers

    def process_request(self, request):
        self.headers = dict(
            [(k, request.META[k]) for k in self.header_filter if k in request.META]
        )

    def process_response(self, request, response):
        self.record_stats({
            'headers': self.headers
        })
