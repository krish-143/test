import requests
import json
import argparse
import os
import base64

class Repo:
    """
    This class represents a GitHub repository creation utility. It includes methods for creating a repository,
    configuring it based on engineer type (Platform or Data), and adding collaborators.
    """

    # GitHub API headers
    auth_headers = {
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(os.getenv("GITHUB_TOKEN"))
    }

    def __init__(self, org, repo_name, description, engineer_type):
        """
        Initialize a Repo object with the given organization, repository name, description, and engineer type.
        """
        self.org = org
        self.repo_name = repo_name
        self.description = description
        self.engineer_type = engineer_type

    def create_repo(self):
        """
        Create a new repository with the given description.
        """
        repo_creation_config = {
            "name": self.repo_name,
            "description": self.description,
            "homepage": "https://github.com",
            "private": True,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True,
            "auto_init": True
        }

        r = requests.post(
            "https://api.github.com/user/repos",
            headers=self.auth_headers,
            data=json.dumps(repo_creation_config)
        )

        res_dict = json.loads(r.text)

        if r.status_code == 201:
            print(f"Created: {res_dict['html_url']}")
        else:
            print(f'Create repo error Message: {res_dict["message"]}')

        return res_dict["name"]

    def add_collaborators(self, collaborators):
        """
        Add collaborators to the repository.
        """
        for collaborator in collaborators:
            username, permission = collaborator.split(":")
            r = requests.put(
                f"https://api.github.com/repos/{self.org}/{self.repo_name}/collaborators/{username}",
                headers=self.auth_headers,
                data=json.dumps({"permission": permission})
            )

            if r.status_code == 200:
                print(f"{username} added to repo with permission: {permission}")
            elif r.status_code == 204:
                print(f"{username} already has {permission} permissions")
            else:
                res_dict = json.loads(r.text)
                print('Error Message: {}'.format(res_dict["message"]))

    def configure_for_platform_engineer(self):
        """
        Configure repository for a Platform Engineer.
        """
        print("Configuring repository for Platform Engineer...")
        # Add Terraform configurations
        self.add_terraform_configurations()
        # Add collaborators specific to Platform Engineer
        self.add_collaborators(["admin-user:admin", "maintain-user:maintain"])
        print("Repository configured for Platform Engineer.")

    def configure_for_data_engineer(self):
        """
        Configure repository for a Data Engineer.
        """
        print("Configuring repository for Data Engineer...")
        # Add Python configurations
        self.add_python_configurations()
        # Add collaborators specific to Data Engineer
        self.add_collaborators(["data-user:read"])
        print("Repository configured for Data Engineer.")

    def add_terraform_configurations(self):
        """
        Add Terraform configurations to the repository.
        """
        # Add Terraform files, example: main.tf, variables.tf
        # This could be implemented based on your organization's Terraform best practices
        pass

    def add_python_configurations(self):
        """
        Add Python configurations to the repository.
        """
        # Add Python files, example: requirements.txt, script.py
        # This could be implemented based on your organization's Python best practices
        pass

    # Other methods for additional functionalities like adding CI/CD configurations, etc.

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="GitHub Repo Creation Utility",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--name", help="Repository Name")
    parser.add_argument("-o", "--organization", help="Organization Name")
    parser.add_argument("-d", "--description", help="Repository Description", default="")
    parser.add_argument("-t", "--engineer-type", help="Engineer Type (platform or data)", default="platform")
    parser.add_argument("-b", "--defbranch", help="Default Branch", default="main")
    args, unknown = parser.parse_known_args()  # Parse only known arguments
    config = vars(args)
    print(f"Arguments Passed in: {config}")

    if "GITHUB_TOKEN" not in os.environ:
        print("GITHUB TOKEN not in environment")
        exit(1)
    elif args.name is None:
        print("Repo Name required")
        exit(1)
    else:
        print("Creating Repo")
        repo = Repo(args.organization, args.name, args.description, args.engineer_type)
        repo_name = repo.create_repo()

        if args.engineer_type == "platform":
            repo.configure_for_platform_engineer()
        elif args.engineer_type == "data":
            repo.configure_for_data_engineer()
        else:
            print("Invalid engineer type provided.")

import requests
import json
import argparse
import os
import base64

class Repo:
    """
    This class represents a GitHub repository creation utility. It includes methods for creating a repository,
    configuring it based on engineer type (Platform or Data), and adding collaborators.
    """

    # GitHub API headers
    auth_headers = {
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(os.getenv("GITHUB_TOKEN"))
    }

    def __init__(self, org, repo_name, description, engineer_type):
        """
        Initialize a Repo object with the given organization, repository name, description, and engineer type.
        """
        self.org = org
        self.repo_name = repo_name
        self.description = description
        self.engineer_type = engineer_type

    def create_repo(self):
        """
        Create a new repository with the given description.
        """
        repo_creation_config = {
            "name": self.repo_name,
            "description": self.description,
            "homepage": "https://github.com",
            "private": True,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True,
            "auto_init": True
        }

        r = requests.post(
            "https://api.github.com/user/repos",
            headers=self.auth_headers,
            data=json.dumps(repo_creation_config)
        )

        res_dict = json.loads(r.text)

        if r.status_code == 201:
            print(f"Created: {res_dict['html_url']}")
        else:
            print(f'Create repo error Message: {res_dict["message"]}')

        return res_dict["name"]

    def add_collaborators(self, collaborators):
        """
        Add collaborators to the repository.
        """
        for collaborator in collaborators:
            username, permission = collaborator.split(":")
            r = requests.put(
                f"https://api.github.com/repos/{self.org}/{self.repo_name}/collaborators/{username}",
                headers=self.auth_headers,
                data=json.dumps({"permission": permission})
            )

            if r.status_code == 200:
                print(f"{username} added to repo with permission: {permission}")
            elif r.status_code == 204:
                print(f"{username} already has {permission} permissions")
            else:
                res_dict = json.loads(r.text)
                print('Error Message: {}'.format(res_dict["message"]))

    def configure_for_platform_engineer(self):
        """
        Configure repository for a Platform Engineer.
        """
        print("Configuring repository for Platform Engineer...")
        # Add Terraform configurations
        self.add_terraform_configurations()
        # Add collaborators specific to Platform Engineer
        self.add_collaborators(["admin-user:admin", "maintain-user:maintain"])
        print("Repository configured for Platform Engineer.")

    def configure_for_data_engineer(self):
        """
        Configure repository for a Data Engineer.
        """
        print("Configuring repository for Data Engineer...")
        # Add Python configurations
        self.add_python_configurations()
        # Add collaborators specific to Data Engineer
        self.add_collaborators(["data-user:read"])
        print("Repository configured for Data Engineer.")

    def add_terraform_configurations(self):
        """
        Add Terraform configurations to the repository.
        """
        # Add Terraform files, example: main.tf, variables.tf
        # This could be implemented based on your organization's Terraform best practices
        pass

    def add_python_configurations(self):
        """
        Add Python configurations to the repository.
        """
        # Add Python files, example: requirements.txt, script.py
        # This could be implemented based on your organization's Python best practices
        pass

    # Other methods for additional functionalities like adding CI/CD configurations, etc.

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="GitHub Repo Creation Utility",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--name", help="Repository Name")
    parser.add_argument("-o", "--organization", help="Organization Name")
    parser.add_argument("-d", "--description", help="Repository Description", default="")
    parser.add_argument("-t", "--engineer-type", help="Engineer Type (platform or data)", default="platform")
    parser.add_argument("-b", "--defbranch", help="Default Branch", default="main")
    unknown = parser.parse_known_args()  # Parse only known arguments
    config = vars(unknown)
    print("Arguments Passed in: {config}")

    if "GITHUB_TOKEN" not in os.environ:
        print("GITHUB TOKEN not in environment")
        exit(1)
    elif args.name is None:
        print("Repo Name required")
        exit(1)
    else:
        print("Creating Repo")
        repo = Repo(args.organization, args.name, args.description, args.engineer_type)
        repo_name = repo.create_repo()

        if args.engineer_type == "platform":
            repo.configure_for_platform_engineer()
        elif args.engineer_type == "data":
            repo.configure_for_data_engineer()
        else:
            print("Invalid engineer type provided.")

