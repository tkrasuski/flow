import datetime
import logger

logger = logger.logger

class TaskException(Exception):
   def __init__(self, message, errors):
      logger.error(message+' :'+errors)
      super(TaskException, self).__init__(message, errors)
      self.errors = errors

'''
    task states
'''
states = ['pending', 'started', 'aborted','completed', 'waiting', 'error']
types = ['task','subprocess','start','end', 'automatic', 'event']

'''
    params is  dictionary in given format
    state_ - state of the task
    type_ - type of task 
    fields_  - dictionary of fields with values
    code_ - string with python code manipulating on fields
    started_ - datetime value of start moment
    completed_ -  if task is not completed it's None, else datetime of completion
'''
class BaseTask():
   def __init__(self, params):
        '''
            initialize class and sets all params 
        '''
        self.initializeTime = datetime.datetime.now() # time of class initialization
        self.isReady_=False # is the item done or not 
        self.waitTime_ = None # date time until which item waits to run
        self.started_ = None # when item was started date time
        self.completed_ = None # when item was completed date time
        
        
        # lets check if params has proper fields
        if isinstance(params, dict):
            error = ''
            # validating params 
            if 'state_' in params:
                self.state_=params['state_']
                if  not self.state_ in states:
                    raise  TaskException('Params validation error','state_  must be one of  %s ' %states)
            if 'type_' in params:
                self.type_ = params['type_']
                if not self.type_ in types:
                    raise  TaskException('Params validation error','type_  must be one of  %s ' %types)
            if 'code_' in params:
                self.code_=params['code_']
            if  'fields_' in params:
                self.fields_= params['fields_']
            if not 'state_' in params or not 'type_' in params:
                print params
                raise  TaskException('Params validation error','state_ and type_ are required')
            if 'name_' in params:
               self.name_=params['name_']
    
   def start(self):
        '''
            starts the task
        '''
        pass
   def abort(self):
        '''
            aborts the task
        '''
        pass
   def complete(self):
        '''
            cmpletes the task
        '''
        pass
   def wait(self, time_):
        '''
            set task to wait, param time in miliseconds 
        '''
        pass
   def waitUntil(self, datetime_):
        '''
            sets task to wait until date time comes
        '''
        pass
   def doJob(self):
        '''
            if task contains code__ param it executes the code and sets
            params to corresponding fields
        '''
        pass
   def serialize(self):
      pass
   
    
class Task(BaseTask):
    def start(self):
        pass
    
