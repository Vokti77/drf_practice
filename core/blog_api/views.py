from rest_framework import generics
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from blog.models import Post
from blog_api.serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, IsAuthenticated, BasePermission, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authentication import TokenAuthentication

class PostUserWritePermission(BasePermission):
    message = 'Editnig post is restricted to the Author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.postobjects.all()

    def list(self, request):
        serializer_class = PostSerializer(self.queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PostSerializer(post)
        return Response(serializer_class.data)
    

    def create(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk=None):
        qs = Post.objects.get(pk=pk)
        serializer = PostSerializer(qs, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PostList(generics.ListCreateAPIView):
#     permission_classes = []
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer



# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer