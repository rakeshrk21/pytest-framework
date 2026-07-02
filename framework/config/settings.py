import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    raise RuntimeError("BASE_URL is not set")


"""

                Local Development
             -----------------------
.env  ─────► load_dotenv()
                  │
                  ▼
          Environment Variables
                  │
                  ▼
             os.getenv()

                Jenkins
             -----------------------
Jenkins Env Vars ───────────────► os.getenv()

                Docker
             -----------------------
docker run -e BASE_URL=... ────► os.getenv()

              Kubernetes
             -----------------------
ConfigMap / Secret ────────────► os.getenv()

"""