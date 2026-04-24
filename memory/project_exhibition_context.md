---
name: Exhibition context and post-exhibition roadmap
description: Year-end exhibition deadline driving stability decisions; multi-user support deferred
type: project
---

AURA>ego is targeting a year-end exhibition as its hard deadline. Stability of the single-user experience takes priority over new features.

**Why:** Live exhibition environment — reliability and low latency matter more than feature completeness.

**How to apply:** When suggesting changes or features, flag anything that could destabilise the session loop, camera feed, or p5 render performance. Defer exploratory work (multi-user, new APIs) until post-exhibition.

Post-exhibition backlog item noted by user:
- Multi-person pose tracking via `@mediapipe/tasks-vision` `PoseLandmarker` (requires full migration: new script imports, new init pattern, `result.landmarks[i]` loop, updated coM/smI/pLMs/debug drawing, pose matching loop)
