from pydantic import BaseModel, computed_field, field_validator, Field
from typing import Optional, List, Dict, Annotated, Literal

class UserInput(BaseModel):
    id: Annotated[str, Field(..., description="Task ID.")]
    title: Annotated[str, Field(..., description="Task title.")]
    status: Annotated[Literal['pending', 'in-progess','completed','archived'], Field (description="Task status.['pending', 'in-progress', 'completed']", default="pending")]
    description: Annotated[Optional[str], Field(description="Some description about the task.", default=None)]
    
    