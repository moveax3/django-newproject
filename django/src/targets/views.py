import logging
from django.views.generic import ListView, DetailView
from .models import Target

logger = logging.getLogger('default')

class TargetsDetailView(DetailView):
    model = Target

    def get_object(self, queryset=None):
        object = super(TargetsDetailView, self).get_object()
        return object

class TargetsListView(ListView):
    model = Target
    template_name = "targets/target_list.html"

    """
    #Изменяет список задач, рекурсивно вкладывая дочерние внутрь родительских
    def get_queryset(self):
        def form_subtargets(root_targets):
            for root_target in root_targets:
                subtargets = list(Target.objects.filter(parent=root_target))
                if len(subtargets) > 0:
                    print(type(subtargets))
                    root_target.subtargets = form_subtargets(subtargets)
            return root_targets

        root_targets = list(Target.objects.filter(parent=None))
        print(root_targets)
        root_targets = form_subtargets(root_targets)
        print(root_targets)
        print(root_targets[0].subtargets)
        return root_targets
    """
