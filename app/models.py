from datetime import UTC, datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class EngagementType(StrEnum):
    LOGIN = "login"
    ASSIGNMENT_SUBMITTED = "assignment_submitted"
    COURSE_VIEWED = "course_viewed"


class EngagementEvent(BaseModel):
    student_hash: str = Field(min_length=8, max_length=64)
    course_id: str = Field(pattern=r"^[A-Z]{2,8}-\d{3,5}$")
    event_type: EngagementType
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class EngagementSummary(BaseModel):
    active_students: int
    events_last_hour: int
    completion_rate: float
    source: str = "synthetic-demo-data"

