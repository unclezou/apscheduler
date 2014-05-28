__all__ = ('EVENT_SCHEDULER_START', 'EVENT_SCHEDULER_SHUTDOWN', 'EVENT_JOBSTORE_ADDED', 'EVENT_JOBSTORE_REMOVED',
           'EVENT_JOBSTORE_JOB_ADDED', 'EVENT_JOBSTORE_JOB_REMOVED', 'EVENT_JOBSTORE_JOB_MODIFIED',
           'EVENT_JOB_EXECUTED', 'EVENT_JOB_ERROR', 'EVENT_JOB_MISSED', 'EVENT_ALL', 'SchedulerEvent', 'JobStoreEvent',
           'JobEvent')


EVENT_SCHEDULER_START = 1
EVENT_SCHEDULER_SHUTDOWN = 2
EVENT_JOBSTORE_ADDED = 4
EVENT_JOBSTORE_REMOVED = 8
EVENT_JOBSTORE_JOB_ADDED = 16
EVENT_JOBSTORE_JOB_REMOVED = 32
EVENT_JOBSTORE_JOB_MODIFIED = 64
EVENT_JOB_EXECUTED = 128
EVENT_JOB_ERROR = 256
EVENT_JOB_MISSED = 512
EVENT_ALL = (EVENT_SCHEDULER_START | EVENT_SCHEDULER_SHUTDOWN | EVENT_JOBSTORE_ADDED | EVENT_JOBSTORE_REMOVED |
             EVENT_JOBSTORE_JOB_ADDED | EVENT_JOBSTORE_JOB_REMOVED | EVENT_JOBSTORE_JOB_MODIFIED | EVENT_JOB_EXECUTED |
             EVENT_JOB_ERROR | EVENT_JOB_MISSED)


class SchedulerEvent(object):
    """
    An event that concerns the scheduler itself.

    :ivar code: the type code of this event
    """

    def __init__(self, code):
        super(SchedulerEvent, self).__init__()
        self.code = code

    def __repr__(self):
        return '<%s (code=%d)>' % (self.__class__.__name__, self.code)


class JobStoreEvent(SchedulerEvent):
    """
    An event that concerns job stores.

    :ivar jobstore_alias: the alias of the job store involved
    :ivar job_id: identifier of the new job if a job was added
    """

    def __init__(self, code, jobstore_alias, job_id=None):
        super(JobStoreEvent, self).__init__(code)
        self.jobstore_alias = jobstore_alias
        if job_id:
            self.job_id = job_id


class JobEvent(SchedulerEvent):
    """
    An event that concerns the execution of individual jobs.

    :ivar job_id: identifier of the job in question
    :ivar scheduled_run_time: the time when the job was scheduled to be run
    :ivar retval: the return value of the successfully executed job
    :ivar exception: the exception raised by the job
    :ivar traceback: the traceback object associated with the exception
    """

    def __init__(self, code, job_id, scheduled_run_time, retval=None, exception=None, traceback=None):
        super(JobEvent, self).__init__(code)
        self.job_id = job_id
        self.scheduled_run_time = scheduled_run_time
        self.retval = retval
        self.exception = exception
        self.traceback = traceback
