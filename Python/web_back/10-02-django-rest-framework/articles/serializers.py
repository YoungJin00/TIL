from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

# 읽기 전용 필드
# 데이터를 전송하는 시점에 " 유효성 검사에서 제외" 시키고,
# 데이터 조회 시에는 출력 하는 필드
class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # override
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # 읽기 전용 필드
        # 데이터를 전송하는 시점에 " 유효성 검사에서 제외" 시키고,
        # 데이터 조회 시에는 출력 하는 필드
        # read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source = 'comment_set.count', read_only = True)
    class Meta:
        model = Article
        fields = '__all__'
