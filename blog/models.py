from django.conf import settings
from django.db import models
from django.utils import timezone

# モデルを定義することで、Djangoはデータベースに保存すべきものが分かる

# オブジェクト:Post

# プロパティ: author, title, text, created_date, published_date
# フィールドタイプ: models.ForeignKeyなど 各プロパティ指定されている

# メソッド: publish()

# 新しいモデルを作ったら移行ファイルを作成 (makemigrations)
# 移行ファイルをデータベースに追加 (migrate)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title