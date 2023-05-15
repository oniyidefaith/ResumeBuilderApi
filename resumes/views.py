from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ResumeView(generics.CreateAPIView):
    """This view allows you to create resume name"""
    serializer_class = ResumeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class DeleteResume(generics.DestroyAPIView):
    """This view allows you to Delete an entire resume  """
    authentication_classes = []
    queryset = Links.objects.all()
    serializer_class = ResumeSerializer


class ProfileView(generics.CreateAPIView):
    """" This endpoint allows users to create the profile section in a resume """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class DetailProfile(generics.RetrieveUpdateAPIView):
    """This endpoint allows you to edit or put, get, update the profile """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Profile.objects.filter(owner=self.request.user)


class CreateLinks(generics.CreateAPIView):
    """This endpoint allows users to create their various links or urls section to their resume"""
    queryset = Links.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListLinks(generics.ListAPIView):
    """This endpoint allows the users to have a list of their links added to the resume application"""
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Links.objects.all()

    def get_queryset(self):
        return Links.objects.filter(owner=self.request.user)


class GetLinks(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get , update , and delete any link
    """
    permission_classes = (IsAuthenticated,)
    queryset = Links.objects.all()
    serializer_class = LinkSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Links.objects.filter(owner=self.request.user)


class CreateWorkExperience(generics.CreateAPIView):
    """
    This endpoint allow users to create work experience
    """
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class UpdateWorkExperience(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update user work experiences
    """
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return WorkExperience.objects.filter(owner=self.request.user)


class CreateEducationalHistory(generics.CreateAPIView):
    """
    This endpoint allow users to create their educational history
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class UpdateEducationHistory(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update user educational history
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return WorkExperience.objects.filter(owner=self.request.user)


class CreateAwards(generics.CreateAPIView):
    """
    This endpoint allows you to create awards for your resume
    """
    queryset = Awards.objects.all()
    serializer_class = AwardSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListAwards(generics.ListAPIView):
    """
    This endpoint allows you to get a list of your created awards
    """
    serializer_class = AwardSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Awards.objects.all()

    def get_queryset(self):
        return Awards.objects.filter(owner=self.request.user)


class UpdateAwards(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update user awards
    """
    queryset = Awards.objects.all()
    serializer_class = AwardSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Awards.objects.filter(owner=self.request.user)


class CreateCertificate(generics.CreateAPIView):
    """
    This endpoint allows users to create their own certificate
    """
    queryset = Certifications.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListCertificate(generics.ListAPIView):
    """
    This endpoint allows you to get a list of your created certificate
    """
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Certifications.objects.all()

    def get_queryset(self):
        return Certifications.objects.filter(owner=self.request.user)


class UpdateCertificates(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update user awards
    """
    queryset = Certifications.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Certifications.objects.filter(owner=self.request.user)


class CreatePublication(generics.CreateAPIView):
    """
    This endpoint allows users to create publications
    """
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListPublication(generics.ListAPIView):
    """
    This endpoint allows you to get a list of created publications
    """
    serializer_class = PublicationSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Publication.objects.all()

    def get_queryset(self):
        return Publication.objects.filter(owner=self.request.user)


class UpdatePublication(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update user publication
    """
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Publication.objects.filter(owner=self.request.user)


class CreateSkills(generics.CreateAPIView):
    """
    This endpoint allows users to create or skill sets
    """
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListSkill(generics.ListAPIView):
    """
    This endpoint allows you to get a list of created skills
    """
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Skills.objects.all()

    def get_queryset(self):
        return Skills.objects.filter(owner=self.request.user)


class UpdateSkill(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update user skills
    """
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Skills.objects.filter(owner=self.request.user)


class CreateLanguage(generics.CreateAPIView):
    """
    This endpoint allows users to create or sets of languages they understand
    """
    queryset = Languages.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListLanguage(generics.ListAPIView):
    """
    This endpoint allows you to get a list of created Languages
    """
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Languages.objects.all()

    def get_queryset(self):
        return Languages.objects.filter(owner=self.request.user)


class UpdateLanguage(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update a set of user languages
    """
    queryset = Languages.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Languages.objects.filter(owner=self.request.user)


class CreateInterest(generics.CreateAPIView):
    """
    This endpoint allows users to include set of their interests
    """
    queryset = Interests.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListInterest(generics.ListAPIView):
    """
    This endpoint allows you to get a list of users interest
    """
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Interests.objects.all()

    def get_queryset(self):
        return Interests.objects.filter(owner=self.request.user)


class UpdateInterest(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update a set of users interest
    """
    queryset = Interests.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Interests.objects.filter(owner=self.request.user)


class CreateVolunteerView(generics.CreateAPIView):
    """
    This endpoint allows users to create set of volunteer experience
    """
    queryset = VolunteerExperience.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListVolunteerView(generics.ListAPIView):
    """
    This endpoint allows you to get a list of users volunteer experience
    """
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = VolunteerExperience.objects.all()

    def get_queryset(self):
        return VolunteerExperience.objects.filter(owner=self.request.user)


class UpdateVolunteerView(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update a set of users interest
    """
    queryset = VolunteerExperience.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return VolunteerExperience.objects.filter(owner=self.request.user)


class CreateProjectView(generics.CreateAPIView):
    """
    This endpoint allows users to create set of their completed projects
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListProjects(generics.ListAPIView):
    """
    This endpoint allows you to get a list of users project
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Projects.objects.all()

    def get_queryset(self):
        return Projects.objects.filter(owner=self.request.user)


class UpdateProjectView(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update a set of projects
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Projects.objects.filter(owner=self.request.user)


class CreateReferenceView(generics.CreateAPIView):
    """
    This endpoint allows users to create set of references they have
    """
    queryset = References.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListReference(generics.ListAPIView):
    """
    This endpoint allows you to get a list of references the users have
    """
    serializer_class = ReferenceSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = References.objects.all()

    def get_queryset(self):
        return References.objects.filter(owner=self.request.user)


class UpdateReference(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update a specific preference
    """
    queryset = References.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return References.objects.filter(owner=self.request.user)


# cover letter views

class PersonalDetailsView(generics.CreateAPIView):
    """
    This endpoint allows users to create their personal details in the cover letter
    """
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailSerializer
    # permission_classes = [IsAuthenticated, ]
    lookup_field = "id"

    def get_queryset(self):
        return PersonalDetails.objects.filter(owner=self.request.user)


class UpdatePersonalDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update their personal details
    """
    queryset = References.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return References.objects.filter(owner=self.request.user)


class RecipientView(generics.CreateAPIView):
    """
    This endpoint allows users to create the recipient to their cover letter
    """
    queryset = RecipientInfo
    serializer_class = ReferenceSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_field = "id"

    def get_queryset(self):
        return RecipientInfo.objects.filter(owner=self.request.user)


class UpdateRecipientView(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update their recipient details
    """
    queryset = RecipientInfo.objects.all()
    serializer_class = RecipientSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return RecipientInfo.objects.filter(owner=self.request.user)


class SubjectView(generics.CreateAPIView):
    """
    This endpoint allows users to create the Subject to their cover letter
    """
    queryset = DateSubject
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_field = "id"

    def get_queryset(self):
        return DateSubject.objects.filter(owner=self.request.user)


class UpdateSubjectView(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update their subject details
    """
    queryset = DateSubject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return DateSubject.objects.filter(owner=self.request.user)


class IntroductionView(generics.CreateAPIView):
    """
    This endpoint allows users to create the introduction to their cover letter
    """
    queryset = Introduction
    serializer_class = IntroductionSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_field = "id"

    def get_queryset(self):
        return Introduction.objects.filter(owner=self.request.user)


class UpdateIntroductionView(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to get, delete,and update their introduction details
    """
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Introduction.objects.filter(owner=self.request.user)


