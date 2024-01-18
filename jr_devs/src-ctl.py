class SrcCtl:
    def __init__(self, repo_url):
        self.repo_url = repo_url
        self.branches = ['main']

    def clone_repo(self):
        # Logic to clone a repository from GitHub
        print(f"Cloning repository from {self.repo_url}")

    def create_branch(self, branch_name):
        # Logic to create a new branch in the repository
        if branch_name not in self.branches:
            self.branches.append(branch_name)
            print(f"Branch '{branch_name}' created")
        else:
            print(f"Branch '{branch_name}' already exists")

    def commit_changes(self, branch_name, commit_message):
        # Logic to commit changes to a branch
        if branch_name in self.branches:
            print(f"Changes committed to '{branch_name}' with message: '{commit_message}'")
        else:
            print(f"Branch '{branch_name}' does not exist")

    def push_changes(self, branch_name):
        # Logic to push changes to GitHub
        if branch_name in self.branches:
            print(f"Changes pushed to branch '{branch_name}' in {self.repo_url}")
        else:
            print(f"Branch '{branch_name}' does not exist")