from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# def lat_lng_validator(value):
#     #정규표현식을 통해 위도, 경도 포맷 지정
#     if not re.match('(\d+\.?\d*),(\d+/.?\d*)$', value):
#         raise ValidationError('Invalid LatLng Type') #유효성에 맞지 않는 경우 "Invalid LngLat Type" 출력

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(blank=True, null=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(400, 250)])
    #ImageSpecField에서 확장자, 압축 방식도 인자로 지정 가능
    #확장자 format='JPEG'
    #압축 방식 options={'quality':60}
    body = models.TextField()
    lat_lng = models.CharField(blank=True, null=True, max_length=50)
    # lat_lng = models.CharField(blank=True, null=True, max_length=50, validators=[lat_lng_validator], help_text='위도,경도 포맷으로 입력') # 유효성을 검사한다.
    isUpdated = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # def summary(self):
    #     return self.body[:100]