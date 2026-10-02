from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import EvaluationCase
from .eval_service import EvaluationService

class EvaluationRunView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request, case_id):
        try: case=EvaluationCase.objects.get(pk=case_id)
        except EvaluationCase.DoesNotExist: return Response({'detail':'evaluation case not found'},status=404)
        run=EvaluationService().run_case(case, request.user)
        return Response({'id':run.id,'score':run.score,'passed':run.passed,'feedback':run.feedback},status=201)
