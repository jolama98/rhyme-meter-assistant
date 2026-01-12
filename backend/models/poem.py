from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Poem:
    """Represents a poem in our system"""
    id: Optional[int] = None
    title: str = ""
    content: str = ""
    form_type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def to_dict(self):
        """Convert poem to dictionary for JSON responses"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'formType': self.form_type,
            'createdAt': self.created_at.isoformat() if self.created_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @staticmethod
    def from_dict(data):
        """Create Poem from dictionary (from frontend)"""
        return Poem(
            id=data.get('id'),
            title=data.get('title', ''),
            content=data.get('content', ''),
            form_type=data.get('formType')
        )
