from django.test import TestCase
from .models import Profile,Neighbourhood,Business
from django.contrib.auth.models import User
# Create your tests here.


class UserTest(TestCase):
    def setUp(self):
        self.user=User(username='asumanibrighton',first_name='brighton',last_name='asumani',email='asumanibrighton@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    def test_data(self):
        self.assertTrue(self.user.username,"asumani")
        self.assertTrue(self.user.first_name,"brighton")
        self.assertTrue(self.user.last_name,'asumani')
        self.assertTrue(self.user.email,'asumanibrighton@gmail.com')

    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)

    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)==0)




class NeighbourhoodTest(TestCase):
    def setUp(self):
        self.user=User(username='asumanibrighton',first_name='brighton',last_name='asumani',email='asumanibrighton@gmail.com')
        self.user.save()
        self.new_Neighbourhood=Neighbourhood( Occupants_count="6",name='Moringa',location='Kenya')
        self.new_Neighbourhood = Neighbourhood( Occupants_count="6",name='Moringa',location='Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_Neighbourhood,Neighbourhood))

    def test_data(self):
        self.assertTrue(self.new_Neighbourhood.location,'Kenya')

    def test_save(self):
        self.new_Neighbourhood.save()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete(self):
        hood = Neighbourhood.objects.filter(id=1)
        hood.delete()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

    def test_update_post(self):
        self.new_Neighbourhood.save()
        self.update_Neighbourhood = Neighbourhood.objects.filter(name='Moringa').update(name='kawangware')
        self.updated_Neighbourhood = Neighbourhood.objects.get(name='kawangware')
        self.assertTrue(self.updated_Neighbourhood.name,'kawangware')




class ProfileTest(TestCase):
    def setUp(self):
        self.new_profile=Profile(name ="brighton",bio='this is my bio',location="Kenya",picture="https://www.google.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_data(self):
        self.assertTrue(self.new_profile.bio,"this is my bio")
        self.assertTrue(self.new_profile.name,"brighton")
        self.assertTrue(self.new_profile.location,"Kenya")
        self.assertTrue(self.new_profile.picture,"https://www.google.com")

    def test_save(self):
        self.new_profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete(self):
        profile = Profile.objects.filter(id=1)
        profile.delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)


    def test_edit_profile(self):
        self.new_profile.save()
        self.update_profile = Profile.objects.filter(bio='this is my bio').update(bio = 'this is my bio')
        self.updated_profile = Profile.objects.get(bio='this is my bio')
        self.assertTrue(self.updated_profile.bio,'this is my bio')
