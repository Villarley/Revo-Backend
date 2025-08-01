"""
User GraphQL types for Farmers Marketplace.
"""

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Optional
from uuid import UUID

import strawberry

if TYPE_CHECKING:
    from app.models.users.user import User as UserModel


@strawberry.enum
class UserType(Enum):
    """GraphQL enum for user types."""

    FARMER = "FARMER"
    BUYER = "BUYER"
    ADMIN = "ADMIN"


@strawberry.type
class User:
    """GraphQL User type with all fields."""

    id: UUID
    email: str
    user_type: UserType
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_model(cls, user_model: "UserModel") -> "User":
        """Convert SQLAlchemy User model to GraphQL User type."""
        return cls(
            id=user_model.id,
            email=user_model.email,
            user_type=UserType(user_model.user_type.value),
            is_active=user_model.is_active,
            is_verified=user_model.is_verified,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at,
        )


@strawberry.input
class UserInput:
    """GraphQL input type for user creation."""

    email: str
    password: str
    user_type: UserType


@strawberry.input
class UserUpdateInput:
    """GraphQL input type for user updates."""

    email: Optional[str] = None
    user_type: Optional[UserType] = None
