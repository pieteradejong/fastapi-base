from datetime import datetime
from pydantic import BaseModel

"""
Not actual app logic - just an example of what a model might look like.
"""

class Comment(BaseModel):
    title: str
    text: str
    datetime_posted: datetime
    comment_on_post_id: int
