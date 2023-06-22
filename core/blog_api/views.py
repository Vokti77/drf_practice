from rest_framework import generics
from blog.models import Post
from blog_api.serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, IsAuthenticated, BasePermission, DjangoModelPermissionsOrAnonReadOnly


class PostUserWritePermission(BasePermission):
    message = 'Editnig post is restricted to the Author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer



class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer