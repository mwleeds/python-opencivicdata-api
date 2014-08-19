from opencivicdata.api.service import Service
from opencivicdata.api.result import OCDListResult, OCDDictResult


class OCDAPI(Service):
    def __init__(self, host=None, apikey=None):
        """
        """
        self.setup(host=host, apikey=apikey)

    def _get(self, entity_id, **kwargs):
        """
        """
        return self._query(
            entity_id,
            handler=OCDDictResult,
            **kwargs
        )

    def organizations(self, **kwargs):
        """
        """
        return self._query(
            "organizations",
            handler=OCDListResult,
            **kwargs
        )

    def organization(self, organization_id, *args, **kwargs):
        """
        """
        return self._get(organization_id, *args, **kwargs)

    def person(self, person_id, *args, **kwargs):
        """
        """
        return self._get(person_id, *args, **kwargs)

    def bill(self, bill_id, *args, **kwargs):
        """
        """
        return self._get(bill_id, *args, **kwargs)

    def vote(self, vote_id, *args, **kwargs):
        """
        """
        return self._get(vote_id, *args, **kwargs)

    def event(self, event_id, *args, **kwargs):
        """
        """
        return self._get(event_id, *args, **kwargs)