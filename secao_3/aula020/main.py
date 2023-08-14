from log import LogPrintMixin, LogFileMixin

lp = LogPrintMixin()
lf = LogFileMixin()

lf.log_error('erro do main')
lf.log_success('aqui é do main')

