from apartment.models import AptApproved
from django.db.models import Q


def get_apartment(street_address, city, state, country):
    try:
        result = AptApproved.objects.get(
            Q(country__iexact=country),
            Q(state__iexact=state),
            Q(city__iexact=city),
            Q(street_address__iexact=street_address))
    except AptApproved.DoesNotExist:
        result = None
    return result
