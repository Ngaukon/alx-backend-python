#!/usr/bin/env python3
"""Module for testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the `GithubOrgClient` class."""
    
    @parameterized.expand([
        ("google", {'login': "google"}),  # Test with organization name and expected response
        ("abc", {'login': "abc"}),        # Another test case with different organization
    ])
    @patch("client.get_json")
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests the `org` method of GithubOrgClient."""
        mocked_fxn.return_value = MagicMock(return_value=resp)  # Mock the return value of get_json
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)  # Assert that the org method returns the expected response
        mocked_fxn.assert_called_once_with(  # Ensure get_json was called with the correct URL
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property of GithubOrgClient."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            # Assert that the _public_repos_url returns the correct URL from the org property
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method of GithubOrgClient."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]  # Mock return value for repos
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]  # Mock the repos URL property
            # Assert that the public_repos method returns the correct list of repo names
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()  # Ensure the property was accessed once
        mock_get_json.assert_called_once()  # Ensure get_json was called once

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),  # Test with matching license key
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),      # Test with non-matching license key
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Tests the `has_license` method of GithubOrgClient."""
        gh_org_client = GithubOrgClient("google")
        client_has_licence = gh_org_client.has_license(repo, key)  # Check if repo has the specified license
        self.assertEqual(client_has_licence, expected)  # Assert that the result matches expected value


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],  # Organization payload for tests
        'repos_payload': TEST_PAYLOAD[0][1],  # Repositories payload for tests
        'expected_repos': TEST_PAYLOAD[0][2],  # Expected repositories output
        'apache2_repos': TEST_PAYLOAD[0][3],  # Expected repositories with Apache 2.0 license
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the `GithubOrgClient` class."""
    
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class-level fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,  # Map API route to organization payload
            'https://api.github.com/orgs/google/repos': cls.repos_payload,  # Map API route to repositories payload
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})  # Return mock for known URLs
            return HTTPError  # Raise HTTPError for unknown URLs

        cls.get_patcher = patch("requests.get", side_effect=get_payload)  # Patch requests.get to use the mock
        cls.get_patcher.start()  # Start the patcher

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method using integration tests."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,  # Check if the output matches expected repos
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a specified license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,  # Check if the output matches expected repos with license
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Cleans up class-level fixtures after running all tests."""
        cls.get_patcher.stop()  # Stop the patcher to restore original behavior
