import unittest

from .provider import Provider, SynchronousProvider, AsynchronousProvider
from .strategy_provider import APIOrganizationStrategy, APIMonitoring


class TestProvider(unittest.TestCase):

    def test_perform_quack(self):
        test_provider = Provider(APIOrganizationStrategy(), APIMonitoring())
        self.assertEqual(test_provider.perform_get_organization(), 'Get organization info from restful API')
        self.assertEqual(test_provider.perform_check_monitoring(), 'Monitoring changes through an API call')


class TestSynchronousProvider(unittest.TestCase):
    def test_sync_provider(self):
        test_sync_provider = SynchronousProvider()
        self.assertEqual(test_sync_provider.perform_get_organization(), 'Get organization info from restful API')
        self.assertEqual(test_sync_provider.perform_check_monitoring(), 'Monitoring changes through an API call')


class TestAsynchronousProvider(unittest.TestCase):
    def test_sync_provider(self):
        test_sync_provider = AsynchronousProvider()
        self.assertEqual(test_sync_provider.perform_get_organization(), 'Get organization info from restful API')
        self.assertEqual(test_sync_provider.perform_check_monitoring(), 'Monitoring changes through a file')
