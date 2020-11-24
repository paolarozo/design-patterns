from .strategy_provider import APIOrganizationStrategy
from .strategy_provider import FileMonitoring, APIMonitoring


class Provider:

    def __init__(self, organization_strategy, monitoring_strategy):
        self._organization_strategy = organization_strategy
        self._monitoring_strategy = monitoring_strategy

    def perform_get_organization(self):
        return self._organization_strategy.get_organization()

    def perform_check_monitoring(self):
        return self._monitoring_strategy.check_monitoring()


class SynchronousProvider(Provider):
    def __init__(self):
        super().__init__(APIOrganizationStrategy(), APIMonitoring())


class AsynchronousProvider(Provider):
    def __init__(self):
        super().__init__(APIOrganizationStrategy(), FileMonitoring())
