# 3rd Party Libraries
from allauth_2fa.middleware import BaseRequire2FAMiddleware


class RequireUser2FAMiddleware(BaseRequire2FAMiddleware):
    def require_2fa(self, request):
        # Superusers are not required to have 2FA.
        return not request.user.is_superuser
