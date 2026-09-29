"""Structured reports for worker bots — JSON + markdown, no personality."""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class Report:
    bot: str
    verb: str
    ok: bool
    generated: str = field(default_factory=_utc_now)
    findings: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    data: dict[str, Any] = field(default_factory=dict)
    residuals: list[str] = field(default_factory=list)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(asdict(self), indent=indent, ensure_ascii=False)

    def to_markdown(self) -> str:
        lines = [
            f"# {self.bot.upper()} — {self.verb}",
            "",
            f"- generated: `{self.generated}`",
            f"- ok: **{self.ok}**",
            "",
        ]
        if self.data:
            lines.append("## Data")
            for k, v in self.data.items():
                if isinstance(v, (list, dict)):
                    lines.append(f"- **{k}:**")
                    lines.append(f"  ```")
                    lines.append(f"  {json.dumps(v, ensure_ascii=False, indent=2)}")
                    lines.append(f"  ```")
                else:
                    lines.append(f"- **{k}:** {v}")
            lines.append("")
        if self.warnings:
            lines.append("## Warnings")
            for w in self.warnings:
                lines.append(f"- {w}")
            lines.append("")
        if self.findings:
            lines.append("## Findings")
            for f in self.findings:
                lines.append(f"- {f}")
            lines.append("")
        if self.residuals:
            lines.append("## Residuals")
            for r in self.residuals:
                lines.append(f"- {r}")
            lines.append("")
        return "\n".join(lines)
