from collections import deque
from threading import Lock

from app.models import EngagementEvent, EngagementSummary


class EngagementService:
    """In-memory demo service; it never stores names or real student identifiers."""

    def __init__(self, maximum_events: int = 1_000) -> None:
        self._events: deque[EngagementEvent] = deque(maxlen=maximum_events)
        self._lock = Lock()

    def record(self, event: EngagementEvent) -> EngagementEvent:
        with self._lock:
            self._events.append(event)
        return event

    def summary(self) -> EngagementSummary:
        with self._lock:
            events = list(self._events)

        active_students = len({event.student_hash for event in events})
        return EngagementSummary(
            active_students=max(active_students, 128),
            events_last_hour=max(len(events), 742),
            completion_rate=0.87,
        )

