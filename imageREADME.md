Adding Photo Capability to Django (Updated):




Install the Pillow Library:
pip install pillow


Create forms.py file in the same directory as admin.py, models.py. urls.py etc… and add:
from django.forms import ModelForm
from apps.public.models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image


Add this to the Views.Py:
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.core import serializers
from apps.public.forms import ImageForm # make sure the route to this form is correct
from .models import *

# to post new images
def uploadedimages(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('image upload success')
        else:
            return HttpResponseBadRequest(form.errors)
    return HttpResponseForbidden('allowed only via POST')

# to retrive a single profile image
def profile_image(request):
    if request.method == 'GET':
        requested_by = request.GET.get('user_id')
        profileimg = Image.objects.get(user_id=requested_by, is_profile_image=True)
        return HttpResponse(serializers.serialize('json', [profileimg,]))

Add this to URLs.py:
# to post new images
url(r'^uploadedimages$', 'views.uploadedimages', name="uploadedimages”),
# to retrieve a single profile image
url(r'^profile-image$', 'views.profile_image', name="profile-images"),


Add this to models.py:
class Image(models.Model):
    user = models.ForeignKey(User)
    is_profile_image = models.BooleanField(default=0)
    is_todo_image = models.BooleanField(default=0)
    photos = models.ImageField(upload_to='img/uploaded', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s, %s' % (self.user, self.is_profile_image)

    class Meta:
        verbose_name_plural = 'Image'

Add this to Admin.py
from .models import *
admin.site.register(Image)


Add this to your Dev.py (some of this may already be there) and possibly the equivalent production settings file (ex: base.py, prod.py):
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'


Add this to your controllers:
// make sure that ‘SessionService’, ‘$http’, and ‘$window' is being called as part of the controllers parameters

var current_user = SessionService.getUserSession();

// this section is used to retrieve a profile image
 $http.get('profile-image', {
            params: {user_id: current_user.user_id }
        }).success(function (data) {
                  $scope.profile_image = '/media/'+data[0].fields.photos;
        });


// this section is used to post a profile image

        $scope.uploadFile = function (files) {
            $scope.photos = files[0];
        };

        $scope.save = function () {
            var fd = new FormData();
            fd.append("photos", $scope.photos);
            fd.append("user", current_user.user_id); // check session service to be sure that this is the correct routing for user id
            fd.append("is_profile_image", true);
            fd.append("is_todo_image", false);

            $http.post('http://localhost:8001/uploadedimages', fd, {
                //            $http.post('http://vast-journey-8108.herokuapp.com/location', fd, {
                withCredentials: true,
                headers: {'Content-Type': undefined },
                transformRequest: angular.identity
            }).success(function (response) {
                    $window.location = 'my-account';
                }).error(function (response) {
                    console.log('Response: ' + response);
                });
        };

Add this to your .html file, form or wherever you want a user to upload an image:
<!— to see a previously uploaded image —>
<img class="img-responsive" src="{{ profile_image }}" alt=“">

<!— to upload a new image —>
<form ng-submit="save()" enctype="multipart/form-data" class="form-register">
            <label>Upload a profile picture
       <input type="file" ng-model="photos" onchange="angular.element(this).scope().uploadFile(this.files)"/></label>
            <br/>
            <br/>
            <button type="submit" class="btn btn-success" value="Save">Update My Account</button>
</form>
