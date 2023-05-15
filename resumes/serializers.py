from rest_framework import serializers
from .models import *


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateResume
        fields = ('name', 'slug')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'image', 'fullname', 'email', 'gender', 'description', 'summary', 'address', 'city',
            'region', 'country', 'postal')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ('id', 'title', 'website')


class WorkExperienceSerializer(serializers.ModelSerializer):
    present = models.BooleanField(default=False)

    class Meta:
        model = WorkExperience
        fields = ('id', 'title', 'position', 'employer', 'url', 'startDate', 'endDate', 'website', 'summary', 'present')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            'id', 'institute', 'degree', 'school', 'url', 'city', 'country', 'startDate', 'endDate', 'description')


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = ('id', 'title', 'issuer', 'url', 'date', 'description')


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certifications
        fields = ('id', 'certificate', 'Issuer', 'URL', 'Description')


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'Title', 'Name', 'URL', 'Date', 'Description')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('id', 'name', 'level', 'subSkill')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = ('id', 'Name', 'Level')


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = ('id', 'name')


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerExperience
        fields = ('id', 'Organization', 'Position', 'StartDate', 'EndDate', 'URL', 'Summary')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'name', 'description', 'url')


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = References
        fields = ('id', 'name', 'relationship',)


# Cover Letter Serializers
class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = ('id', 'first_name', 'last_name', 'address', 'email', 'postal', 'city')


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipientInfo
        fields = ('id', 'contact_person', 'organization', 'address', 'postal', 'city')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateSubject
        fields = ('id', 'date', 'application_model', 'position')


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = ('id', 'text', 'person', 'position', 'organization', 'magazine', 'website_name')




