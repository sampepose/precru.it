class disable_csrf:
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        return None
