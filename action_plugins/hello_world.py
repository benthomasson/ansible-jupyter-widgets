from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        var_name = self._task.args.get('var_name', None)
        result['application/x-python'] = """import jupyter_widget_example
{0} = jupyter_widget_example.HelloWorld()
display({0})""".format(var_name)
        return result
