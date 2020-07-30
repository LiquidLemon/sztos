from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Problem, Solution
from .tasks import validate_solution


class ProblemIndexView(generic.ListView):
    template_name = 'judge/index.html'
    context_object_name = 'latest_problem_list'

    def get_queryset(self):
        """Return all published problems."""
        return Problem.objects.order_by('-pub_date')[:]


class ProblemDetailView(generic.DetailView):
    model = Problem
    template_name = 'judge/detail.html'


class ResultsView(generic.DetailView):  # name?
    model = Problem
    template_name = 'judge/results.html'


def send_solution(request, problem_id):
    if request.method == 'POST':
        solution = request.POST['solution']
        problem = get_object_or_404(Problem, pk=problem_id)
        s = Solution(problem=problem, text=solution)
        s.save()
        validate_solution.delay(s.id)
        return HttpResponseRedirect(reverse('judge:results', args=(problem.id,)))
