from rest_framework import serializers
from .models import question_topic, question_type, question_complexity, app_question, question_choices



# Serializers define the API representation.



class Question_topicSerializer(serializers.ModelSerializer):
    class Meta:
        model = question_topic
        fields = ('id','name','acronym','status')

class Question_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = question_type
        fields = '__all__'


class Question_complexSerializer(serializers.ModelSerializer):
    class Meta:
        model = question_complexity
        fields = '__all__'


class Add_questionSerializer(serializers.HyperlinkedModelSerializer):
    questiontype_name = serializers.CharField(source='questiontype.name', read_only=True)
    questioncomplexity_name = serializers.CharField(source='questioncomplexity.name', read_only=True)
    questiontopic_name = serializers.CharField(source='questiontopic.name', read_only=True)

    class Meta:
        model = app_question
        fields = ('id','description','questiontype_name', 'questioncomplexity_name', 'questiontopic_name','image','status')
    

class Choice_questionSerializer(serializers.HyperlinkedModelSerializer):
    # question_id_description = serializers.CharField(source='question_id.description',read_only=False)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = question_choices
        fields = ('id','name','question_id','status')
    
    read_only_fields = ('question_id',)


class Add_questionSerializertwo(serializers.ModelSerializer):
    
    choices = Choice_questionSerializer(many=True, required=False)
    class Meta:
        model = app_question
        fields = ('id','description','questiontype', 'questioncomplexity', 'questiontopic','image','status','choices')
    
    def create(self,validated_data):
        choices = validated_data.pop('choices')
        question = app_question.objects.create(**validated_data)
        for choice in choices:
             question_choices.objects.create(question_id=question, **choice)
        return question
    ###############################################################################################################################
    # def create(self,validated_data):
    #     questiontype_name = validated_data.pop('questiontype')
    #     questioncomplexity = validated_data.pop('questioncomplexity')
    #     questiontopic = validated_data.pop('questiontopic')
    #     questiontype_instance = question_type.objects.get(id=questiontype)
    #     questioncomplexity_instance = question_type.objects.get(id=questioncomplexity)
    #     questiontopic_instance = question_type.objects.get(id=questiontopic)
    #     question = app_question.objects.create(**validated_data)
    #     return question
    # questiontype = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # questioncomplexity = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # questiontopic = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # def create(self,validated_data):
    #     typename = validated_data.pop('questiontype')
    #     complexname = validated_data.pop('questioncomplexity')  
    #     topicname = validated_data.pop('questiontopic')
    #     typename_instance, created = question_type.objects.get(name=typename)
    #     complexname_instance, created = question_complexity.objects.get(name=complexname)
    #     topicname_instance, created = question_topic.objects.get(name=topicname)
    #     appquestion = app_question.objects.create(questiontype=typename_instance,questioncomplexity=complexname_instance,questiontopic=topicname_instance,**validated_data)
    #     # appquestion.questiontype.set(typename_instance)
    #     # appquestion.questioncomplexity.set(complexname_instance)
    #     # appquestion.questiontopic.set(topicname_instance)
    #     # appquestion.save()
    #     # try:
    #     #     appquestion.questiontype = question_type.objects.get(name=typename,)
    #     # except question_type.DoesNotExist:
    #     #     pass
    #     # try:
    #     #     appquestion.questioncomplexity = question_complexity.objects.get(name=complexname)
    #     # except question_complexity.DoesNotExist:
    #     #     pass
    #     # try:
    #     #     appquestion.questiontopic = question_topic.objects.get(name=topicname)
    #     # except question_topic.DoesNotExist:
    #     #     pass
    #     return appquestion

