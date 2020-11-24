import abc


# Strategy to get information of an organization
class OrganizationStrategyAbstract(abc.ABC):
    @abc.abstractmethod
    def get_organization(self):
        """"Function to fetch all the available data of an organization"""


class APIOrganizationStrategy(OrganizationStrategyAbstract):
    def get_organization(self):
        return 'Get organization info from restful API'


# Strategy to monitor organization's changes
class MonitoringStrategyAbstract(abc.ABC):
    @abc.abstractmethod
    def check_monitoring(self):
        """Function to check all changes over the organizations"""


class FileMonitoring(MonitoringStrategyAbstract):
    def check_monitoring(self):
        return 'Monitoring changes through a file'


class APIMonitoring(MonitoringStrategyAbstract):
    def check_monitoring(self):
        return 'Monitoring changes through an API call'
