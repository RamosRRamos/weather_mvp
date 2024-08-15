"""
Model definitions with common fields for timestamping and unique UUID primary keys.

Classes:
    IndexedTimeStampedModel - Abstract base model with auto-created and auto-modified timestamp fields.
    AbstractBaseModel - Extends IndexedTimeStampedModel to include a UUID primary key.
"""

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class IndexedTimeStampedModel(models.Model):
    """
    Abstract base class model that provides self-managed "created" and
    "modified" fields, which are indexed in the database for optimized querying.
    """

    created = AutoCreatedField(_("created"), db_index=True)
    modified = AutoLastModifiedField(_("modified"), db_index=True)

    class Meta:
        abstract = True


class AbstractBaseModel(IndexedTimeStampedModel):
    """
    Abstract base class model that provides a UUID primary key along with
    "created" and "modified" fields from IndexedTimeStampedModel.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
