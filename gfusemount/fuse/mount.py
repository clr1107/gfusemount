class Mount:
    def __init__(self, remote, local, volname=None, volicon=None, fs_flags=None):
        if fs_flags is None:
            fs_flags = dict()

        self.remote = remote
        self.local = local
        self.volname = volname
        self.volicon = volicon
        self.fs_flags = fs_flags


class SSHMount(Mount):
    def __init__(self, remote, local, volname=None, volicon=None, fs_flags=None, fs_options=None):
        if fs_flags is None:
            fs_flags = dict()
        if fs_options is None:
            fs_options = list()

        super().__init__(remote, local, volname, volicon, fs_flags)
        self.fs_options = fs_options

        self.set_options()
        self.set_flags()

    def set_options(self):
        for option in self.fs_options:
            self.fs_flags[option] = None

    def set_flags(self):
        if self.volname is not None:
            self.fs_flags['volname'] = self.volname
        if self.volicon is not None:
            self.fs_flags['volicon'] = self.volicon
