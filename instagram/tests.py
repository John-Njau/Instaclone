# from django.test import TestCase
# from .models import Image, Comments, Likes, Profile, Follow

# # Create your tests here.
# class ImageTestClass(TestCase):
#     #set up method
#     def setUp(self):
#         '''
#         This set up method runs before any instance is executed
#         '''
#         self.image = Image(image='myimage.jpg', name='myimage', caption='mycaption', likes='0', comments='0', date_uploaded='2019-01-01')
        
#     # tesing instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.image,Image))
        
# #     #test save method
# #     def test_save_method(self):
# #         '''
# #         Test to check the save method execution
# #         '''
# #         self.loc.save_location()
# #         locs = Location.objects.all()
# #         self.assertTrue(len(locs)> 0)
        
# class CategoryTestClass(TestCase):
#     #set up method
#     def setUp(self):
#         '''
#         This set up method runs before any instance is executed
#         '''
#         self.cat = Category(name='nature', description='blissful, serene, and peaceful', category_image='media/category/nature.jpg')
        
# #     # tesing instance
# #     def test_instance(self):
# #         self.assertTrue(isinstance(self.cat,Category))
        
# #     #test save method
# #     def test_save_method(self):
# #         '''
# #         Test to check the save method execution
# #         '''
# #         self.cat.save_category()
# #         categoriess = Category.objects.all()
# #         self.assertTrue(len(categoriess)> 0)
        
        
# # class ImageTestClass(TestCase):
# #     def setUp(self):
# #         ''' 
# #         Creating a new location and saving it
# #         '''
# #         self.loc1 = Location(name = 'Arusha')
# #         self.loc1.save_location()
        
# #         ''' Creating a new category instance and saving it '''
# #         self.cat1 = Category(name='nature', description='blissful, serene, and peaceful', category_image='media/category/nature.jpg')
# #         self.cat1.save_category()
        
# #         ''' Creating a new Image instance '''
# #         self.new_image = Image(name="Test image ", description="This is a random test post", location = self.loc1, category = self.cat1, dated='May 29, 2022, 3:51 p.m.')
# #         self.new_image.save_image()
        
        
# #     def tearDown(self):
# #         '''
# #         This tearDown method does clean up after each test case has run.
# #         '''
# #         Location.objects.all().delete()
# #         Category.objects.all().delete()
# #         Image.objects.all().delete()
        
# #     def test_search_by_name(self):
# #         '''
# #         To test whether the search functionality is implemented properly
# #         '''
# #         searched = Image.search_by_name('Test image')
# #         self.assertTrue(len(searched) > 0)
        

# #running tests
# # python3 manage.py test news
# # ./manage.py tests


from django.test import TestCase

from django.contrib.auth.models import User

from .models import Image, Comments, Likes, Profile, Follow



# Create your tests here.

class UserTestClass(TestCase):

    def setUp(self):
        self.new_user = User.objects.create(
            username = 'john',
            password = 'pass1',
            email = 'johnnjaunjoroge@gmail.com'
        )

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_save_method(self):
        self.new_user.save()
        users = User.objects.all()
        self.assertEquals(len(users),1)

    def test_delete_method(self):
        self.new_user.save()
        test_user = User(username = 'testuser',password='12345678',email='example@gmail.com')
        test_user.save()
        self.new_user.delete()
        users = User.objects.all()
        self.assertEquals(len(users),1)


        


class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(
            username = 'john',
            password = 'pass1',
            email = 'johnnjaunjoroge@gmail.com'
        )

        # saving user to create profile for
        self.new_user.save()

        # profile instance
        self.new_profile = Profile(user = self.new_user,bio = "my bio")


    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))



    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()

        self.assertEquals(len(profiles),1)

    def test_delete_profile(self):
        ''''

        method to test deleteing a profile
        create and save a test profile
        then delete new_profile instance
        '''
        self.test_user = User.objects.create(
            username = 'testuser',
            password = '123456789',
            email = 'example@gmail.com'
        )

        self.test_user.save()

        self.test_profile = Profile(user = self.test_user, bio = "new bio")
        self.test_profile.save_profile()
        self.new_profile.save_profile()

        self.new_profile.delete()

        profiles = Profile.objects.all()

        self.assertEquals(len(profiles),1)


        

# class FollowTestClass(TestCase):
#     def setUp(self):
#         self.john = User.objects.create(
#             username = 'john',
#             password = 'pass1',
#             email = 'johnnjaunjoroge@gmail.com'
#         )


#         self.test = User.objects.create(
#             username = 'test',
#             password = 'test1234',
#             email = 'example@gmail.com'
#         )


#         self.test2 = User.objects.create(
#             username = 'test_user2',
#             password = 'test1234',
#             email = 'example@gmail.com'
#         )


#         self.john.save()
#         self.test.save()
#         self.test2.save()

#     def test_instance(self):
#         self.follow = Follow(user_am_following = self.john,user_following_me = self.test)
#         self.assertTrue(isinstance(self.follow,Follow))

    
#     def test_follow(self):
#         self.follow = Follow(user_am_following = self.john,user_following_me = self.test)
#         self.follow.follow()

#         follow_objects = Follow.objects.all()

#         self.assertEquals(follow_objects,1)