"""JSON lines adapter; policy output is always a list of current offer IDs."""
import json
import sys
from policy import Policy

policy = None
for line in sys.stdin:
    request = json.loads(line)
    if request["type"] == "reset":
        policy = Policy(request["config"])
        response = {"ready": True}
    else:
        response = {"chosen": policy.choose(request["observation"])}
    print(json.dumps(response, allow_nan=False, separators=(",", ":")), flush=True)
