from st2common.runners.base_action import Action

class MyEchoAction(Action):
  def run(self, message):
    output = u''.join(message).encode('utf-8').strip()

    return (True, output)
