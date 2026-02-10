from App import app, ViewNotLoadedYetError

class Section:
    @property
    def section_name(self) -> list:
        return self.getName()

    @property
    def append_prefix(self): # -> dict[str, int]
        '''
        Thing that shows id of some object like:

        DownloadItem->1
        '''
        return None

    def log_message(self, *args, **kwargs):
        # It's better to create Log instance here, but it will call recursive import or smth, so doing sh.code
        _sections = self.section_name
        if kwargs.get('section') != None:
            _sections += kwargs.get('section')

        kwargs["section"] = _sections

        try:
            return app.Logger.log(*args, **kwargs)
        except ViewNotLoadedYetError:
            pass
        except AttributeError:
            pass
            #print("logger not initialized; ", args[0])
        except Exception as e:
            raise (e)
            print("logger error; ", args[0])

    def log(self, *args, **kwargs):
        if self.append_prefix != None:
            kwargs["prefix"] = self.append_prefix

        return self.log_message(*args, **kwargs)

    def log_error(self, *args, **kwargs):
        if kwargs.get('role') == None:
            kwargs['role'] = []
        kwargs.get('role').append('error')
        return self.log(*args, **kwargs)

    def log_success(self, *args, **kwargs):
        if kwargs.get('role') == None:
            kwargs['role'] = []
        kwargs.get('role').append('success')
        return self.log(*args, **kwargs)

    def fatal(self, exception):
        pass
