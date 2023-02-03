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
            'id', 'Image', 'Full_Name', 'Date', 'email', 'Phone', 'Gender', 'Description', 'Summary', 'Address', 'City',
            'Region', 'Country', 'Postal')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ('id', 'Title', 'Website')


class WorkExperienceSerializer(serializers.ModelSerializer):
    present = models.BooleanField(default=False)

    class Meta:
        model = WorkExperience
        fields = ('id', 'Title', 'Position', 'Employer', 'Url', 'StartDate', 'EndDate', 'Website', 'Summary', 'present')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            'id', 'Institute', 'Degree', 'School', 'URL', 'City', 'Country', 'StartDate', 'EndDate', 'Description')


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = ('id', 'Title', 'Issuer', 'URL', 'Date', 'Description')


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
        fields = ('id', 'Name', 'Level', 'SubSkill')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = ('id', 'Name', 'Level')


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = ('id', 'Name')


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerExperience
        fields = ('id', 'Organization', 'Position', 'StartDate', 'EndDate', 'URL', 'Summary')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'Name', 'Description', 'URL')


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = References
        fields = ('id', 'Name', 'Relationship', 'Phone',)


# Cover Letter Serializers
class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = ('id', 'first_name', 'last_name', 'address', 'email', 'image', 'postal', 'city')


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


class SituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurSituation
        fields = ('id', 'text', 'position', 'organization', 'city', 'responsibility', 'education', 'school')


class MotivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivation
        fields = ('id', 'text', 'position', 'organization', 'city', 'responsibility', 'personal_description')


class ClosingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Closing
        fields = ('id', 'text', 'position', 'email', 'Phone', 'first_name', 'last_name')
