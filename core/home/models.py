from django.db import models
import uuid
import os

class Folder(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


def get_uploaded_path(instace, filename):
    return os.path.join(str(instace.folder.uid), filename)


class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_uploaded_path)
    create_at = models.DateField(auto_now=True)
