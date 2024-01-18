from src_ctl import SrcCtl

class JrDev2:
    def __init__(self, src_ctl: SrcCtl):
        self.branches = []

    def create_branch(self, base, branch_name):
        # Logic to create a branch from the base
        self.branches.append((base, branch_name))
        print(f"Branch '{branch_name}' created from '{base}'")
        self.src_ctl.create_branch(branch_name)
        self.src_ctl.commit_changes(branch_name, f"Create branch {branch_name}")

    def work_on_bugs(self, branch_name, bug_list):
        # Logic to work on bugs in the specified branch
        for bug in bug_list:
            print(f"Working on {bug} in '{branch_name}'")
        # Assuming the bugs are fixed, we'd commit the changes
        print(f"All bugs fixed in '{branch_name}' and ready for review")
        self.src_ctl.commit_changes(branch_name, "Fixed bugs")
        self.src_ctl.push_changes(branch_name)

    def document_changes(self, branch_name):
        # Logic to document changes made in the branch
        print(f"Documentation updated for changes in '{branch_name}'")
        self.src_ctl.commit_changes(branch_name, "Updated documentation")
        self.src_ctl.push_changes(branch_name)


