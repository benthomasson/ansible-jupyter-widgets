from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        var_name = self._task.args.get('var_name', None)
        description = self._task.args.get('description', var_name)
        if var_name is None:
            raise Exception("'var_name' is a required argument")
        result['application/x-python'] = """import ansible_jupyter_widgets
{0} = ansible_jupyter_widgets.Password(var_name='{0}', description='{1}')
display({0})""".format(var_name, description)
        return result
