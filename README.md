## CI/CD Architecture

This project is designed to execute automated tests inside Docker and integrate seamlessly with Jenkins.

### Execution Flow

```text
Developer Pushes Code
        │
        ▼
Git Repository
        │
        ▼
Jenkins Controller
        │
        ▼
Job Queue
        │
        ▼
Available Jenkins Agent (EC2/Docker Host)
        │
        ▼
Clone Repository into Workspace
        │
        ▼
docker build -t pytest-framework .
        │
        ▼
Docker Image
        │
        ▼
docker run pytest-framework
        │
        ▼
uv run pytest --alluredir=/app/allure-results
        │
        ▼
Allure Results Generated
        │
        ▼
Results Written to Jenkins Workspace
        │
        ▼
Jenkins Allure Plugin
        │
        ▼
Allure Dashboard
```

---

## Jenkins Components

### Jenkins Controller

The Jenkins Controller is responsible for:

- Receiving GitHub webhooks or scheduled build triggers
- Maintaining the build queue
- Selecting an available build agent
- Sending the Jenkins pipeline to the selected agent
- Collecting logs and test artifacts
- Publishing the Allure dashboard

The controller typically does **not** execute the build itself.

---

### Jenkins Agents

Build agents (formerly called *slaves*) perform the actual work.

An agent is responsible for:

- Cloning the repository
- Building the Docker image
- Running the Docker container
- Executing the pytest test suite
- Producing Allure test results
- Returning logs and artifacts to the controller

Many organizations provision agents dynamically using AWS EC2, allowing each build to execute on a clean machine.

---

## Docker Build vs Docker Run

The pipeline executes two Docker commands.

### Build Image

```bash
docker build -t pytest-framework .
```

Reads the Dockerfile and creates a reusable Docker image containing:

- Python
- uv
- Project dependencies
- Test framework
- Test suite

The image is stored by Docker and can be reused for multiple test executions.

---

### Run Container

```bash
docker run --rm pytest-framework
```

Creates a temporary container from the previously built image.

The container executes:

```bash
uv run pytest --alluredir=/app/allure-results
```

After the tests complete, the container exits and is automatically removed (`--rm`).

---

## Persisting Allure Results

Since Docker containers are ephemeral, the `allure-results` directory would normally be deleted when the container exits.

To preserve the test results, Jenkins mounts a directory from its workspace into the container:

```bash
docker run \
    -v $WORKSPACE/allure-results:/app/allure-results \
    pytest-framework
```

This creates the following mapping:

```text
Jenkins Workspace
-------------------------------
$WORKSPACE/allure-results
          ▲
          │ Mounted Volume
          ▼
Docker Container
-------------------------------
/app/allure-results
```

As pytest generates Allure result files, they are written directly into the Jenkins workspace.

When the container exits, the results remain available for Jenkins to publish.

---

## Allure Reporting

The Jenkins Allure Plugin reads the generated JSON files from:

```
allure-results/
```

and produces an interactive dashboard showing:

- Total tests
- Passed tests
- Failed tests
- Skipped tests
- Execution duration
- Historical trends (when configured)

This provides a centralized view of test execution across CI builds.