from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ResumeView(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class DeleteResume(generics.DestroyAPIView):
    authentication_classes = []
    queryset = Links.objects.all()
    serializer_class = ResumeSerializer


class ProfileView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class DetailProfile(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Profile.objects.filter(owner=self.request.user)


# class DetailProfile(generics.RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer


class CreateLinks(generics.CreateAPIView):
    queryset = Links.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListLinks(generics.ListAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Links.objects.all()

    def get_queryset(self):
        return Links.objects.filter(owner=self.request.user)


class GetLinks(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Links.objects.all()
    serializer_class = LinkSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Links.objects.filter(owner=self.request.user)


class CreateWorkExperience(generics.CreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class UpdateWorkExperience(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return WorkExperience.objects.filter(owner=self.request.user)


class CreateEducationalHistory(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class UpdateEducationHistory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return WorkExperience.objects.filter(owner=self.request.user)


class CreateAwards(generics.CreateAPIView):
    queryset = Awards.objects.all()
    serializer_class = AwardSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListAwards(generics.ListAPIView):
    serializer_class = AwardSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Awards.objects.all()

    def get_queryset(self):
        return Awards.objects.filter(owner=self.request.user)


class UpdateAwards(generics.RetrieveUpdateDestroyAPIView):
    queryset = Awards.objects.all()
    serializer_class = AwardSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Awards.objects.filter(owner=self.request.user)


class CreateCertificate(generics.CreateAPIView):
    queryset = Certifications.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListCertificate(generics.ListAPIView):
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Certifications.objects.all()

    def get_queryset(self):
        return Certifications.objects.filter(owner=self.request.user)


class UpdateCertificates(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certifications.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Certifications.objects.filter(owner=self.request.user)


class CreatePublication(generics.CreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListPublication(generics.ListAPIView):
    serializer_class = PublicationSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Publication.objects.all()

    def get_queryset(self):
        return Publication.objects.filter(owner=self.request.user)


class UpdatePublication(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Publication.objects.filter(owner=self.request.user)


class CreateSkills(generics.CreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListSkill(generics.ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Skills.objects.all()

    def get_queryset(self):
        return Skills.objects.filter(owner=self.request.user)


class UpdateSkill(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Skills.objects.filter(owner=self.request.user)


class CreateLanguage(generics.CreateAPIView):
    queryset = Languages.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListLanguage(generics.ListAPIView):
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Languages.objects.all()

    def get_queryset(self):
        return Languages.objects.filter(owner=self.request.user)


class UpdateLanguage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Languages.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Languages.objects.filter(owner=self.request.user)


class CreateInterest(generics.CreateAPIView):
    queryset = Interests.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListInterest(generics.ListAPIView):
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Interests.objects.all()

    def get_queryset(self):
        return Interests.objects.filter(owner=self.request.user)


class UpdateInterest(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interests.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Interests.objects.filter(owner=self.request.user)


class CreateVolunteerView(generics.CreateAPIView):
    queryset = VolunteerExperience.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListVolunteerView(generics.ListAPIView):
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = VolunteerExperience.objects.all()

    def get_queryset(self):
        return VolunteerExperience.objects.filter(owner=self.request.user)


class UpdateVolunteerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerExperience.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return VolunteerExperience.objects.filter(owner=self.request.user)


class CreateProjectView(generics.CreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListProjects(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Projects.objects.all()

    def get_queryset(self):
        return Projects.objects.filter(owner=self.request.user)


class UpdateProjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Projects.objects.filter(owner=self.request.user)


class CreateReferenceView(generics.CreateAPIView):
    queryset = References.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ListReference(generics.ListAPIView):
    serializer_class = ReferenceSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = References.objects.all()

    def get_queryset(self):
        return References.objects.filter(owner=self.request.user)


class UpdateReference(generics.RetrieveUpdateDestroyAPIView):
    queryset = References.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return References.objects.filter(owner=self.request.user)
