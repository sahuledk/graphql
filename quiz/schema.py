import graphene
from graphene_django import DjangoObjectType
from .models import Quizzes, Question, Answer, Category
from graphene_django import DjangoListField



class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class QuizType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = '__all__'


class Query(graphene.ObjectType):
    # all_quizzes = DjangoListField(QuizType)
    # all_questions = DjangoListField(QuestionType)
    #
    # def resolve_all_quizzes(root, info):
    #     return Quizzes.objects.all()
    # def resolve_all_questions(root, info):
    #     return Question.objects.all()

    # all_quizzes = graphene.Field(QuizType, id=graphene.Int())
    #
    # def resolve_all_quizzes(root, info, id):
    #     return Quizzes.objects.get(pk=id)
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)


# class CategoryMutation(graphene.Mutation):
#
#     class Arguments:
#         name = graphene.String(required=True)
#
#     category =graphene.Field(CategoryType)
#
#     @classmethod
#     def mutate(cls, root, info, name):
#         category = Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)
#
# class Mutation(graphene.ObjectType):
#     update_category = CategoryMutation.Field()
# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()
#         name = graphene.String(required=True)
#
#     category = graphene.Field(CategoryType)
#
#     @classmethod
#     def mutate(cls, root ,info, id, name):
#         category = Category.objects.get(id=id)
#         category.name = name
#         category.save()
#         return CategoryMutation(category=category)
# class Mutation(graphene.ObjectType):
#     update_category = CategoryMutation.Field()

class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()


    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return


class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)