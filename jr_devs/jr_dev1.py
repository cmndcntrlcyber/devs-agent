class JrDev1:
    def __init__(self):
        self.draft_program = {
            'features': [],
            'bugs': [],
            'version': 0.1
        }
        self.requests = []

    def create_initial_draft(self):
        # Logic to create the initial draft of the program
        # Here we'll simulate the creation of a program draft by initializing a dictionary
        self.draft_program['features'].append("Basic program structure")
        self.draft_program['version'] = 0.1
        print(f"Draft program created with version {self.draft_program['version']}: {self.draft_program['features']}")

    def receive_requests(self, requests):
        # Logic to receive new requests from jr_dev5
        # Requests will be a list of tuples with the format (type, description)
        for req_type, description in requests:
            if req_type == 'feature':
                self.draft_program['features'].append(description)
            elif req_type == 'bug':
                self.draft_program['bugs'].append(description)
            print(f"Received request to add a {req_type}: {description}")

    def implement_requests(self):
        # Logic to implement the received requests
        for feature in self.draft_program['features']:
            print(f"Implementing feature: {feature}")
        for bug in self.draft_program['bugs']:
            print(f"Fixing bug: {bug}")
        
        # Incrementing version number after implementing requests
        self.draft_program['version'] += 0.1
        print(f"Updated program to version {self.draft_program['version']}")

        # Clearing requests after they have been implemented
        self.draft_program['features'].clear()
        self.draft_program['bugs'].clear()

# This code will be saved to a Python file.
# For demonstration purposes, let's instantiate the class and run its methods to show their functionality.

# Mock run
jr_dev1 = JrDev1()
jr_dev1.create_initial_draft()
jr_dev1.receive_requests([('feature', 'User authentication'), ('bug', 'Fix page load issue')])
jr_dev1.implement_requests()

# Since this is a coding environment, we'll display the outputs here.
# In an actual file, we would not include the mock run and print statements.