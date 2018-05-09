class GoogleCampaignMiddleware:
    """This middleware captures the various utm* querystring pararmeters and saves them in session."""

    UTM_CODES = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not request.session.get('utm'):
            request.session['utm'] = {}

        if request.GET.get('utm_source'):
            utm = {}

            for code in self.UTM_CODES:
                value = request.GET.get(code)
                if value:
                    utm[code] = value

            request.session['utm'] = utm

        # store utm codes on the request object, so they're available in templates
        request.utm = request.session['utm']

        response = self.get_response(request)

        return response
