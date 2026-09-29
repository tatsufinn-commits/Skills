"""Registry / catalog health when TOOL_REGISTRY exists."""

from __future__ import annotations

import json

from shared.report import Report
from shared.paths import RepoPaths


def run_registry_doctor(repo: RepoPaths | None = None) -> Report:
    repo = repo or RepoPaths()
    reg = repo.join("tools/TOOL_REGISTRY.json")
    if not reg.is_file():
        return Report(
            bot="housekeeper",
            verb="registry-doctor",
            ok=True,
            residuals=["tools/TOOL_REGISTRY.json ABSENT"],
            data={"registry_present": False},
        )
    try:
        payload = json.loads(reg.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return Report(
            bot="housekeeper",
            verb="registry-doctor",
            ok=False,
            findings=[f"TOOL_REGISTRY.json invalid JSON: {e}"],
            data={"registry_present": True},
        )

    tools = payload.get("tools") if isinstance(payload, dict) else payload
    count = len(tools) if isinstance(tools, list) else (
        len(payload) if isinstance(payload, dict) else 0
    )
    return Report(
        bot="housekeeper",
        verb="registry-doctor",
        ok=True,
        data={"registry_present": True, "tool_count_estimate": count},
    )
