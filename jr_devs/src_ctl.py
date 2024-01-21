class SrcCtl:
    def __init__(self, repo_url, pat=None):
        self.repo_url = repo_url
        self.pat = pat or os.getenv('GITHUB_PAT')
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
        # Modified push_changes to use PAT
        if branch_name in self.branches:
            push_command = f"git push origin {branch_name}"
            self._run_git_command(push_command)
            print(f"Changes pushed to branch '{branch_name}' in {self.repo_url}")
        else:
            print(f"Branch '{branch_name}' does not exist")

    def _run_git_command(self, command):
        # Helper method to run Git commands with PAT authentication
        complete_command = f"echo {self.pat} | {command}"
        subprocess.run(complete_command, shell=True)