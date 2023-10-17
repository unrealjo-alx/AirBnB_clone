#!/usr/bin/python3
"""
Reload the stored objects
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
